#!/usr/bin/env python3
"""
Syncs posts using requests + xml.etree (Bypasses feedparser sanitization)
"""

import os
import re
import requests
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
from email.utils import parsedate_to_datetime

# Configuration
RSS_FEED_URL = os.environ.get('RSS_FEED_URL', 'https://thelisaproject.tumblr.com/rss')
POSTS_DIR = Path('_notes')
IMAGES_DIR = Path('pic/notes')
TRACK_FILE = Path('.github/synced_posts.txt')

# Create directories
POSTS_DIR.mkdir(exist_ok=True)
IMAGES_DIR.mkdir(parents=True, exist_ok=True)
TRACK_FILE.parent.mkdir(parents=True, exist_ok=True)

def load_synced_posts():
    """Load list of already synced post GUIDs"""
    if TRACK_FILE.exists():
        return set(TRACK_FILE.read_text().strip().split('\n'))
    return set()

def save_synced_post(guid):
    """Save a post GUID as synced"""
    with TRACK_FILE.open('a') as f:
        f.write(f"{guid}\n")

def clean_html(html_text):
    """Convert HTML to Markdown"""
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
    """Robust image extraction looking for the W descriptor inside srcset"""
    if not description: return []
    images = []
    
    # Pattern to find srcset content: looks for srcset="..."
    img_pattern = r'srcset=["\']([^"\']+)["\']'
    srcset_matches = re.findall(img_pattern, description)
    
    print(f"  Found {len(srcset_matches)} image groups (srcset)")

    for srcset_value in srcset_matches:
        variants = srcset_value.split(',')
        candidates = []
        for v in variants:
            parts = v.strip().split()
            # Look for URL + Space + Width (e.g. "http://... 2048w")
            if len(parts) >= 2 and parts[-1].endswith('w'):
                try:
                    width = int(parts[-1][:-1])
                    url = parts[0]
                    candidates.append((width, url))
                except ValueError: pass
            # Handle cases with just URL (assume small/0 priority)
            elif len(parts) >= 1:
                candidates.append((0, parts[0]))
        
        # Sort by width (highest first)
        candidates.sort(key=lambda x: x[0], reverse=True)
        
        if candidates:
            best_width, best_url = candidates[0]
            print(f"  ✓ Selected largest: {best_width}w -> {best_url.split('/')[-1]}")
            images.append(best_url)

    # Fallback to src if absolutely no srcset found
    if not images:
        print("  ! No srcset found, falling back to basic src attributes")
        src_pattern = r'<img[^>]+src=["\'](https?://[^"\']+)["\']'
        images = re.findall(src_pattern, description)
        
    return images

def download_image(url, post_id):
    """Download image and return local path"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        ext = Path(urlparse(url).path).suffix or '.jpg'
        if ext == '.gifv': ext = '.gif'
        filename = f"{post_id}-{hash(url) & 0xffffffff:08x}{ext}"
        filepath = IMAGES_DIR / filename
        
        if filepath.exists():
            return f"/pic/notes/{filename}"
            
        filepath.write_bytes(response.content)
        return f"/pic/notes/{filename}"
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return url

def main():
    print(f"Fetching RSS feed from {RSS_FEED_URL}...")
    
    # 1. Download RAW XML (Bypassing feedparser)
    try:
        response = requests.get(RSS_FEED_URL, timeout=30)
        response.raise_for_status()
        xml_content = response.content
    except Exception as e:
        print(f"Error fetching feed: {e}")
        return

    # 2. Parse XML directly
    try:
        root = ET.fromstring(xml_content)
        # Standard RSS path: channel -> item
        channel = root.find('channel')
        if channel is None: channel = root # Handle cases where items are at root
        items = channel.findall('item')
        print(f"Found {len(items)} items in feed")
    except Exception as e:
        print(f"Error parsing XML: {e}")
        return

    synced_posts = load_synced_posts()
    new_posts = 0
    
    # Process all items (limit inside loop if needed)
    # Reversing so we process oldest first
    
    # Slice the last 3 items for testing/syncing
    items_to_process = items[:3]
    
    for item in reversed(items_to_process):
        # Extract fields using XML find
        guid = item.find('guid').text if item.find('guid') is not None else ''
        title = item.find('title').text if item.find('title') is not None else 'Untitled'
        description = item.find('description').text if item.find('description') is not None else ''
        pub_date_str = item.find('pubDate').text if item.find('pubDate') is not None else ''
        
        if not guid:
            continue

        if guid in synced_posts:
            print(f"Skipping already synced: {title[:30]}")
            continue
            
        print(f"\nProcessing new entry: {title[:30]}...")
        
        # Parse Date
        try:
            date_obj = parsedate_to_datetime(pub_date_str)
            date_str = date_obj.strftime('%Y-%m-%d')
        except:
            print("  Skipping (no valid date)")
            continue

        # Extract Images (Using the new robust logic on RAW description)
        images = extract_images(description)
        content = clean_html(description)
        post_id = guid.split('/')[-1]

        local_images = []
        for img_url in images:
            local_path = download_image(img_url, post_id)
            local_images.append(local_path)

        # Create Jekyll Post
        filename = f"{date_str}-notes.md"
        filepath = POSTS_DIR / filename
        
        if filepath.exists(): 
            print("  File already exists, skipping write.")
            # We still mark as synced to prevent reprocessing
            save_synced_post(guid)
            continue

        frontmatter = [
            "---",
            "categories: [notes]",
            "comments: disabled",
        ]
        if local_images:
            frontmatter.append(f"image: {local_images[0]}")
            
        frontmatter.extend([
            "layout: post",
            f"permalink: notes/{date_obj.year}/{date_obj.month:02d}/{date_obj.day:02d}",
            "---",
            ""
        ])
        
        post_content = "\n".join(frontmatter)
        for img_path in local_images:
            post_content += f"![]({img_path})\n\n"
        post_content += content
        
        filepath.write_text(post_content, encoding='utf-8')
        save_synced_post(guid)
        new_posts += 1
        print(f"  ✓ Created post {filename}")

    if new_posts > 0:
        print(f"\n✓ Sync complete! {new_posts} new posts.")
    else:
        print("\nNo new posts to create.")

if __name__ == '__main__':
    main()
