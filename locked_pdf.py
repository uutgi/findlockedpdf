import os
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2


class LockedPDFsFinder:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Locked PDFs Finder v. 1.0')

        self.title_label = tk.Label(self.root, text="Locked PDFs Finder v. 1.0", fg="orange", font=("Helvetica", 16))
        self.title_label.pack(pady=10)

        self.folder_file_button = tk.Checkbutton(self.root, text="Folder", command=self.update_button_text, fg="white")
        self.folder_file_button.pack(pady=10)

        self.select_button = tk.Button(self.root, text="Select File", command=self.select_file_or_folder)
        self.select_button.pack()

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=10)

        self.root.mainloop()

    def update_button_text(self):
        if self.folder_file_button.cget('text') == 'Folder':
            self.folder_file_button.config(text='File')
            self.select_button.config(text='Select Folder')
        else:
            self.folder_file_button.config(text='Folder')
            self.select_button.config(text='Select File')

    def select_file_or_folder(self):
        if self.folder_file_button.cget('text') == 'Folder':
            file_path = filedialog.askopenfilename(title="Select file", filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
            if file_path:
                self.process_file(file_path)
        else:
            folder_path = filedialog.askdirectory(title="Select folder")
            if folder_path:
                self.process_folder(folder_path)

    def process_file(self, file_path):
        locked_pdfs = self.find_locked_pdfs_in_file(file_path)
        self.show_result(locked_pdfs)

    def process_folder(self, folder_path):
        locked_pdfs = self.find_locked_pdfs_in_folder(folder_path)
        self.show_result(locked_pdfs)

    def find_locked_pdfs_in_file(self, file_path):
        if file_path.endswith(".pdf"):
            with open(file_path, "rb") as input_file:
                reader = PyPDF2.PdfReader(input_file)
                if reader.is_encrypted:
                    return [file_path]
        return []

    def find_locked_pdfs_in_folder(self, folder_path):
        locked_pdfs = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".pdf"):
                    input_path = os.path.join(root, file)
                    with open(input_path, "rb") as input_file:
                        reader = PyPDF2.PdfReader(input_file)
                        if reader.is_encrypted:
                            locked_pdfs.append(input_path)
        return locked_pdfs

    def show_result(self, locked_pdfs):
        if locked_pdfs:
            messagebox.showinfo("Result", "\n".join(locked_pdfs))
        else:
            messagebox.showinfo("Result", "No locked PDFs found.")


if __name__ == "__main__":
    app = LockedPDFsFinder()
