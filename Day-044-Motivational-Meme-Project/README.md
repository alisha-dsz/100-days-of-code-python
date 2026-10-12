# Day 44 - Motivational Meme Website

📖 Overview

The Motivational Meme Website is a simple webpage created as part of the 100 Days of Code: The Complete Python Pro Bootcamp by Angela Yu.

The project displays a motivational poster featuring an image of a man helping another man climb a mountain. It includes the word "Rise" as the main heading and an inspirational quote about helping others overcome their struggles.

The webpage is built using HTML and CSS. Day 44 focuses on CSS styling, including background colors, text alignment, margins, image borders, text transformation, font styling, and the use of Google Fonts to improve the appearance of a webpage.

🎯 Objective

Create a simple motivational meme webpage that:

- Displays a motivational image.
- Shows a main heading with the word "Rise".
- Displays an inspirational quote below the image.
- Uses HTML elements to structure the webpage content.
- Links an external CSS stylesheet.
- Applies background colors, text colors, borders, and alignment using CSS.
- Uses margins and width properties to position the poster.
- Imports and applies a Google Font to style the heading.
- Understands how HTML and CSS work together to create a visually appealing webpage.

🛠️ Concepts Practiced

**HTML**

HTML document structure

HTML headings and paragraphs

Image elements and attributes

Linking external stylesheets

Linking Google Fonts

Classes and attributes

**CSS**

Background colors

Text alignment

Margins and width

Image styling

Borders and border colors

Text transformation

Font families

Text colors

External font integration

📚 HTML Elements Used

**<!doctype html>**

Tells the browser that the document uses modern HTML.

**<html lang="en">**

The root element of the HTML document. The `lang` attribute specifies that the webpage content is in English.

**<head>**

Contains metadata, the webpage title, and links to external resources such as stylesheets and fonts.

**<meta charset="UTF-8" />**

Specifies the character encoding so that text and special characters can be displayed correctly.

**<meta name="viewport" content="width=device-width, initial-scale=1.0" />**

Helps the webpage adapt to different screen sizes, including mobile devices.

**<title>**

Sets the title displayed in the browser tab.

`<title>Motivational Meme Website</title>`

**<link>**

Connects external resources to the HTML document, such as the CSS stylesheet and Google Fonts.

`<link rel="stylesheet" href="./style.css" />`

The `rel` attribute specifies the relationship between the HTML document and the linked resource, while `href` specifies its location.

**<div>**

Creates a container that groups related HTML elements together.

`<div class="poster">`

The `poster` class allows the entire motivational poster section to be styled using CSS.

**<img>**

Displays an image on the webpage.

`<img class="poster-img" src="./assets/images/motivation.jpg" alt="A man helping another man climb a mountain" />`

The `src` attribute specifies the image path, while the `alt` attribute provides alternative text describing the image.

**<h1>**

Defines the main heading of the webpage.

`<h1>r i s e</h1>`

The heading displays the word "Rise" with spaces between the letters to create a visual effect. CSS is used to transform the text to uppercase.

**<p>**

Defines a paragraph of text.

`<p>A helping hand can turn someone’s struggle into their greatest strength.</p>`

The paragraph displays the motivational quote below the heading.

🎨 CSS Properties Practiced

**background-color**

Sets the background color of an element.

`background-color: black;`

Used to give the webpage a black background that contrasts with the golden and orange text.

**width**

Controls the width of an element.

`width: 50%;`

Used to set the poster container's width to 50% of its containing block.

**margin-left**

Sets the left margin of an element.

`margin-left: 25%;`

Used to position the poster container horizontally.

**margin-top**

Sets the top margin of an element.

`margin-top: 100px;`

Adds space above the poster container.

**text-align**

Controls the horizontal alignment of text.

`text-align: center;`

Centers the poster's text content.

**color**

Sets the text color of an element.

`color: #ffc349;`

Applies a golden color to the poster text.

**border**

Adds a border around an element.

`border: 5px solid #ffc349;`

Adds a solid golden border around the motivational image.

**text-transform**

Controls the capitalization of text.

`text-transform: uppercase;`

Transforms the heading text to uppercase.

**font-family**

Specifies the font used for text.

`font-family: "Libre Baskerville", serif;`

Uses the Libre Baskerville font imported from Google Fonts, with a serif fallback.

**Google Fonts**

The project imports the Libre Baskerville font using a Google Fonts URL. This provides a more elegant and readable appearance for the motivational heading.

📂 Project Structure

Day-044-Motivational-Meme-Website/  
│  
├── index.html # Main HTML webpage  
├── style.css # CSS stylesheet  
├── assets/  
│ └── images/  
│ └── motivation.jpg # Motivational poster image  
└── README.md # Project documentation

💻 Code Structure

The webpage follows this basic structure:

HTML Document  
↓

<html>  
↓  
<head>  
↓  
Page Title + CSS Link + Google Fonts  
↓  
<body>  
↓  
Poster Container  
↓  
Motivational Image  
↓  
Main Heading — "Rise"  
↓  
Inspirational Quote

The CSS stylesheet controls the poster's position, image dimensions, border, background color, text alignment, text colors, and font styling.

🧠 What I Learned

By completing this project, I learned how to:

- Create a basic motivational webpage using HTML.
- Organize related elements inside a `<div>` container.
- Display images using the `<img>` element.
- Use the `src` and `alt` attributes appropriately.
- Create headings and paragraphs using HTML.
- Link an external CSS stylesheet to an HTML document.
- Change the background color of a webpage using CSS.
- Apply text colors using hexadecimal color codes.
- Control element width using percentage values.
- Position elements using margins.
- Center text using the `text-align` property.
- Add borders around images using the `border` property.
- Transform text into uppercase using `text-transform`.
- Import and use Google Fonts in a webpage.
- Understand how CSS properties affect the appearance and layout of HTML elements.
- Combine HTML structure and CSS styling to create a motivational poster.

🚀 Future Improvements

Possible improvements for this project include:

- Make the poster responsive for mobile devices and tablets.
- Add padding and spacing to improve the overall layout.
- Use CSS Flexbox to center the poster horizontally and vertically.
- Add more motivational posters with different quotes.
- Experiment with different Google Fonts and typography styles.
- Add subtle hover effects and CSS animations.
- Improve accessibility by maintaining good color contrast.
- Add a button to generate or display a random motivational quote.
- Create a collection of motivational memes with different themes.
- Improve the image sizing and layout for different screen resolutions.

🔑 Key Takeaway

This project helped me practice CSS styling and understand how basic CSS properties can transform a simple HTML document into a visually appealing webpage.

The main takeaway was learning how to combine HTML elements with CSS properties such as background colors, margins, width, borders, text alignment, text transformation, and font families to design a motivational poster.

I also gained hands-on experience integrating Google Fonts into a webpage and using visual design elements to make content more engaging.

This project strengthened my understanding of HTML and CSS as part of my 100 Days of Code journey.
