from PIL import ImageGrab, Image
import pyperclip
import pytesseract
import keyboard

# Make sure to provide the path to the tesseract executable.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# Function to be called to extract text from a clipboard's image content.
def convert_clipboard_to_text():

    # Errors may arise when the clipboard's content is not an image. 
    try:
        img = ImageGrab.grabclipboard()
        pyperclip.copy(pytesseract.image_to_string(img))
    except:
        print("Error: Clipboard content is not an image.")



if __name__ == "__main__":
    keyboard.add_hotkey("shift+windows+d", convert_clipboard_to_text)
    keyboard.wait()