# Day 42 - Birthday Invite Project

## 📖 Overview

The Birthday Invite Project is a simple HTML project created as part of the 100 Days of Code: The Complete Python Pro Bootcamp by Angela Yu.

The project is a basic birthday invitation webpage that displays the birthday date, a birthday cake image, a list of items to bring, and a Google Maps link to the location.

Although this project is part of a Python learning journey, Day 42 focuses on HTML elements and web development concepts, including images, lists, hyperlinks, page structure, and attributes.

## 🎯 Objective

Create a simple birthday invitation webpage that:

Displays a main heading announcing the birthday.

Displays the birthday date.

Adds a birthday cake image to the webpage.

Shows a list of items guests should bring.

Provides a Google Maps link for the location.

Uses HTML elements to organize webpage content.

Understands how to add images, lists, and hyperlinks to an HTML document.

## 🛠️ Concepts Practiced

HTML

HTML document structure

`<!doctype html>`

`<html>`

`<head>`

`<meta>`

`<title>`

`<body>`

`<center>`

`<h1>`

`<h2>`

`<h3>`

`<br />`

`<img>`

`<ul>`

`<li>`

`<a>`

HTML attributes: `src`, `alt`, `href`, `lang`, `charset`, and `name`

Image embedding using a URL

Creating unordered lists

Adding hyperlinks

Using comments in HTML

## 📚 HTML Elements Used

### `<!doctype html>`

Tells the browser that the document uses modern HTML.

```html
<!doctype html>
```

### `<html>`

The root element of the HTML document. The `lang` attribute specifies the language of the webpage.

```html
<html lang="en"></html>
```

### `<head>`

Contains information about the webpage, such as its title and metadata, that is not directly displayed in the main page content.

### `<meta>`

Provides metadata about the webpage.

```html
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
```

The `charset` attribute sets the character encoding, while the viewport setting helps the webpage display properly on different screen sizes.

### `<title>`

Sets the title displayed in the browser tab.

```html
<title>Birthday Invite Project</title>
```

### `<body>`

Contains all the visible content of the webpage.

### `<center>`

Centers the content inside it. This element is obsolete in modern HTML; CSS is the recommended way to center content.

```html
<center>
  <h1>It's My Birthday!</h1>
</center>
```

### `<h1>`

Used for the main heading of the webpage.

```html
<h1>It's My Birthday!</h1>
```

### `<h2>`

Used for a secondary heading, displaying the birthday date.

```html
<h2>On the 6th of September</h2>
```

### `<br />`

Adds a line break to the webpage.

```html
<br />
```

### `<img>`

Embeds an image into the webpage.

```html
<img
  src="https://raw.githubusercontent.com/appbrewery/webdev/main/birthday-cake3.4.jpeg"
  alt="Birthday cake with candles"
/>
```

- `src` specifies the image URL.
- `alt` provides alternative text describing the image if it cannot be displayed and helps accessibility.

### `<h3>`

Used for smaller headings, such as the list of items to bring and the location section.

```html
<h3>What to bring:</h3>
```

### `<ul>`

Creates an unordered list, usually displayed with bullet points.

```html
<ul>
  <li>Balloons</li>
  <li>Cake</li>
  <li>An appetite</li>
</ul>
```

### `<li>`

Defines an individual item inside a list.

```html
<li>Balloons (I love balloons)</li>
```

### `<a>`

Creates a hyperlink that allows users to navigate to another webpage or location.

```html
<a
  href="https://www.google.com/maps/@35.7040744,139.5577317,3a,75y,289.6h,87.01t,0.72r/data=!3m6!1e1!3m4!1sgT28ssf0BB2LxZ63JNcL1w!2e0!7i13312!8i6656"
>
  Google Map Link
</a>
```

The `href` attribute specifies the destination of the link. In this project, it points to Google Maps.

### HTML Comments

Comments are used to explain the code and are not displayed as visible webpage content.

```html
<!-- Example Google Maps Link -->
```

## 🎂 Birthday Invitation Includes

The webpage contains the following sections:

**Birthday Announcement**

Displays the main heading: "It's My Birthday!"

**Birthday Date**

Shows the birthday date as the 6th of September.

**Birthday Cake Image**

Displays a birthday cake image using an external image URL.

**What to Bring**

An unordered list containing:

- Balloons
- Cake
- An appetite

**Location**

Provides a Google Maps hyperlink so guests can view the location.

## 📂 Project Structure

```text
Day-042-Birthday-Invite-Project/
│
├── index.html       # Main HTML webpage
└── README.md        # Project documentation
```

## 💻 Code Structure

The webpage follows this basic structure:

```text
HTML Document
      ↓
    <html>
      ↓
    <head>
      ↓
  Page Title + Metadata
      ↓
    <body>
      ↓
   Centered Content
      ↓
 Birthday Announcement
      ↓
    Birthday Date
      ↓
  Birthday Cake Image
      ↓
    What to Bring
      ↓
    Unordered List
      ↓
    Google Maps Link
```

## 🧠 What I Learned

By completing this project, I learned how to:

Create a basic birthday invitation webpage using HTML.

Understand the structure of an HTML document.

Use headings to organize webpage content.

Embed images using the `<img>` element.

Understand the purpose of the `src` and `alt` attributes.

Create unordered lists using `<ul>` and `<li>`.

Add hyperlinks using the `<a>` element and the `href` attribute.

Link to an external website such as Google Maps.

Use HTML comments to explain sections of code.

Add metadata to an HTML document.

Use the `<br />` element to insert a line break.

Understand how HTML elements work together to create a complete webpage.

## 🚀 Future Improvements

Possible improvements for this project include:

Add CSS to improve the overall design.

Use background colors and attractive fonts.

Add a custom birthday invitation theme.

Include the birthday venue's actual address.

Replace the sample Google Maps link with the real venue location.

Add the date, time, and RSVP details.

Make the webpage responsive for mobile devices.

Use CSS Flexbox or Grid to arrange the content.

Replace the obsolete `<center>` element with modern CSS styling.

Add animations and decorative birthday elements.

## 🔑 Key Takeaway

This project helped me understand how HTML elements can be combined to create a complete and meaningful webpage.

The main takeaway was learning how to display images, organize content using lists, and connect a webpage to an external location using hyperlinks.

This project also strengthened my understanding of HTML attributes and webpage structure as part of my 100 Days of Code journey.
