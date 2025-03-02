import os
import tkinter as tk
from tkinter import filedialog, messagebox

import fitz  # PyMuPDF for PDF processing


def merge_pdfs(front_path, back_path, output_path):
    """Merge front and back PDFs alternately."""
    try:
        doc1 = fitz.open(front_path)
        doc2 = fitz.open(back_path)
        doc2.select(range(len(doc2) - 1, -1, -1))  # Reverse the order of pages in doc2
        merged = fitz.open()

        max_pages = max(len(doc1), len(doc2))

        for i in range(max_pages):
            if i < len(doc1):
                merged.insert_pdf(doc1, from_page=i, to_page=i)
            if i < len(doc2):
                merged.insert_pdf(doc2, from_page=i, to_page=i)

        merged.save(output_path)
        merged.close()
        doc1.close()
        doc2.close()

        messagebox.showinfo("Erfolg", "PDFs wurden erfolgreich zusammengefügt!")
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Zusammenfügen: {str(e)}")


def select_directory(entry_field):
    """Open file dialog to select a PDF file."""
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    entry_field.delete(0, tk.END)
    entry_field.insert(0, file_path)


def start_merge():
    """Start merging process."""
    front_pdf = front_entry.get()
    back_pdf = back_entry.get()
    if not front_pdf or not back_pdf:
        messagebox.showerror("Fehler", "Bitte wählen Sie beide PDF-Dateien korrekt aus.")
        return

    output_path = os.path.join(os.path.dirname(front_pdf), "merged.pdf")
    merge_pdfs(front_pdf, back_pdf, output_path)


# GUI Setup
root = tk.Tk()
root.title("Duplex-Druck-Assistent")
root.geometry("500x300")

tk.Label(root, text="Zusammenfügen von Vorder- und Rückseite", font=("Arial", 12, "bold")).pack(pady=10)

# Front File Selection
front_frame = tk.Frame(root)
front_frame.pack(pady=5)
tk.Label(front_frame, text="Vorderseite (front.pdf):").pack(side=tk.LEFT)
front_entry = tk.Entry(front_frame, width=40)
front_entry.pack(side=tk.LEFT)
tk.Button(front_frame, text="Auswählen ...", command=lambda: select_directory(front_entry)).pack(side=tk.LEFT)

# Back File Selection
back_frame = tk.Frame(root)
back_frame.pack(pady=5)
tk.Label(back_frame, text="Rückseite (back.pdf):").pack(side=tk.LEFT)
back_entry = tk.Entry(back_frame, width=40)
back_entry.pack(side=tk.LEFT)
tk.Button(back_frame, text="Auswählen ...", command=lambda: select_directory(back_entry)).pack(side=tk.LEFT)

# Merge Button
tk.Button(root, text="Zusammenfügen", command=start_merge, font=("Arial", 12, "bold"), bg="green", fg="white").pack(
    pady=20)

root.mainloop()
