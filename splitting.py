# !pip install langchain
# !pip install python-dotenv
# !pip install openai
# !pip install pypdf


import os
import openai
import sys
from dotenv import load_dotenv, find_dotenv

os.environ["OPENAI_API_KEY"] = "openIAKEY"
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']


from langchain.text_splitter  import RecursiveCharacterTextSplitter, CharacterTextSplitter


chunk_size = 10
chunk_overlap = 4


r_splitter = RecursiveCharacterTextSplitter( chunk_size = chunk_size, chunk_overlap = chunk_overlap)
c_splitter = CharacterTextSplitter( chunk_size = chunk_size, chunk_overlap = chunk_overlap)


text1 = 'gdqweuydbqwiuqwidpwqiudbqwiud'
r_splitter.split_text(text1)


text3 = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
r_splitter.split_text(text3)


c_splitter.split_text(text3)
c_splitter.split_text(text1)


text = """When writing documents, writers will use document structure to group content. \
This can convey to the reader, which idea's are related. For example, closely related ideas \
are in sentances. Similar ideas are in paragraphs. Paragraphs form a document. \n\n  \
Paragraphs are often delimited with a carriage return or two carriage returns. \
Carriage returns are the "backslash n" you see embedded in this string. \
Sentences have a period at the end, but also, have a space.\
and words are separated by space."""


len(text)


c_splitter = CharacterTextSplitter( chunk_size = 100, chunk_overlap = 50, separator = ' ')
r_splitter = RecursiveCharacterTextSplitter( chunk_size = 100, chunk_overlap = 50, separators=["\n", "\n\n", " ", ""])


c_splitter.split_text(text)



r_splitter.split_text(text)


r_splitter = RecursiveCharacterTextSplitter( chunk_size = 150, chunk_overlap = 0, separators=["\n", "\n\n", " ", ""])
r_splitter.split_text(text)


r_splitter = RecursiveCharacterTextSplitter( chunk_size = 150, chunk_overlap = 0, separators=["\n", "\n\n", "(?<=\. )" " ", ""])
r_splitter.split_text(text)


# !pip install tiktoken


from langchain.text_splitter  import TokenTextSplitter
token_text_splitter = TokenTextSplitter(chunk_size = 1, chunk_overlap = 0)


text2 = 'foo bar bazzyfoo'


token_text_splitter.split_text(text2)


from langchain.text_splitter  import MarkdownHeaderTextSplitter


document = """"
# Title\n\n \
## Chapter 1\n\n \
Hi this is Jim\n\n Hi this is Joe\n\n \
### Section \n\n \
Hi this is Lance \n\n
## Chapter 2\n\n \
Hi this is Molly
"""


headers_to_split = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
]


makrdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on = headers_to_split)
md_header_splits = makrdown_splitter.split_text(document)


md_header_splits[0]



md_header_splits[1]


md_header_splits[2]