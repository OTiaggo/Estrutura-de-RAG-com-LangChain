# RAG com LangChain  
Estrutura de RAG (Retrieval‑Augmented Generation) utilizando LangChain e base de documentos para gerar respostas com contexto.

## 🔍 Visão Geral  
Este projeto fornece uma **estrutura básica** para criação de um sistema de QA (perguntas e respostas) ou assistente que combina:  
- Recuperação de documentos (uma base de dados de conhecimento)  
- Geração de respostas de modelo de linguagem com contexto recuperado  
- Integração com LangChain para orquestração dos fluxos de RAG  

## 📂 Contéudo do Repositório  
- `rag.py` – código para indexação/armazenamento da base de conhecimento e mecanismo de RAG.  
- `chat.py` – interface simples de chat para interagir com o sistema.  
- `data/` – pasta contendo a base de dados (por exemplo, `chroma_db`) onde os documentos são armazenados ou indexados.  
- `OPERACAO‑DE‑TRATORES.pdf` – exemplo de documento inserido na base de conhecimento.  
- `requeriments.txt` – lista de dependências necessárias.  
- `.gitignore` – arquivos/pastas ignorados no versionamento.

## 🛠 Funcionalidades Principais  
- Carregar documentos (PDF ou outros formatos) na base de conhecimento.  
- Indexar os documentos para uso posterior na fase de recuperação.  
- Fazer **querys** do usuário: o sistema recupera trechos relevantes da base, e depois o modelo — com LangChain — gera uma resposta considerando o contexto recuperado.  
- Interface de chat simples para entrada de usuário e resposta do sistema.

## ✅ Por que esse projeto é útil  
- Permite construir **assistentes de conhecimento** que entendem e respondem com base em documentos específicos.  
- Ajuda a reduzir “alucinações” de modelos de linguagem, pois a resposta é amparada por uma base documental.  
- Estrutura simples e adaptável: você pode trocar os documentos, modelo de linguagem, ou mecanismo de recuperação conforme suas necessidades.

## 📋 Como usar  
1. Clone o repositório:  
   ```bash
   git clone https://github.com/OTiaggo/RAG-com-LangChain.git  
   cd RAG-com-LangChain  
   ```  
2. Instale dependências:  
   ```bash
   pip install -r requeriments.txt  
   ```  
3. Crie o `.env` e crie a variável **OPENAI_API_KEY** passando sua chave de api da openai 
4. Modifique `rag.py` para apontar para seu PDF.  
5. Execute o script de indexação/recuperação (`rag.py`) para preparar a base.  
6. Execute o chat (`chat.py`) e interaja com o sistema:  
   ```bash
   python chat.py  
   ```  
7. Digite sua pergunta e veja a resposta gerada com contexto recuperado.

## ⚙️ Configurações & Personalização  
- Você pode configurar qual modelo de linguagem usar (por exemplo, OpenAI GPT, local model, etc.).  
- Modificar o tamanho do “chunk” de documentos, método de vetorização/embedding, etc.  
- Adaptar a UI (interface) para web, terminal ou API.  
- Expandir a base de conhecimento conforme o domínio desejado.

## 🧪 Exemplos de uso  
- Perguntar algo como: *“Como operar um trator?”* e ver como o sistema utiliza o documento `OPERACAO‑DE‑TRATORES.pdf`.  
- Expandir para outros domínios como manual de usuário, base jurídica, FAQ de empresa, etc.  
- Integrar com front‑end ou bot de chat para atendimento automatizado com conhecimento embutido.

## 👥 Contribuição  
Contribuições são bem‑vindas! Você pode:  
- Adicionar suporte a novos formatos de documento (DOCX, HTML, etc).  
- Melhorar a interface de chat.  
- Integrar com outros mecanismos de recuperação ou bases de dados.  
- Escrever testes ou documentação adicional.

