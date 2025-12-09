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
    """Remove HTML tags and clean up text"""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', html_text)
    # Decode HTML entities
    text = text.replace('&lt;', '<').replace('&gt;', '>').replace('&amp;', '&')
    text = text.replace('&quot;', '"').replace('&apos;', "'")
    return text.strip()

def extract_images(description):
    """Extract image URLs from HTML description"""
    img_pattern = r'<img[^>]+src=["\'](https?://[^"\']+)["\']'
    return re.findall(img_pattern, description)

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
    
    # Process entries in reverse order (oldest first)
    for entry in reversed(feed.entries):
        guid = entry.get('guid', entry.get('id', ''))
        
        if not guid:
            print("Skipping entry without GUID")
            continue
        
        if guid in synced_posts:
            continue
        
        try:
            if create_jekyll_post(entry):
                save_synced_post(guid)
                new_posts += 1
        except Exception as e:
            print(f"Error processing entry {guid}: {e}")
    
    print(f"\nSync complete! Created {new_posts} new posts.")

if __name__ == '__main__':
    main()
