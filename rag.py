from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from dotenv import load_dotenv
load_dotenv()

# Carregando PDF
file_path = "./OPERACAO-DE-TRATORES.pdf"  
loader = PyPDFLoader(file_path)

docs = loader.load()

# Criando Chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)
all_splits = text_splitter.split_documents(docs)    

# Embeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Armazenando vetores com Chroma
vector_store = Chroma(
    collection_name="operacao_de_trator",
    embedding_function=embeddings,
    persist_directory="./data/chroma_db"
)

# Adicione splits no vectorStore
vector_store.add_documents(all_splits)

