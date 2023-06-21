# findlockedpdf
"Locked PDFs Finder" application that allows users to select a file or folder and identify any locked (encrypted) PDF files within it.

# Locked PDFs Finder

The "Locked PDFs Finder" is a Python application that helps users identify locked (encrypted) PDF files within a selected file or folder. It utilizes the PyPDF2 library to read PDF files and determine if they are encrypted.

## Features

- Allows users to choose between selecting a single file or a folder.
- For file selection, it checks if the file is a PDF and if it is encrypted.
- For folder selection, it recursively searches for PDF files within the folder and its subdirectories, identifying any encrypted files.
- Displays the list of locked PDF files found or a message indicating that no locked PDFs were found.

## Prerequisites

- Python 3.x installed on your system.
- Required Python packages: tkinter, PyPDF2.

## Getting Started

1. Clone the repository or download the source code files.
2. Install the required Python packages:
   ```
   pip install tkinter PyPDF2
   ```
3. Run the application:
   ```
   python locked_pdfs_finder.py
   ```
4. The application window will appear, allowing you to select a file or folder.

## Usage

1. Selecting a File:
   - Click the "Select File" button.
   - Choose a PDF file using the file dialog window.
   - If the selected file is locked (encrypted), a message box will display the path to the locked PDF file. Otherwise, a message will indicate that no locked PDFs were found.

2. Selecting a Folder:
   - Click the "Folder" check button to switch to "File" mode.
   - Click the "Select Folder" button.
   - Choose a folder using the folder dialog window.
   - The application will search for PDF files within the selected folder and its subdirectories.
   - If any locked PDF files are found, a message box will display the paths to the locked PDF files. Otherwise, a message will indicate that no locked PDFs were found.

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## Contact

If you have any questions or need further assistance, feel free to contact the project maintainer at [email protected]

---

Feel free to customize the README file according to your specific project requirements.
