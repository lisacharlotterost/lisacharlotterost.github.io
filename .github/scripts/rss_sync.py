#!/usr/bin/env python3
"""
Syncs Tumblr posts to Jekyll and generates 600px thumbnails.
Requires: pip install requests Pillow
"""

import os
import re
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from email.utils import parsedate_to_datetime
from PIL import Image, ImageSequence

# Configuration
RSS_FEED_URL = os.environ.get('RSS_FEED_URL', 'https://thelisaproject.tumblr.com/rss')
POSTS_DIR = Path('_notes')
IMAGES_DIR = Path('pic/notes')
THUMBS_DIR = Path('pic/thumbs/notes')
TRACK_FILE = Path('.github/synced_posts.txt')

# Create directories
POSTS_DIR.mkdir(exist_ok=True)
IMAGES_DIR.mkdir(parents=True, exist_ok=True)
THUMBS_DIR.mkdir(parents=True, exist_ok=True)
TRACK_FILE.parent.mkdir(parents=True, exist_ok=True)

def load_synced_posts():
    if TRACK_FILE.exists():
        return set(TRACK_FILE.read_text().strip().split('\n'))
    return set()

def save_synced_post(guid):
    with TRACK_FILE.open('a') as f:
        f.write(f"{guid}\n")

def extract_hashtags(text):
    """
    Finds lines starting with hashtags, extracts the tags, 
    and returns the cleaned text (without the hashtag lines) and the list of tags.
    """
    tags = []
    lines = text.split('\n')
    remaining_lines = []

    for line in lines:
        stripped = line.strip()
        # Look for lines starting with # (but not markdown headers like # Title)
        if stripped.startswith('#') and not re.match(r'^#\s', stripped):
            # Find all hashtags in this line: #word or #multi word string
            # This regex looks for # followed by text until the next # or end of line
            found = re.findall(r'#([^#\n]+)', stripped)
            tags.extend([t.strip() for t in found if t.strip()])
        else:
            remaining_lines.append(line)
            
    return "\n".join(remaining_lines).strip(), tags

def clean_html(html_text):
    if not html_text: return ""
    text = re.sub(r'<b>(.*?)</b>', r'**\1**', html_text)
    text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text)
    text = re.sub(r'<i>(.*?)</i>', r'*\1*', text)
    text = re.sub(r'<em>(.*?)</em>', r'*\1*', text)
    text = re.sub(r'<a[^>]+href=["\'](.*?)["\'][^>]*>(.*?)</a>', r'[\2](\1)', text)
    text = re.sub(r'<p>', '', text)
    text = re.sub(r'</p>', '\n\n', text)
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    text = text.replace('&quot;', '"').replace('&apos;', "'")
    text = text.replace('&hellip;', '…').replace('&rsquo;', "'")
    text = text.replace('&ldquo;', '"').replace('&rdquo;', '"')
    text = text.replace('&nbsp;', ' ')
    text = re.sub(r'\n\n\n+', '\n\n', text)
    return text.strip()

def extract_images(description):
    if not description: return []
    images = []
    img_pattern = r'srcset=["\']([^"\']+)["\']'
    srcset_matches = re.findall(img_pattern, description)
    
    for srcset_value in srcset_matches:
        variants = srcset_value.split(',')
        candidates = []
        for v in variants:
            parts = v.strip().split()
            if len(parts) >= 2 and parts[-1].endswith('w'):
                try:
                    width = int(parts[-1][:-1])
                    url = parts[0]
                    candidates.append((width, url))
                except ValueError: pass
            elif len(parts) >= 1:
                candidates.append((0, parts[0]))
        
        candidates.sort(key=lambda x: x[0], reverse=True)
        if candidates:
            images.append(candidates[0][1])

    if not images:
        src_pattern = r'<img[^>]+src=["\'](https?://[^"\']+)["\']'
        images = re.findall(src_pattern, description)
    return images

def generate_thumbnail(source_path, dest_path, size=600):
    """Generates 600px width thumb. Static for images, animated for GIFs."""
    try:
        with Image.open(source_path) as img:
            # Scale height to maintain aspect ratio
            w_percent = (size / float(img.size[0]))
            h_size = int((float(img.size[1]) * float(w_percent)))
            
            if img.format == 'GIF':
                frames = []
                for frame in ImageSequence.Iterator(img):
                    # Use fast resizing for GIF frames to save Action time
                    frame = frame.convert('RGBA').resize((size, h_size), Image.Resampling.NEAREST)
                    frames.append(frame)
                frames[0].save(dest_path, save_all=True, append_images=frames[1:], loop=0, optimize=True)
            else:
                img = img.convert("RGB")
                img = img.resize((size, h_size), Image.Resampling.LANCZOS)
                img.save(dest_path, "JPEG", quality=80, optimize=True)
            print(f"    ✓ Thumbnail created: {dest_path.name}")
    except Exception as e:
        print(f"    ! Thumbnail error: {e}")

def download_image(url, post_id):
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        ext = Path(urlparse(url).path).suffix.lower() or '.jpg'
        if ext == '.gifv': ext = '.gif'
        
        filename = f"{post_id}-{hash(url) & 0xffffffff:08x}{ext}"
        filepath = IMAGES_DIR / filename
        thumb_path = THUMBS_DIR / filename
        
        if not filepath.exists():
            filepath.write_bytes(response.content)
            
        if not thumb_path.exists():
            generate_thumbnail(filepath, thumb_path)
            
        return f"/pic/notes/{filename}"
    except Exception as e:
        print(f"Failed download {url}: {e}")
        return url

def main():
    print(f"Fetching RSS feed...")
    try:
        response = requests.get(RSS_FEED_URL, timeout=30)
        response.raise_for_status()
        root = ET.fromstring(response.content)
        channel = root.find('channel')
        items = channel.findall('item') if channel is not None else root.findall('item')
    except Exception as e:
        print(f"Error: {e}")
        return

    synced_posts = load_synced_posts()
    new_posts = 0
    items_to_process = items[:10]
    
    for item in reversed(items_to_process):
        guid = item.find('guid').text if item.find('guid') is not None else ''
        title = item.find('title').text if item.find('title') is not None else 'Untitled'
        description = item.find('description').text if item.find('description') is not None else ''
        pub_date_str = item.find('pubDate').text if item.find('pubDate') is not None else ''
        
        if not guid or guid in synced_posts:
            continue
            
        print(f"Processing: {title[:30]}...")
        try:
            date_obj = parsedate_to_datetime(pub_date_str)
            date_str = date_obj.strftime('%Y-%m-%d')
        except: continue

        images = extract_images(description)
        raw_content = clean_html(description)
        
        # NEW: Process hashtags
        content, extracted_tags = extract_hashtags(raw_content)
        
        post_id = guid.split('/')[-1]
        local_images = []
        for img_url in images:
            local_images.append(download_image(img_url, post_id))

        filename = f"{date_str}-notes.md"
        filepath = POSTS_DIR / filename
        
        # Build Front Matter
        frontmatter = ["---", "categories: [notes]"]
        
        # Add extracted tags if they exist
        if extracted_tags:
            # Format as YAML list: tags: [tag1, tag2]
            tag_string = ", ".join(extracted_tags)
            frontmatter.append(f"tags: [{tag_string}]")
            
        if local_images:
            frontmatter.append(f"image: {local_images[0]}")
        frontmatter.extend(["---", ""])
        
        post_content = "\n".join(frontmatter)
        for img_path in local_images:
            post_content += f"![]({img_path})\n\n"
        post_content += content
        
        filepath.write_text(post_content, encoding='utf-8')
        save_synced_post(guid)
        new_posts += 1

    print(f"Finished. {new_posts} new posts created.")

if __name__ == '__main__':
    main()
