import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path_or_file) -> str:
    """Extract text from a PDF file (path or file-like)."""
    text = ""
    if isinstance(pdf_path_or_file, str):  # path
        doc = fitz.open(pdf_path_or_file)
    else:  # file object (from upload)
        doc = fitz.open(stream=pdf_path_or_file.read(), filetype="pdf")

    for page in doc:
        text += page.get_text()
    doc.close()
    return text.strip()
