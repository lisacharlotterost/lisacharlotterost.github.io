import os
import re

# Base directory where your year folders are located
base_dir = '/Users/lisa/gitspace/lisacharlotterost.github.io/_notes/'

def update_tweet_permalink(file_path, date_str):
    """
    Adds a permalink to the frontmatter of the tweet file.
    Example: permalink: notes/2014/01/15-1
    """
    with open(file_path, 'r') as f:
        content = f.read()

    # Format the date for the permalink (YYYY-MM-DD -> YYYY/MM/DD)
    formatted_date = date_str.replace('-', '/')
    permalink_line = f"permalink: notes/{formatted_date}-1\n"

    # Regex to find the frontmatter (text between the first pair of ---)
    frontmatter_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
    match = frontmatter_pattern.match(content)

    if match:
        existing_frontmatter = match.group(1)
        # Check if permalink already exists to avoid duplicates
        if 'permalink:' not in existing_frontmatter:
            new_frontmatter = f"---\n{existing_frontmatter}\n{permalink_line}---"
            new_content = frontmatter_pattern.sub(new_frontmatter + "\n", content)
            
            with open(file_path, 'w') as f:
                f.write(new_content)
            print(f"Updated: {file_path}")
        else:
            print(f"Skipped (already has permalink): {file_path}")

# Iterate through year folders (e.g., 2013, 2014, 2016...)
for year_folder in os.listdir(base_dir):
    year_path = os.path.join(base_dir, year_folder)
    
    if os.path.isdir(year_path) and year_folder.isdigit():
        files = os.listdir(year_path)
        
        # Group files by their date prefix (e.g., '2016-01-25')
        for filename in files:
            if filename.endswith("-notes.md"):
                date_prefix = filename.replace("-notes.md", "")
                tweet_filename = f"{date_prefix}-tweet.md"
                
                # If a corresponding tweet file exists for this note
                if tweet_filename in files:
                    tweet_path = os.path.join(year_path, tweet_filename)
                    update_tweet_permalink(tweet_path, date_prefix)

print("Finished processing folders.")
