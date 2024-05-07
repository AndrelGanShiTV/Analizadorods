from module.text_functions import extract_text_from_docx, extract_text_from_pdf, eliminar_stopwords
from module.StringsArray import stopwords, ods_keywords_con_stopword, ods_labels
from module.vectorizar import vectorizar_similitud
# import numpy as np

def calcular_similitud_archivo(archivo, file_path):
    if not file_path:
        return 
    
    # Validar tipo de archivo
    if archivo == 'PDF':
        query_text  = extract_text_from_pdf(file_path)
    elif archivo == 'DOCX':
        query_text = extract_text_from_docx(file_path)
    else:
        print('Error: No se puede usar este tipo de archivo')
        query_text = ''

    # Tu código para calcular similitud
    # Aplicar la función a cada palabra clave
    ods_keywords = [eliminar_stopwords(palabra, stopwords) for palabra in ods_keywords_con_stopword]

    #Vectorizar
    similarity_percentages = vectorizar_similitud(ods_keywords, query_text)

    # Calcular una métrica global (promedio de similitud)
    # global_similarity = np.mean(similarity_percentages)

    # Crear un diccionario que relacione los ODS con sus porcentajes de similitud
    results = dict(zip(ods_labels, similarity_percentages))
    
    # Ordenar los resultados por porcentaje de similitud en orden descendente
    results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1], reverse=True)}

    # Mostrar los resultados con el nombre del ODS correspondiente
    for ods, percentage in results.items():
        print(f"{ods}: {percentage:.2f}%")
    
    return results
