import pyperclip
import time
import keyboard
import spacy
import numpy as np

nlp = spacy.load("en_core_web_md")
def clear_clipboard():
    # Clear their clip board
    pyperclip.copy('')


def paste_from_clipboard():
    # Get the current clipboard content
    clipboard_content = pyperclip.paste()

    # Press Ctrl+V to paste the clipboard content
    keyboard.press_and_release('ctrl+v')

    # Wait for a short amount of time to allow the paste to complete
    time.sleep(0.1)

    # Return the original clipboard content
    pyperclip.copy(clipboard_content)


def copy_to_clipboard():
    # Press Ctrl+C to copy the selected text to the clipboard
    keyboard.press_and_release('ctrl+c')

    # Wait for a short amount of time to allow the copy to complete
    time.sleep(0.1)

    # Paste the copied text
    paste_from_clipboard()


def get_doc0(clipboard_contents):
    print(0)
    sentences0 = clipboard_contents[0].replace('\r', '').split('\n')

    # Create a new doc for each sentence and add it to the doc array
    doc_array0 = [nlp(sentence) for sentence in sentences0]
    # Print the processed text
    for d0 in doc_array0:
        print(d0.text)
    return doc_array0


def separate_list(clipboard_contents):
    # Start on 2nd iteration
    doc_array0 = get_doc0(clipboard_contents)

    for i in range(1, len(clipboard_contents)):
        print(i)
        print('Hello World!')
        # Remove '\r' characters and split the string into sentences
        sentences = clipboard_contents[i].replace('\r', '').split('\n')

        # Create a new doc for each sentence and add it to the doc list
        doc_array = [nlp(sentence) for sentence in sentences]

        # Print the processed text
        for index, d in enumerate(doc_array):
            print(d.text)
            try:
                if d.similarity(doc_array0[index]) < 0.95:
                    print('Found:', doc_array0[index])
                    print('Found:', d.text)
            except:
                print('Out of index range, ensure you are scanning correctly!')


# Listen for changes to the clipboard
clear_clipboard()
all_sentences = []
doc = []
doc0 = []
previous_clipboard_content = pyperclip.paste()
all_clipboard_content = [previous_clipboard_content]
previous_index = 0
print('Scan documents with Google Lens. Pair your computer by logging into your gmail account.')
while True:
    current_clipboard_content = pyperclip.paste()
    if current_clipboard_content != previous_clipboard_content:
        paste_from_clipboard()
        previous_clipboard_content = current_clipboard_content
        all_clipboard_content.append(current_clipboard_content)

    # Check if the user has pressed the 'q' key to exit the program
    if keyboard.is_pressed('q'):
        print('Compiling program...')
        if all_clipboard_content == 1:
            print('You must scan a minimum of two documents!')
        separate_list(all_clipboard_content)
        break

    time.sleep(0.1)
