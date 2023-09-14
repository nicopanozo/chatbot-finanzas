import nltk

# retornamos una lista de segmentos de texto
# Divide el texto en segmentos de 800 palabras con una superposición de 150 palabras.
def get_chunk_text(text):

    sents = nltk.sent_tokenize(text)
    chunks = []
    for i in range(0, len(sents), 800):
        chunks.append(sents[i:i + 800])

        # agregamos el último segmento de texto del párrafo siguiente
        if i + 1 < len(sents):
            chunks.append(sents[i + 1:i + 1 + 150])

    return chunks


pdfs = open("after-load/pdf.txt", "r").read()

chunks = get_chunk_text(pdfs)

print(chunks)