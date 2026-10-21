
from bs4 import BeautifulSoup
import requests
from ytmusicapi import YTMusic

# STEP 1: Ask for a date
date = input(
    "Which date do you want to travel to? (YYYY-MM-DD): "
).strip()

# STEP 2: Scrape Billboard song titles and artists
url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"

response = requests.get(url, timeout=30)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

song_elements = soup.select("h3.chart-entry__title")
songs = []

for song_element in song_elements:
    # Try to find the artist in the same chart entry
    entry = song_element.find_parent(
        class_="chart-entry"
    )

    artist_element = (
        entry.select_one(".chart-entry__artist")
        if entry else None
    )

    title = song_element.get_text(strip=True)
    artist = (
        artist_element.get_text(strip=True)
        if artist_element else ""
    )

    songs.append({
        "title": title,
        "artist": artist
    })

if not songs:
    print("No songs found. Check the date and webpage.")
    raise SystemExit

print(f"Found {len(songs)} Billboard songs.")

# STEP 3: Connect to YouTube Music
yt = YTMusic("browser.json")

playlist_name = f"{date} Billboard 100"

# Check whether this playlist already exists
playlists = yt.get_library_playlists()
playlist_id = None

for playlist in playlists:
    if playlist.get("title") == playlist_name:
        playlist_id = playlist.get("playlistId")
        print("Playlist already exists. Reusing it.")
        break

# Create a new private playlist if necessary
if playlist_id is None:
    playlist_id = yt.create_playlist(
        title=playlist_name,
        description=f"Billboard Hot 100 for {date}",
        privacy_status="PRIVATE"
    )
    print(f"Created private playlist: {playlist_name}")

# Get the songs already in the playlist
existing_video_ids = set()

try:
    playlist_data = yt.get_playlist(
        playlist_id,
        limit=None
    )

    for track in playlist_data.get("tracks", []):
        video_id = track.get("videoId")
        if video_id:
            existing_video_ids.add(video_id)

except Exception as error:
    print(f"Could not check existing songs: {error}")

# STEP 4: Search for and add each song
added_count = 0
skipped_count = 0

for song in songs:
    title = song["title"]
    artist = song["artist"]

    search_query = f"{title} {artist}".strip()

    try:
        results = yt.search(
            search_query,
            filter="songs"
        )

        if not results:
            print(f"Not found: {search_query}")
            skipped_count += 1
            continue

        video_id = results[0].get("videoId")

        if not video_id:
            print(f"No video ID: {search_query}")
            skipped_count += 1
            continue

        if video_id in existing_video_ids:
            print(f"Already in playlist: {search_query}")
            skipped_count += 1
            continue

        yt.add_playlist_items(
            playlistId=playlist_id,
            videoIds=[video_id]
        )

        existing_video_ids.add(video_id)
        added_count += 1
        print(f"Added: {search_query}")

    except Exception as error:
        print(f"Skipped {search_query}: {error}")
        skipped_count += 1
        continue

# STEP 5: Display the summary
print("\n--- Playlist Summary ---")
print(f"Playlist: {playlist_name}")
print(f"New songs added: {added_count}")
print(f"Songs skipped: {skipped_count}")
print(
    "Open YouTube Music: "
    "https://music.youtube.com/library/playlists"
)
