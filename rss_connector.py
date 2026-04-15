import feedparser
import time

/**
 * MODULE: Bureau RSS Syndicator
 * AUTHORITY: The Peculiar Librarian (@thebureau)
 * TARGET: https://coderlegion.com/rss/peculiarlibrarian
 */

def fetch_bureau_stream(rss_url):
    print(f"--- [SYNCING WITH NAIROBI-01-NODE RSS] ---")
    feed = feedparser.parse(rss_url)
    
    if not feed.entries:
        print("✘ NO DATA DETECTED IN STREAM.")
        return

    for entry in feed.entries[:5]:  # Capture the Top 5 Apex posts
        print(f"\n[ENTRY VALIDATED]")
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print("-" * 30)

if __name__ == "__main__":
    BUREAU_RSS = "https://coderlegion.com/rss/peculiarlibrarian"
    fetch_bureau_stream(BUREAU_RSS)
