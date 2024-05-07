from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def vectorizar_similitud(ods_keywords, query_text):
    # Crear un vectorizador TF-IDF
    vectorizer = TfidfVectorizer()

    # Transformar las palabras clave de los ODS en vectores TF-IDF
    X = vectorizer.fit_transform(ods_keywords)

    # Transformar el texto de consulta en un vector TF-IDF
    query_vector = vectorizer.transform([query_text])

    # Calcular la similitud del coseno entre el texto de consulta y las palabras clave de los ODS
    cosine_similarities = cosine_similarity(X, query_vector)

    # Calcular los porcentajes de similitud para cada ODS
    similarity_percentages = (cosine_similarities * 100).flatten()

    return similarity_percentages