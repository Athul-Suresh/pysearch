# PySearch

A Python tool for searching text within PDF files.

## Features

- Search for keywords or phrases in PDF documents
- Supports multiple PDF files in a directory
- Fast and efficient text extraction and searching

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/pysearch.git
   cd pysearch
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   .\.venv\Scripts\activate  # On Windows
   ```

3. Install dependencies:
   ```
   pip install PyMuPDF
   ```

## Usage

1. Place your PDF files in the `pdfs/` directory.

2. Edit `search_pdfs.py` and change the `SEARCH_TEXT` variable to your desired search term.

3. Run the search script:
   ```
   python search_pdfs.py
   ```

The script will scan all PDF files in the `pdfs` folder and print results for pages containing the search text.

## Requirements

- Python 3.7+
- PyMuPDF

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.