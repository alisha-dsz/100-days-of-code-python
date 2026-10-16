# Day 45 - Top 100 Movies Web Scraping Project

## 📖 Overview

The Top 100 Movies Web Scraping Project is a Python project created as part of the 100 Days of Code: The Complete Python Pro Bootcamp by Angela Yu.

The project extracts movie titles from a website using web scraping techniques and saves them into a text file in chronological order, starting with the lowest-ranked movie and ending with the highest-ranked movie.

The project uses the `requests` library to retrieve webpage content and `BeautifulSoup` from `bs4` to parse the HTML document and extract movie titles.

This project focuses on web scraping, HTML parsing, list manipulation, file handling, and working with external website data using Python.

## 🎯 Objective

Create a Python program that:

- Sends an HTTP request to retrieve webpage content.
- Uses the `requests` library to access a movie website.
- Parses HTML content using BeautifulSoup.
- Finds all HTML elements containing movie titles.
- Extracts movie titles using the `getText()` method.
- Reverses the extracted list to arrange movies in chronological order.
- Creates a text file named `movie.txt`.
- Writes each movie title on a separate line.
- Uses UTF-8 encoding to support a wider range of characters.
- Automates the process of collecting and storing movie data.

## 🛠️ Concepts Practiced

### Python

- Variables and constants
- Lists and list comprehensions
- List slicing
- Loops and iteration
- File handling
- The `with open()` statement
- String formatting using f-strings
- UTF-8 file encoding
- Importing external libraries

### Web Scraping

- HTTP requests
- Retrieving webpage source code
- HTML parsing
- Finding HTML elements by tag name and class
- Extracting text from HTML elements
- Working with archived webpages

### Libraries Used

- `requests`
- `BeautifulSoup` from `bs4`

## 📚 Python Concepts Used

### 1. Importing Libraries

```python
import requests
from bs4 import BeautifulSoup
```

The `requests` library sends HTTP requests and retrieves webpage content.

`BeautifulSoup` is imported from the `bs4` library to parse HTML and extract the required information.

### 2. Defining a URL

```python
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
```

The `URL` variable stores the address of the archived Empire magazine webpage containing the movie ranking.

The uppercase variable name follows the Python convention for constants.

### 3. Sending an HTTP Request

```python
response = requests.get(URL)
movie_website = response.text
```

`requests.get(URL)` sends an HTTP GET request to retrieve the webpage.

The `response` object contains information about the server's response.

The `.text` attribute returns the response body as a string, which contains the HTML source code.

### 4. Parsing HTML with BeautifulSoup

```python
soup = BeautifulSoup(movie_website, "html.parser")
```

`BeautifulSoup()` converts the HTML source code into a parsed structure that Python can search and navigate.

- `movie_website` is the HTML content.
- `"html.parser"` specifies the built-in HTML parser.

The resulting `soup` object makes it easier to find specific HTML elements.

### 5. Finding and Extracting Movie Titles

```python
titles = [
    title.getText()
    for title in soup.find_all(name="h3", class_="title")
]
```

The `find_all()` method searches for all HTML `<h3>` elements whose class is `title`.

The `getText()` method extracts the text content from each matching HTML element.

The list comprehension collects the extracted movie titles into a Python list.

For example, the resulting list might look like this:

```python
titles = [
    "Movie Title A",
    "Movie Title B",
    "Movie Title C"
]
```

These example titles illustrate the structure of the list, not the actual titles returned by the website.

### 6. Reversing the List

```python
reversed_title_list = titles[::-1]
```

The slicing expression `[::-1]` creates a reversed copy of the original list.

The original webpage lists movies in descending ranking order, so reversing the list allows the output to be written in ascending order, from the lowest-ranked movie to the highest-ranked movie.

This technique uses Python's extended slicing syntax.

### 7. Writing Movie Titles to a Text File

```python
with open("movie.txt", "w", encoding="utf-8") as file:
    for movie in reversed_title_list:
        file.write(f"{movie}\n")
```

The `open()` function opens a file for writing.

- `"movie.txt"` specifies the output filename.
- `"w"` opens the file in write mode, creating it if it does not exist and replacing its existing contents if it does.
- `encoding="utf-8"` supports a broad range of characters.
- `with` automatically closes the file when the block finishes.
- The `for` loop processes each movie title.
- `file.write()` writes each title to the file.
- `\n` adds a newline so each movie appears on a separate line.

The final result is a text file containing the extracted movie titles in reversed order.

## 🔄 How the Project Works

The program follows this workflow:

1. Store the webpage URL.
2. Send an HTTP GET request using `requests`.
3. Retrieve the HTML response.
4. Parse the HTML using BeautifulSoup.
5. Find all `<h3>` elements with the class `title`.
6. Extract the text from each matching element.
7. Reverse the list of movie titles.
8. Open `movie.txt` in write mode.
9. Write each title on a separate line.
10. Close the file automatically.

## 📂 Project Structure

```text
Day-045-Top-100-Movies/
│
├── main.py          # Python script for web scraping
├── movie.txt        # Output file containing movie titles
└── README.md        # Project documentation
```

The output file `movie.txt` is created when the Python program runs successfully. It does not need to exist beforehand.

## 💻 Code Structure

```text
Import Libraries
       ↓
Define Website URL
       ↓
Send HTTP GET Request
       ↓
Retrieve HTML Content
       ↓
Parse HTML Using BeautifulSoup
       ↓
Find Movie Title Elements
       ↓
Extract Movie Titles
       ↓
Reverse the List
       ↓
Open movie.txt
       ↓
Write Each Movie on a New Line
       ↓
Close File Automatically
```

## 🧠 What I Learned

By completing this project, I learned how to:

- Retrieve webpage content using the `requests` library.
- Understand the role of HTTP GET requests.
- Parse HTML documents using BeautifulSoup.
- Search HTML elements by tag name and class.
- Extract text from HTML elements.
- Use list comprehensions to write concise Python code.
- Reverse a list using extended slicing.
- Write data to a text file using Python.
- Use the `with open()` statement for safe file handling.
- Specify UTF-8 encoding when working with text files.
- Automate the extraction and storage of information from a webpage.
- Combine multiple Python concepts and external libraries in a practical project.

## 🚀 Future Improvements

Possible improvements for this project include:

- Add exception handling for connection errors and timeouts.
- Check the HTTP response status before parsing the webpage.
- Use `response.raise_for_status()` to detect unsuccessful HTTP responses.
- Add a request timeout to prevent the program from waiting indefinitely.
- Remove duplicate movie titles if any are present.
- Save movie rankings alongside movie titles.
- Export the results to a CSV file.
- Extract additional details such as release years and movie descriptions.
- Accept a custom URL as user input.
- Add logging to track the scraping process.
- Create a reusable function for extracting movie titles.
- Add automated tests to verify the extracted results.
- Use a current, accessible movie-ranking page if the archived webpage becomes unavailable.

## 🔑 Key Takeaway

This project helped me understand how Python can retrieve, parse, and organize information from a webpage using web scraping techniques.

The main takeaway was learning how to combine `requests`, BeautifulSoup, list comprehensions, list slicing, and file handling to automate the extraction of movie titles and save them in a structured text file.

This project strengthened my understanding of working with external data and applying Python concepts to a practical automation task as part of my 100 Days of Code journey.
