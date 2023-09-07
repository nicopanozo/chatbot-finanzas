# !pip install langchain
# !pip install python-dotenv
# !pip install openai
# !pip install pypdf

import os
import openai
from dotenv import load_dotenv
from langchain.document_loaders import PyPDFLoader

# loading the environment variables from .env file
load_dotenv()

# access to the OpenAI API key from .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

# configure the API Key
openai.api_key = openai_api_key

# conContinúa con tu código para cargar y procesar el PDF
loader = PyPDFLoader("1.pdf")
pages = loader.load()

