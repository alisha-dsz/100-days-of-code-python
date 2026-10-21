# Day 46 - YouTube Music Playlist Project

## 📖 Overview

The YouTube Music Playlist Project is a Python project created as part of the **100 Days of Code: The Complete Python Pro Bootcamp by Angela Yu**.

The project allows users to travel back in time musically by entering a specific date in the `YYYY-MM-DD` format. It retrieves the Billboard Hot 100 chart for the selected date, extracts song titles, searches for matching songs on YouTube Music, and creates a private playlist containing the selected tracks.

The project uses the `requests` library to retrieve webpage content, `BeautifulSoup` from `bs4` to parse HTML and extract song information, and `ytmusicapi` to authenticate with YouTube Music, search for songs, and manage playlists.

This project focuses on web scraping, HTML parsing, API interaction, authentication, playlist management, exception handling, list manipulation, and Python automation.

## 🎯 Objective

Create a Python program that:

- Accepts a date from the user in `YYYY-MM-DD` format.
- Constructs the URL for the Billboard Hot 100 chart for the selected date.
- Sends an HTTP request to retrieve webpage content.
- Parses the HTML using BeautifulSoup.
- Finds HTML elements containing song titles.
- Extracts song titles and artist names where available.
- Authenticates with YouTube Music using `ytmusicapi`.
- Uses a `browser.json` file for authentication configuration.
- Checks whether a playlist with the requested name already exists.
- Creates a private playlist named `{date} Billboard 100` if it does not exist.
- Searches YouTube Music for each song using its title and artist name.
- Uses the top matching song result when available.
- Adds matching songs to the playlist.
- Handles individual search and playlist errors without stopping the entire program.
- Avoids adding tracks that are already present when reusing an existing playlist.
- Displays a summary of the songs added and skipped.

## 🛠️ Concepts Practiced

### Python
- Variables and constants
- Strings and f-strings
- Lists and list comprehensions
- Dictionaries
- Loops and iteration
- Conditional statements
- Exception handling using `try` and `except`
- Working with external libraries

### Web Scraping
- HTTP GET requests
- Retrieving webpage source code
- HTML parsing with BeautifulSoup
- Finding elements by tag name and CSS class
- Extracting text using `get_text()`
- Handling HTTP response errors

### API Interaction and Authentication
- Using the `ytmusicapi` library
- Authenticating with YouTube Music
- Working with browser request headers and cookies
- Loading authentication configuration from `browser.json`
- Searching for songs using `yt.search()`
- Creating playlists using `yt.create_playlist()`
- Retrieving playlists using `yt.get_library_playlists()`
- Adding tracks using `yt.add_playlist_items()`
- Working with playlist IDs and video IDs

### Error Handling
- Using `response.raise_for_status()`
- Handling unsuccessful song searches
- Handling missing video IDs
- Catching exceptions during individual song processing
- Continuing execution when a song cannot be found or added

## 📚 Python Concepts Used

### 1. Importing Libraries

```python
from bs4 import BeautifulSoup
import requests
from ytmusicapi import YTMusic
```

The `requests` library retrieves webpage content.

BeautifulSoup parses HTML and helps locate song information.

`YTMusic` provides methods for authenticating with YouTube Music, searching for songs, creating playlists, and adding tracks.

### 2. Getting the Date from the User

```python
date = input(
    "Which date do you want to travel to? "
    "Type the date in YYYY-MM-DD format: "
).strip()
```

The `input()` function collects the date from the user.

The `.strip()` method removes unnecessary whitespace from the beginning and end of the input.

The date determines which Billboard chart the program retrieves.

### 3. Constructing the URL and Sending an HTTP Request

```python
url = f"https://appbrewery.github.io/bakeboard-hot-100/{date}/"

response = requests.get(url, timeout=30)
response.raise_for_status()
```

An f-string inserts the selected date into the URL.

`requests.get()` sends an HTTP GET request to retrieve the webpage.

The `timeout=30` argument prevents the request from waiting indefinitely.

`response.raise_for_status()` raises an exception if the server returns an unsuccessful HTTP status code.

### 4. Parsing HTML with BeautifulSoup

```python
soup = BeautifulSoup(response.text, "html.parser")
```

`response.text` contains the HTML returned by the website.

`BeautifulSoup()` parses the HTML into a structure that Python can search and navigate.

The `"html.parser"` argument specifies the parser used to interpret the HTML document.

### 5. Extracting Song Titles

```python
song_elements = soup.find_all(
    name="h3",
    class_="chart-entry__title"
)

songs = [
    song.get_text(strip=True)
    for song in song_elements
]
```

The `find_all()` method retrieves matching `<h3>` elements with the specified CSS class.

The list comprehension extracts the text from each element and stores it in a Python list.

The `strip=True` argument removes unnecessary whitespace around the extracted text.

### 6. Authenticating with YouTube Music

```python
yt = YTMusic("browser.json")
```

The `YTMusic` class creates an object used to interact with YouTube Music.

The `browser.json` file contains the authentication configuration generated using `ytmusicapi`.

This configuration allows the program to access supported YouTube Music account features.

**Security note:** The `browser.json` file contains sensitive authentication information and must never be uploaded to GitHub or shared publicly.

### 7. Checking for an Existing Playlist

```python
playlist_name = f"{date} Billboard 100"

playlists = yt.get_library_playlists()
playlist_id = None

for playlist in playlists:
    if playlist.get("title") == playlist_name:
        playlist_id = playlist.get("playlistId")
        break
```

`get_library_playlists()` retrieves playlists from the authenticated user's library.

The loop checks whether a playlist with the requested title already exists.

If a matching playlist is found, its ID is saved and reused instead of creating another playlist with the same name.

### 8. Creating a Private Playlist

```python
if playlist_id is None:
    playlist_id = yt.create_playlist(
        title=playlist_name,
        description=f"Billboard Hot 100 for {date}",
        privacy_status="PRIVATE"
    )
```

If no matching playlist exists, `create_playlist()` creates a new playlist.

The playlist title includes the selected date, for example:

`2000-08-12 Billboard 100`

The `privacy_status="PRIVATE"` argument requests private visibility.

The returned playlist ID identifies the playlist for subsequent operations.

### 9. Searching for Songs

```python
results = yt.search(
    search_query,
    filter="songs"
)
```

The `search()` method searches YouTube Music using a song title and artist name.

The `filter="songs"` argument restricts the search to song results.

The program uses the first matching result when it contains a valid video ID.

Searching with both the title and artist name can improve the relevance of the results.

### 10. Adding Songs to the Playlist

```python
yt.add_playlist_items(
    playlistId=playlist_id,
    videoIds=[video_id]
)
```

The `add_playlist_items()` method adds the selected song to the playlist.

`playlistId` identifies the destination playlist.

`videoIds` contains the YouTube Music video IDs of the tracks to add.

The program can process songs individually so that an unsuccessful search or addition does not prevent the remaining songs from being processed.

### 11. Handling Errors

```python
try:
    results = yt.search(search_query, filter="songs")

    if results and results[0].get("videoId"):
        video_id = results[0]["videoId"]

        yt.add_playlist_items(
            playlistId=playlist_id,
            videoIds=[video_id]
        )

except Exception as error:
    print(f"Could not process {search_query}: {error}")
```

The `try` block contains operations that might fail.

The `except` block catches errors and displays a message instead of immediately terminating the entire song-processing loop.

This is useful because some songs might not be available or a request might fail temporarily.

## 🔄 How the Project Works

The program follows this workflow:

1. Ask the user to enter a date.
2. Construct the Billboard chart URL.
3. Retrieve the webpage using `requests`.
4. Check the HTTP response status.
5. Parse the HTML using BeautifulSoup.
6. Extract song titles and artist names where available.
7. Authenticate with YouTube Music using `browser.json`.
8. Check whether the date-specific playlist already exists.
9. Create a private playlist if necessary.
10. Search YouTube Music for each song.
11. Retrieve the video ID of the top matching song result.
12. Check for existing tracks when reusing a playlist.
13. Add matching songs to the playlist.
14. Handle unsuccessful searches and individual errors.
15. Display a summary of the songs added and skipped.

## 📂 Project Structure

```text
Day-046-YouTube-Music-Playlist-Project/
│
├── main.py          # Main Python program
├── README.md        # Project documentation
├── requirements.txt # Required Python libraries
└── .gitignore       # Files excluded from Git
```

The `browser.json` file must be generated locally by each user and must not be included in the repository.

The `.gitignore` file should contain:

```gitignore
browser.json
.env
.env.*
__pycache__/
*.py[cod]
.venv/
venv/
```

## 📦 Libraries Used

- **requests** — Retrieves webpage content through HTTP requests.
- **beautifulsoup4** — Parses HTML and extracts song information.
- **ytmusicapi** — Authenticates with YouTube Music, searches for songs, and manages playlists.

Install the required libraries using:

```bash
python -m pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
requests
beautifulsoup4
ytmusicapi
```

## 🔐 Authentication Setup

The project requires YouTube Music authentication through `ytmusicapi`.

To configure authentication:

1. Install `ytmusicapi`.
2. Open YouTube Music in Firefox and sign in to the desired Google account.
3. Open Developer Tools and navigate to the Network tab.
4. Find a successful `browse` request to `music.youtube.com`.
5. Copy the request headers.
6. Use the documented `ytmusicapi` browser authentication setup to generate `browser.json`.
7. Keep the file in the project directory and exclude it from Git.

Authentication may need to be refreshed if the session expires or becomes invalid.

Never publish the request headers or the generated authentication file.

## 💻 Code Structure

```text
Get Date from User
        ↓
Construct Billboard URL
        ↓
Send HTTP GET Request
        ↓
Parse HTML Using BeautifulSoup
        ↓
Extract Song Titles and Artists
        ↓
Authenticate with YouTube Music
        ↓
Check for Existing Playlist
        ↓
Create Private Playlist if Needed
        ↓
Search for Each Song
        ↓
Retrieve Matching Video ID
        ↓
Check for Existing Tracks
        ↓
Add Songs to Playlist
        ↓
Handle Individual Errors
        ↓
Display Playlist Summary
```

## 🧠 What I Learned

By completing this project, I learned how to:

- Retrieve webpage content using HTTP requests.
- Parse HTML documents using BeautifulSoup.
- Extract song titles from HTML elements.
- Work with lists and dictionaries.
- Construct URLs dynamically using f-strings.
- Authenticate with an external service using `ytmusicapi`.
- Understand the role of browser headers and cookies in authentication.
- Search for songs using an API library.
- Create and manage playlists programmatically.
- Work with playlist IDs and video IDs.
- Check for existing playlists to avoid duplicate creation.
- Use exception handling to skip individual failures.
- Avoid adding tracks that are already in a playlist.
- Organize a complete Python automation workflow.
- Protect authentication files using `.gitignore`.

## 🚀 Future Improvements

Possible improvements for this project include:

- Improve song matching by comparing artist names and track titles.
- Verify the HTML selectors used to extract artists.
- Add progress indicators while searching for 100 songs.
- Retry temporary network or API failures.
- Record songs that could not be found in a separate file.
- Generate a report of successful and unsuccessful additions.
- Improve duplicate detection for existing playlist tracks.
- Add unit tests for scraping, searching, and playlist creation.
- Validate the date format before sending the request.
- Add configurable timeouts and detailed logging.
- Handle expired authentication more clearly.

## 🔑 Key Takeaway

This project demonstrates how Python can combine web scraping and API interaction to automate the creation of a music playlist based on historical Billboard charts.

The main takeaway was learning how to extract information from a webpage, authenticate with an external service, search for matching songs, manage playlists, and handle errors in a practical automation project.

This project strengthened my understanding of BeautifulSoup, HTTP requests, authentication, API methods, list manipulation, and exception handling as part of my **100 Days of Code journey**.
