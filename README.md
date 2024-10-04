# Text Convertor Application

## Overview

The **Text Convertor** is a simple web application built using **Django** that allows users to modify and transform text in various ways. Users can perform multiple operations on the input text, such as removing punctuation, converting text to uppercase, removing new lines, removing extra spaces, and counting the number of characters.

## Features

The Text Convertor offers the following features:

- **Remove Punctuation**: Remove all special characters and punctuation from the input text.
- **Convert to Uppercase**: Convert all the characters in the input text to uppercase.
- **Remove New Lines**: Remove all newline (`\n`) and carriage return (`\r`) characters.
- **Remove Extra Spaces**: Remove extra spaces between words, leaving only a single space.
- **Count Characters**: Count the number of characters in the input text (including spaces).


### Prerequisites

Before running the application, ensure that you have the following installed:

- **Python** (preferably 3.6+)
- **Django** (preferably 3.x+)


## Usage

1. **Home Page**: On the home page, enter the text you want to transform in the provided text area.
2. **Select Operations**: Select the operations you want to apply to the text:
    - **Remove Punctuation**: Check this option to remove punctuation.
    - **Convert to Uppercase**: Check this option to convert the text to uppercase.
    - **Remove New Lines**: Check this option to remove newlines.
    - **Remove Extra Spaces**: Check this option to remove extra spaces between words.
    - **Count Characters**: Check this option to count the number of characters in the text.
3. **Submit**: Click the "Submit" button to see the result.
4. **Result Page**: The transformed text will be displayed, and any applicable transformations will be highlighted.

## File Structure

```plaintext
text-convertor/
│
├── manage.py
├── textconvertor/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   ├── index.html
│   ├── success.html
│   ├── about.html
│   └── contact.html
│
└── static/
    └── css/
        └── styles.css
