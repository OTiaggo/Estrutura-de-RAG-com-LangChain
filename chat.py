from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

from dotenv import load_dotenv
load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

vector_store = Chroma(
    collection_name="operacao_de_trator",
    embedding_function=embeddings,
    persist_directory="./data/chroma_db"
)

results = vector_store.similarity_search(
    "Para que serve o diferencial ?"
)

@tool
def retrieve_context(query: str) -> str:
    """
    Recupera o conteúdo relevante do documento PDF com base na consulta fornecida.

    Args:
        query (str): A pergunta ou termo de busca a ser pesquisado no conteúdo do PDF.

    Returns:
        str: O conteúdo relevante extraído do PDF que responde à consulta.
    """
    results = vector_store.similarity_search(query)
    conteudo = ""

    for chuncks in results:
        conteudo += chuncks.page_content

    return conteudo

agent = create_agent(
    model="gpt-4o-mini",
    tools=[retrieve_context],
    system_prompt="Você é um expecialista em finanças e possui os dados dos resultados do segundo trimestre de 2025 da empresa WEG."
)

while True:
    query = input("Pergunta: ")
    result = agent.invoke({
        "messages": [
            {"role": "user", "content": query}
        ]
    })
    print(result['messages'][-1].content) 