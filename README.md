# Scan-Copy-And-Sort-Documents
This repository contains a script that allows you to scan, copy, and sort documents using Google Lens. The script automates the process of extracting text from scanned images, copying it to a text file, and sorting the text based on specific criteria.

# Prerequisites
A smartphone with the Google Lens app installed.
A computer with Google Chrome browser and an active Google account.
# Instructions
Follow these steps to scan, copy, and sort your documents:

# Open Google Lens on your smartphone.
Sign in to your Google account in the Chrome browser on your computer. This step is crucial for pairing your phone and computer.
# Scan and Copy Text
Use your smartphone to scan images with text using Google Lens.
Copy the scanned text from your phone to your computer. You can paste the text into a text file or any desired text editor.
# Exclude Unwanted Documents
Ensure that you only scan similar documents together. Avoid scanning different types of documents (e.g., sign-in sheets and tests) simultaneously.
If you mistakenly scan different types of documents together, separate them and proceed with sorting them individually.
# Generate Sorted Text File
Open the 'EditMe.py' file in the repository using a text editor.
Customize the 'EditMe.py' file by adding the web elements of the desired copyable sections. This step allows you to fully automate the process.
Refer to the example provided in the 'EditMe.py' file, which includes a link to a McDonald's survey and a YouTube tutorial.
Save the changes made in the 'EditMe.py' file.
Quit and Generate Sorted Text File
# Run the script.
While the script is running, it will prompt you to press 'q' to quit.
Press 'q' to terminate the script and generate the text file.
The generated text file will contain the originally scanned text followed by the sorted and relevant text.
For example, if you scanned a sign-in sheet, it will extract only the names, excluding repeated elements like "Sign here please."
In the case of multiple sign-in sheets with different dates, it will also include the dates.
Congratulations! You have successfully scanned, copied, and sorted documents using Google Lens and the provided script.

# Customization
Feel free to customize the 'EditMe.py' file further to meet your specific requirements. Make sure to test the script with different documents and make adjustments as needed.

# License
This project is licensed under the MIT License.
