from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text(pdf_file):
    reader = PdfReader(pdf_file)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + " "

    return text

def cosine_search(query, document_text):
    
    sentences = document_text.split('.')
    sentences = [s.strip() for s in sentences if s.strip() != ""]

    all_text = sentences + [query]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(all_text)

    query_vector = vectors[-1]
    sentence_vectors = vectors[:-1]

    similarities = cosine_similarity(query_vector, sentence_vectors)

    best_index = similarities.argmax()
    best_score = similarities[0][best_index]

    if best_score > 0:
        return sentences[best_index]
    else:
        return "Sorry, no relevant information is found"