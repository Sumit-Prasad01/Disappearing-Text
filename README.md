# Typing Word Counter App
## This is a simple desktop application built with PyQt5 that tracks and displays the number of words typed in a text field. It also includes a timer that clears the text and resets the word count after 5 seconds of inactivity.

### Features
- Word Count Display: It counts the number of words typed in real-time and updates the displayed count.
- Automatic Text Clearing: If no keypress occurs within 5 seconds, the text is automatically cleared, and the word count is reset.
- Custom Styling: The app uses custom colors, fonts, and padding to make the user interface visually appealing.
### Installation
- Before running the app, make sure you have Python 3.x and PyQt5 installed.
### How It Works
- When you start typing in the text box, the app dynamically counts and displays the number of words typed.
- If you stop typing for more than 5 seconds, the text area is cleared, and the word count is reset to zero.
### Word Counting
- The app defines a word as any sequence of characters separated by spaces. It ignores spaces and punctuation to only count actual words.
### Timer
- A QTimer is used to track the time between keypresses. When the timer exceeds 5 seconds without activity, the text is cleared, and the word count label is reset.
