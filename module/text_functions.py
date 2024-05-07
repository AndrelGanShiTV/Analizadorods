from docx import Document
import PyPDF2

# Extraer Texto de un PDF
def extract_text_from_pdf(pdf_file_path):
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file_path)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
           page = pdf_reader.pages[page_num]
           text += page.extract_text()
        return text
    except Exception as e:
        return str(e)

# Extraer Texto de un Word
def extract_text_from_docx(docx_filename):
    doc = Document(docx_filename)
    text = []
    for paragraph in doc.paragraphs:
        text.append(paragraph.text)
    return ' '.join(text)

# Tokenizar y eliminar stopwords
def eliminar_stopwords(texto, stopwords):
        palabras = texto.split(" ")  # Supongo que las palabras clave están separadas por comas y espacios
        palabras_sin_stopwords = [palabra for palabra in palabras if palabra.lower() not in stopwords]
        return " ".join(palabras_sin_stopwords)