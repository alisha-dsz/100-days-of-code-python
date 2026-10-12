# Day 43 - Spanish Vocabulary Project

## 📖 Overview

The Spanish Vocabulary Project is a simple HTML project created as part of the 100 Days of Code: The Complete Python Pro Bootcamp by Angela Yu.

The project is a basic webpage that helps users learn the names of different colors in Spanish. It displays Spanish color names along with images representing each color.

Although this project is part of a Python learning journey, Day 43 focuses on HTML and introduces the basics of CSS, including linking an external stylesheet, using classes and IDs, and working with images.

## 🎯 Objective

Create a simple Spanish vocabulary webpage that:

Displays a main heading.
Displays a subheading.
Shows the names of different colors in Spanish.
Displays images representing each color.
Uses HTML headings and image elements.
Links an external CSS stylesheet.
Uses classes and IDs to identify specific elements.
Understands how HTML and CSS work together.

## 🛠️ Concepts Practiced

HTML

HTML document structure

CSS stylesheet linking

HTML headings

`<link>`
`<h1>`
`<h2>`
`<img>`
`class`
`id`
`src`
`alt`

## 📚 HTML Elements Used

### `<!DOCTYPE html>`

Tells the browser that the document is written using modern HTML.

### `<html>`

The root element of the HTML document.

### `<head>`

Contains information about the webpage, including its title and linked stylesheet.

### `<meta charset="UTF-8">`

Specifies the character encoding of the webpage so that text can be displayed correctly.

### `<title>`

Sets the title that appears in the browser tab.

`<title>Spanish Vocabulary</title>`

### `<link>`

Connects an external CSS file to the HTML document.

`<link rel="stylesheet" href="./style.css" />`

### `<body>`

Contains all the visible content of the webpage.

### `<h1>`

Used for the main heading of the webpage.

`<h1>Colors</h1>`

### `<h2>`

Used for secondary headings and Spanish color names.

`<h2>Learn the colors in Spanish!</h2>`

### `<img>`

Displays an image on the webpage.

`<img class="color" src="./assets/images/red.png" alt="red" />`

The `src` attribute specifies the image path, while the `alt` attribute provides alternative text describing the image.

### `class`

Used to group HTML elements so that they can be styled using CSS.

`class="color-title"`

### `id`

Provides a unique identifier for an HTML element, allowing it to be targeted using CSS.

`id="red"`

## 🎨 Colors Included

The webpage contains five colors with their Spanish names:

**Rojo** — Red

**Azul** — Blue

**Anaranjado** — Orange

**Verde** — Green

**Amarillo** — Yellow

Each color is displayed with an image representing that color.

## 📂 Project Structure

Day-043-Spanish-Vocabulary-Project/
│
├── index.html # Main HTML webpage
├── style.css # CSS stylesheet
├── assets/
│ └── images/
│ ├── red.png
│ ├── blue.png
│ ├── orange.png
│ ├── green.png
│ └── yellow.png
│
└── README.md # Project documentation

## 💻 Code Structure

The webpage follows this basic structure:

HTML Document
↓
`<html>`
↓
`<head>`
↓
Page Title + CSS Link
↓
`<body>`
↓
Main Heading
↓
Subheading
↓
Spanish Color Name
↓
Corresponding Color Image
↓
Repeat for All Five Colors

## 🧠 What I Learned

By completing this project, I learned how to:

Create a basic HTML webpage.
Use headings to organize webpage content.
Display images using the `<img>` element.
Specify image paths using the `src` attribute.
Provide alternative text using the `alt` attribute.
Link an external CSS stylesheet to an HTML document.
Use classes to identify groups of HTML elements.
Use IDs to uniquely identify specific HTML elements.
Organize image files inside folders.
Understand how HTML and CSS work together to create webpages.
Build a simple educational webpage from scratch.

## 🚀 Future Improvements

Possible improvements for this project include:

Add more Spanish vocabulary words.
Add CSS styling to make the webpage more attractive.
Apply the actual colors to their respective Spanish headings.
Improve the layout using margins, padding, and alignment.
Add pronunciation guides for each Spanish word.
Add audio pronunciation for each color.
Add interactive flashcards.
Create a quiz to test Spanish color vocabulary.
Make the webpage responsive for mobile devices.
Add background colors and different fonts.

## 🔑 Key Takeaway

This project helped me practice HTML structure and learn how to connect an external CSS stylesheet to a webpage.

The main takeaway was understanding how HTML elements, classes, IDs, and images can be used to organize webpage content and prepare it for styling with CSS.

This project gave me more hands-on experience with web development as part of my 100 Days of Code journey.
