# Scan-Copy-And-Sort-Documents
This repository scans and uploads ML sorted documents from Google Lens to you.
1.  First open Gogole Lens and connect to your Google account in Chrome. Otherwise, it will not pair with your computer.
    Use your phone and install the Google app. Then scan images w/ text and copy to your computer.
2.  Next, the copied text will be pasted into a text file. Scan all similar documents, i.e. do not scan in sign-in sheets 
    and tests at the same time.
4.  Press 'q' to quit. This will generate the text file with all originally scanned text, then the variant (hopefully 
    useful) text. I.e. a sign in sheet will typically contain today's single date and others' names. This will return only the name(s).
    Will return the date if multiple sign in sheets have different dates. Will not return things like "Sign here please" if repeated across
    all documents.
5.  You can edit the attached 'EditMe.py' file to contain the web elements of your desired copyable sections. A link to a McDonald survey and
    YouTube tutorial will be provided as an example on how to do this. You may want to do this to fully automate the process. 
