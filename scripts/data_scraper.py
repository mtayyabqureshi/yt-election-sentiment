import csv
import os
import time
import json
import random
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Output CSV file
CSV_FILE = "data/youtube_comments.csv"

# Rotating API keys to handle quota limits
API_KEYS = [
    "YOUR_API_KEY_1",
    "YOUR_API_KEY_2",
    "YOUR_API_KEY_3"
]
current_key_index = 0

# List of YouTube video IDs with metadata
video_list = [
    {"video_id": "xrFdHO7FH8w", "candidate": "Donald Trump", "podcast": "IMPAULSIVE", "host_name": "Logan Paul"},
    {"video_id": "blqIZGXWUpU", "candidate": "Donald Trump", "podcast": "All-In Podcast", "host_name": "Chamath Palihapitiya et al."},
    {"video_id": "s11uIW7wi-E", "candidate": "Donald Trump", "podcast": "Adin Ross", "host_name": "Adin Ross"},
    # Add more entries as needed
]

def get_api_key():
    """Rotate through API keys."""
    global current_key_index
    key = API_KEYS[current_key_index]
    current_key_index = (current_key_index + 1) % len(API_KEYS)
    return key

def append_comments_to_csv(video, comments):
    """Append comments to the output CSV."""
    os.makedirs(os.path.dirname(CSV_FILE), exist_ok=True)
    file_exists = os.path.isfile(CSV_FILE)

    with open(CSV_FILE, mode="a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Candidate", "Podcast", "Host", "Author", "Comment", "Likes", "Is Reply"])

        for comment in comments:
            writer.writerow([
                video["candidate"], video["podcast"], video["host_name"],
                comment.get("author", "Unknown"),
                comment.get("text", ""),
                comment.get("likes", 0),
                comment.get("is_reply", "No")
            ])

def get_youtube_comments(video_id, api_key, page_token=None, max_retries=5):
    """Fetch comments using YouTube API."""
    youtube = build('youtube', 'v3', developerKey=api_key)
    retries = 0

    while retries < max_retries:
        try:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                pageToken=page_token,
                maxResults=100
            )
            response = request.execute()

            comments = [
                {
                    "author": item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
                    "text": item["snippet"]["topLevelComment"]["snippet"]["textDisplay"],
                    "likes": item["snippet"]["topLevelComment"]["snippet"]["likeCount"],
                    "is_reply": "No"
                }
                for item in response.get("items", [])
            ]

            return comments, response.get("nextPageToken")

        except HttpError as e:
            print(f"API error: {e}")
            return None, None

        except Exception as e:
            print(f"Unexpected error: {e}")
            return None, None

def save_progress(index, page_token):
    """Save scraping progress."""
    with open("progress.json", "w") as f:
        json.dump({"current_video": index, "next_page_token": page_token}, f)

def load_progress():
    """Load saved progress."""
    if os.path.exists("progress.json"):
        with open("progress.json", "r") as f:
            return json.load(f)
    return {"current_video": 0, "next_page_token": None}

def main():
    progress = load_progress()
    start_index = progress["current_video"]
    next_page_token = progress["next_page_token"]

    for i, video in enumerate(video_list[start_index:], start=start_index):
        print(f"Fetching comments for: {video['podcast']}")

        while True:
            api_key = get_api_key()
            comments, next_page_token = get_youtube_comments(video["video_id"], api_key, next_page_token)

            if comments is None:
                break

            append_comments_to_csv(video, comments)
            save_progress(i, next_page_token if next_page_token else "")

            if not next_page_token:
                break

    print("All videos processed.")

if __name__ == "__main__":
    main()
