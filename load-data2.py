import spacy
import os
import PyPDF2

def get_embeddings(sentences):
    # Create a spaCy model
    nlp = spacy.load("en_core_web_trf")

    # Get the embeddings
    embeddings = nlp(sentences).vectors

    return embeddings

def get_pdf_sentences(pdf_file_path):
    # Initialize a variable to store extracted sentences
    extracted_sentences = ""

    # Open the PDF file
    with open(pdf_file_path, "rb") as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        # Iterate through pages and extract text
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            page_text = page.extractText()
            
            # Append extracted text to the variable
            extracted_sentences += page_text

    # Create a spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Process the extracted text to split it into sentences
    doc = nlp(extracted_sentences)

    # Initialize a variable to store sentences
    sentences = []

    # Extract sentences from the processed text
    for sent in doc.sents:
        sentences.append(sent.text)

    return " ".join(sentences)

def load_pdf_data():
    # Get the list of PDF files in the directory
    pdf_files = os.listdir("./finances-data")

    # List to store the content of all PDFs
    all_data = []

    # Iterate over the PDF files
    for pdf_file in pdf_files:
        # Load the PDF file and get the sentences
        sentences = get_pdf_sentences(f"./finances-data/{pdf_file}")

        # Get the embeddings of the sentences
        embeddings = get_embeddings(sentences)

        # Add the embeddings to the list
        all_data.extend(embeddings)

    return all_data

# Call the function
all_data = load_pdf_data()
print(all_data)
