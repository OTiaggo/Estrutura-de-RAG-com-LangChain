# from langchain.chat_models import init_chat_model
# from langchain.tools import tool
# from langchain.agents import create_agent
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import chromadb

from dotenv import load_dotenv
load_dotenv()

client = chromadb.PersistentClient(path="./data/chroma_db")

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = Chroma(
    client=client,
    collection_name="operacao_de_trator",
    embedding_function=embeddings,
)

results = vector_store.similarity_search(
    "Para que serve o diferencial ?"
)

print(results)

# @tool
# def retrieve_context(query: str) -> str:
#     """
#     Recupera o conteúdo relevante do documento PDF com base na consulta fornecida.

#     Args:
#         query (str): A pergunta ou termo de busca a ser pesquisado no conteúdo do PDF.

#     Returns:
#         str: O conteúdo relevante extraído do PDF que responde à consulta.
#     """
#     results = client.similarity_search(query)
#     conteudo = ""

#     for chuncks in results:
#         conteudo += chuncks.page_content

#     return conteudo

# agent = create_agent(
#     model="gpt-4o-mini",
#     tools=[retrieve_context],
#     system_prompt="Você é um especialista em operar tratores."
# )

# while True:
#     query = input("Pergunta: ")
#     result = agent.invoke({
#         "messages": [
#             {"role": "user", "content": query}
#         ]
#     })
#     print(result) 