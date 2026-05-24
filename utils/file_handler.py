import pypdf
import docx2txt
import io

def extract_text_from_file(uploaded_file) -> str:
    """Extracts raw string text content from PDF, TXT, or DOCX formats safely."""
    filename = uploaded_file.name.lower()
    
    try:
        if filename.endswith('.txt'):
            return uploaded_file.read().decode("utf-8")
            
        elif filename.endswith('.pdf'):
            pdf_reader = pypdf.PdfReader(io.BytesIO(uploaded_file.read()))
            text = ""
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text
            
        elif filename.endswith('.docx'):
            file_bytes = uploaded_file.read()
            text = docx2txt.process(io.BytesIO(file_bytes))
            return text
            
        else:
            return ""
    except Exception as e:
        return f"Error extracting text: {str(e)}"