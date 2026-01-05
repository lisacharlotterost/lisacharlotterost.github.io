#!/usr/bin/env python3
"""
Syncs posts from an RSS feed to Jekyll blog posts.
"""

import os
import re
import yaml
import feedparser
import requests
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse

# Configuration
RSS_FEED_URL = os.environ.get('RSS_FEED_URL', 'https://thelisaproject.tumblr.com/rss')
POSTS_DIR = Path('_notes')
IMAGES_DIR = Path('pic/notes')
TRACK_FILE = Path('.github/synced_posts.txt')

# Create directories if they don't exist
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
    # Convert bold
    text = re.sub(r'<b>(.*?)</b>', r'**\1**', html_text)
    text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text)
    
    # Convert italic
    text = re.sub(r'<i>(.*?)</i>', r'*\1*', text)
    text = re.sub(r'<em>(.*?)</em>', r'*\1*', text)
    
    # Convert links
    text = re.sub(r'<a[^>]+href=["\'](.*?)["\'][^>]*>(.*?)</a>', r'[\2](\1)', text)
    
    # Convert paragraphs to double newlines
    text = re.sub(r'<p>', '', text)
    text = re.sub(r'</p>', '\n\n', text)
    
    # Convert line breaks
    text = re.sub(r'<br\s*/?>', '\n', text)
    
    # Remove remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Decode HTML entities
    text = text.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    text = text.replace('&quot;', '"').replace('&apos;', "'")
    text = text.replace('&hellip;', '…').replace('&rsquo;', "'")
    text = text.replace('&ldquo;', '"').replace('&rdquo;', '"')
    text = text.replace('&nbsp;', ' ')
    
    # Clean up excessive whitespace
    text = re.sub(r'\n\n\n+', '\n\n', text)
    
    return text.strip()

def extract_images(description):
    """Extract highest quality image URLs from HTML description"""
    images = []
    
    # Look for img tags with srcset attribute
    img_pattern = r'<img[^>]*srcset=["\'](.*?)["\'][^>]*>'
    img_matches = re.findall(img_pattern, description, re.DOTALL)
    
    print(f"Found {len(img_matches)} images with srcset")
    
    for idx, srcset_value in enumerate(img_matches):
        print(f"\n--- Processing image {idx + 1} ---")
        # Split by comma to get individual entries
        srcset_entries = srcset_value.split(',')
        print(f"Found {len(srcset_entries)} size variants")
        
        max_width = 0
        best_url = None
        
        for entry in srcset_entries:
            entry = entry.strip()
            # Split from right to separate URL and width descriptor
            parts = entry.rsplit(None, 1)
            if len(parts) == 2:
                url = parts[0]
                width_str = parts[1]
                if width_str.endswith('w'):
                    try:
                        width = int(width_str[:-1])
                        print(f"  {width}w: {url[:60]}...")
                        if width > max_width:
                            max_width = width
                            best_url = url
                    except ValueError:
                        continue
        
        if best_url:
            print(f"✓ Selected: {max_width}w")
            images.append(best_url)
        else:
            print("✗ No valid image found")
    
    # Fallback: look for regular src attributes if no srcset found
    if not images:
        simple_pattern = r'<img[^>]+src=["\'](https?://[^"\']+)["\']'
        images = re.findall(simple_pattern, description)
        print(f"Fallback to src attribute, found {len(images)} images")
    
    return images

def download_image(url, post_id):
    """Download image and return local path"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Get file extension from URL or content-type
        ext = Path(urlparse(url).path).suffix or '.jpg'
        if ext == '.gifv':
            ext = '.gif'
        
        # Create filename: use post_id plus hash for uniqueness
        filename = f"{post_id}-{hash(url) & 0xffffffff:08x}{ext}"
        filepath = IMAGES_DIR / filename
        
        # Skip if already downloaded
        if filepath.exists():
            return f"/pic/notes/{filename}"
        
        filepath.write_bytes(response.content)
        return f"/pic/notes/{filename}"
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return url  # Return original URL if download fails

def create_jekyll_post(entry):
    """Convert RSS entry to Jekyll post"""
    # Extract post details
    guid = entry.get('guid', entry.get('id', ''))
    link = entry.get('link', '')
    description = entry.get('description', '')
    pub_date = entry.get('published_parsed')
    
    if not pub_date:
        print(f"Skipping post without date")
        return False
    
    # Convert date
    date = datetime(*pub_date[:6])
    date_str = date.strftime('%Y-%m-%d')
    
    # Extract images
    images = extract_images(description)
    
    # Clean content
    content = clean_html(description)
    
    # Create post ID from GUID
    post_id = guid.split('/')[-1]
    
    # Download images and update references
    local_images = []
    for img_url in images:
        local_path = download_image(img_url, post_id)
        local_images.append(local_path)
    
    # Create filename: date-notes.md
    filename = f"{date_str}-notes.md"
    filepath = POSTS_DIR / filename
    
    # Skip if file already exists
    if filepath.exists():
        return False
    
    # Generate title from date
    title = date.strftime('%B %d, %Y')  # e.g., "October 16, 2024"
    
    # Generate permalink
    permalink = f"notes/{date.year}/{date.month:02d}/{date.day:02d}"
    
    # Generate summary (first 100 chars of content)
    summary = content[:100] + '...' if len(content) > 100 else content
    summary = summary.replace('\n', ' ').strip()
    
    # Create frontmatter (order matters for your format)
    frontmatter_lines = [
        "---",
        "categories: [notes]",
        "comments: disabled",
    ]
    
    # Add image if available
    if local_images:
        frontmatter_lines.append(f"image: {local_images[0]}")
    
    frontmatter_lines.extend([
        "layout: post",
        f"permalink: {permalink}",
        f"summary: {summary}",
        f"title: {title}",
        f"date: {date_str}",
        "---",
    ])
    
    # Create post content
    post_content = '\n'.join(frontmatter_lines) + '\n\n'
    
    # Add images to content
    for img_path in local_images:
        post_content += f"![]({img_path})\n\n"
    
    # Add text content
    if content:
        post_content += f"{content}\n"
    
    # Write post file
    filepath.write_text(post_content, encoding='utf-8')
    print(f"Created post: {filename}")
    
    return True

def main():
    """Main sync function"""
    print(f"Fetching RSS feed from {RSS_FEED_URL}...")
    feed = feedparser.parse(RSS_FEED_URL)
    
    if feed.bozo:
        print(f"Warning: Feed parsing error: {feed.bozo_exception}")
    
    synced_posts = load_synced_posts()
    new_posts = 0
    
    print(f"Found {len(feed.entries)} entries in feed")
    print(f"Already synced {len(synced_posts)} posts")
    
    # Only process the last 3 entries
    entries_to_process = feed.entries[:3]
    print(f"Checking the last {len(entries_to_process)} entries")
    
    # Process entries in reverse order (oldest first of the 3)
    for entry in reversed(entries_to_process):
        guid = entry.get('guid', entry.get('id', ''))
        title = entry.get('title', 'Untitled')[:50]
        
        if not guid:
            print("Skipping entry without GUID")
            continue
        
        if guid in synced_posts:
            print(f"Already synced: {title} ({guid})")
            continue
        
        print(f"Processing new entry: {title} ({guid})")
        
        try:
            if create_jekyll_post(entry):
                save_synced_post(guid)
                new_posts += 1
                print(f"✓ Successfully created post for: {title}")
        except Exception as e:
            print(f"✗ Error processing entry {guid}: {e}")
            import traceback
            traceback.print_exc()
    
    if new_posts == 0:
        print("\nNo new posts to sync. All recent entries already processed.")
    else:
        print(f"\n✓ Sync complete! Created {new_posts} new posts.")


if __name__ == '__main__':
    main()
