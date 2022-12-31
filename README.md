# Text-From-Clipboard-Image

A simple Python script that allows you to extract text from an image copied in your clipboard.

### Python Library Requirements
- pillows
- pyperclip
- pytesseract
- keyboard

Make sure the tesseract application is installed within your device through https://github.com/UB-Mannheim/tesseract/wiki. 

### Usage
In certain situations where a piece of required text is found in an image that cannot be parsed or accessed, a user is able to utilise a shortcut to extract text from an image in their clipboard. Users may use programs such as Windows' "Snipping Tool" to take a snapshot of the desired area for extraction.

For example, finding a piece of desired text within an image, a user may use the Snipping Tool to copy the image to their clipboard. Then, using this program's shortcut, a user can convert the image content in their clipboard into the extracted text.

### Limitations
This script is limited by the performance of the Tesseract OCR engine, which may occasionally incorrectly extract a piece of text or character, such as detecting 'I' as '|'. 