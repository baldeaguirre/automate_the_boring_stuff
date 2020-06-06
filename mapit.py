#! python3
import webbrowser
import sys
import pyperclip

# Check if command line arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com.mx/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com.mx/maps/place/' + address)