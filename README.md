# RAG com LangChain  
Estrutura de RAG (Retrieval-Augmented Generation) utilizando LangChain e base de documentos para gerar respostas contextualizadas — neste exemplo, sobre os **resultados financeiros da WEG no segundo semestre de 2025**.

## 🔍 Visão Geral  
Este projeto demonstra como criar um sistema de **Perguntas e Respostas (QA)** baseado em documentos, usando o conceito de **RAG (Retrieval-Augmented Generation)**.  
O sistema é capaz de:  
- Ler relatórios e documentos sobre o **resultado da WEG no 2º semestre de 2025**;  
- Indexar o conteúdo desses documentos em uma base vetorial;  
- Recuperar os trechos mais relevantes conforme a pergunta do usuário;  
- Gerar respostas contextualizadas com suporte do modelo de linguagem via **LangChain**.

## 📂 Estrutura do Repositório  
- `rag.py` – código responsável por carregar os documentos, gerar embeddings e indexar a base vetorial.  
- `chat.py` – interface de chat simples para interação com o modelo.  
- `data/` – pasta que contém os documentos utilizados (por exemplo, relatórios financeiros da WEG).  
- `requeriments.txt` – dependências necessárias.  
- `.gitignore` – lista de arquivos ignorados no versionamento.  

## 🛠 Funcionalidades Principais  
- **Carregamento automático de documentos** PDF ou texto (relatórios da WEG).  
- **Geração de embeddings** com `OpenAIEmbeddings` ou outro modelo configurável.  
- **Armazenamento vetorial** em memória (pode ser substituído por ChromaDB, FAISS, etc.).  
- **Busca semântica e geração de resposta** baseada nos trechos mais relevantes do documento.  
- **Chat interativo** que responde perguntas sobre o desempenho e resultados da empresa.

## ✅ Por que esse projeto é útil  
- Permite responder perguntas sobre relatórios ou comunicados financeiros com base em fontes oficiais.  
- Evita respostas genéricas ou incorretas ao ancorar o modelo em **dados reais**.  
- Serve como base para criar **assistentes financeiros**, **analisadores de relatórios corporativos** ou **dashboards inteligentes**.  

## 📋 Como usar  
1. Clone o repositório:  
   ```bash
   git clone https://github.com/OTiaggo/RAG-com-LangChain.git  
   cd RAG-com-LangChain  
   ```

2. Instale as dependências:  
   ```bash
   pip install -r requeriments.txt  
   ```

3. Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API da OpenAI:  
   ```bash
   echo "OPENAI_API_KEY=sua_chave_aqui" > .env
   ```
   > Substitua `sua_chave_aqui` pela sua chave real obtida no [Painel da OpenAI](https://platform.openai.com/account/api-keys).

4. Coloque os relatórios da **WEG (2º semestre de 2025)** dentro da pasta `data/`.  

5. Gere a base vetorial executando:  
   ```bash
   python rag.py  
   ```

6. Inicie o chat interativo:  
   ```bash
   python chat.py  
   ```

7. Faça perguntas como:  
   - “Qual foi o lucro líquido da WEG no segundo semestre de 2025?”  
   - “Houve crescimento de receita em comparação ao primeiro semestre?”  
   - “Quais foram os principais fatores que influenciaram os resultados?”  

## ⚙️ Personalização  
- Substitua os documentos na pasta `data/` para outros relatórios ou períodos.  
- Altere o modelo de embeddings (`OpenAIEmbeddings`, `HuggingFaceEmbeddings`, etc.).  
- Use outra base vetorial persistente (ChromaDB, FAISS, Pinecone, etc.).  
- Adapte a interface de chat para uma aplicação web ou API REST.  

## 🧪 Exemplos de uso  
- **Chat corporativo:** Responde perguntas sobre resultados trimestrais de empresas.  
- **Análise de mercado:** Consolida informações de múltiplos relatórios financeiros.  
- **Assistente interno:** Suporte a equipes financeiras para consulta de dados históricos da WEG.  

## 👥 Contribuição  
Contribuições são bem-vindas!  
Você pode:  
- Adicionar novos formatos de documentos (DOCX, HTML, etc.);  
- Melhorar a interface de chat;  
- Integrar com dashboards de BI;  
- Adicionar mais análises automáticas baseadas em métricas financeiras.  