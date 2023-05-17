import spacy
import re

nlp = spacy.load("en_core_web_md")

clipboard_contents = [
    'This is a bunch of text stuff.\r\n\r\nThis is more text.\r\n\r\nHello, this is more text!\r\n\r\n123456789\r\n\r\nPut your handwriting here: I EAT BEANS!!',
    'This is a bunch of text stuff.\r\n\r\nThis is more text.\r\n\r\nHello, this is more text!\r\n\r\n123456789\r\n\r\nPut your handwriting here: I love beans eating\r\n']
all_sentences = []
doc = []
doc0 = []

# def matching_first_phrase(clipboard_contents, index):
# Define a regular expression to match the first phrase

pattern = r'^\w+ is'

test_string = 'This is a test string.'

match = re.match(pattern, test_string)

if match:
    print('Match found!')
else:
    print('Match not found.')


def first_phrase(texts):
    regex = re.compile(r'^[A-Za-z]+(?:\s+[A-Za-z]+)*')

    for text in texts:
        # Find the first match for the regex in the string
        match = regex.search(text)
        if match:
            # Extract the matched text
            first_phrase = match.group()
            print(first_phrase)
            return first_phrase
    print('Did not find a first-phrase match, scan again?')


first_phrase(clipboard_contents)


def get_doc0():
    print(0)
    sentences0 = clipboard_contents[0].replace('\r', '').split('\n')

    # Create a new doc for each sentence and add it to the doc array
    doc_array0 = [nlp(sentence) for sentence in sentences0]
    # Print the processed text
    for d0 in doc_array0:
        print(d0.text)
    return doc_array0


# Start on 2nd iteration

doc_array0 = get_doc0()

for i in range(1, len(clipboard_contents)):
    print(i)
    print('Hello World!')
    # matching_first_phrase(clipboard_contents, i)
    # Remove '\r' characters and split the string into sentences
    sentences = clipboard_contents[i].replace('\r', '').split('\n')

    # Create a new doc for each sentence and add it to the doc list
    doc_array = [nlp(sentence) for sentence in sentences]

    # Print the processed text
    for index, d in enumerate(doc_array):
        print(d.text)
        try:
            if d.similarity(doc_array0[index]) < 0.95:
                print('Eureka!', doc_array0[index])
                print('Eureka!', d.text)
        except:
            print('Out of index range, ensure you are scanning correctly!')
