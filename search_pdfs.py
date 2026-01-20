import fitz  # PyMuPDF
import os

SEARCH_TEXT = "apcpImebw" # change to your search text
PDF_FOLDER = "pdfs"  # change to your folder path


def search_in_pdfs(folder_path, search_text):
    found = False

    for file_name in os.listdir(folder_path):
        if not file_name.lower().endswith(".pdf"):
            continue

        file_path = os.path.join(folder_path, file_name)
        print(f"🔍 Scanning: {file_name}")

        try:
            doc = fitz.open(file_path)

            for page_number in range(len(doc)):
                page = doc[page_number]
                text = page.get_text()

                if search_text in text:
                    print(
                        f"✅ FOUND in {file_name} | Page {page_number + 1}"
                    )
                    found = True

            doc.close()

        except Exception as e:
            print(f"❌ Error reading {file_name}: {e}")

    if not found:
        print("\n🚫 Text not found in any PDF.")


if __name__ == "__main__":
    search_in_pdfs(PDF_FOLDER, SEARCH_TEXT)
