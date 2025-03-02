## README.md

# Duplex Print Assistant

## Description
A simple assistant to merge front and back sides of scanned documents.

## Features
- Select a scanner (HP Envy 6400 or other compatible scanners)
- Save front and back pages as PDFs
- Automatically merge pages in the correct order
- Easy-to-use graphical interface (Tkinter)

## Installation
1. Ensure Python 3.x is installed.
2. Clone the repository:
   ```sh
   git clone https://github.com/anmarchio/duplexmerger.git
   cd duplex-print-assistant
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
1. Start the program with:
   ```sh
   python duplex_scan_merge.py
   ```
2. Select or scan the front and back pages.
3. Click "Merge" to create a combined PDF file.

## Requirements
- A compatible scanner (e.g., HP Envy 6400)
- Windows or Linux (supports TWAIN or SANE for scanning)