import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Capture any YouTube embed video ID
    match = re.search(r'<iframe[^>]+src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"', s)

    if match:
        video_id = match.group(1)  # Extract the video ID
        return f"https://youtu.be/{video_id}"
    return None  # Return None if no match is found

if __name__ == "__main__":
    main()
