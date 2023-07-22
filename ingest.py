import os
import getpass
import csv

os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key:")

class Document:
    def __init__(self, page_content, metadata):
        self.page_content = page_content
        self.metadata = metadata

    def __repr__(self):
        return f"Document(page_content=\"{self.page_content[:60]}...\", metadata={self.metadata})"

def parse_csv_and_create_documents(csv_file):
    documents = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            file, heading_text, content, _, _ = row  # Unpack the row values
            page_content = heading_text + " " + content
            metadata = {'source': file}
            documents.append(Document(page_content, metadata))
    return documents

# Example usage
csv_file = "output.csv"
docs = parse_csv_and_create_documents(csv_file)

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import TextLoader

embeddings = OpenAIEmbeddings()


db = FAISS.from_documents(docs, embeddings)
db.save_local("faiss_index")

new_db = FAISS.load_local("faiss_index", embeddings)


docs = new_db.similarity_search(query="how to install langchain" , k=3)


print(docs[0].page_content)