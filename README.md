# 🤖 Hermes AI Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain" />
  <img src="https://img.shields.io/badge/Ollama-100%25%20Local-black?style=for-the-badge" alt="Ollama" />
</p>

> 🚀 **Desenvolvido por [Luciana Sampaio](https://www.linkedin.com/in/luciana-sampaio/)** &nbsp;|&nbsp; ✍️ **[Medium](https://medium.com/@luciana.sampaio84)**

O **Hermes** é um assistente virtual inteligente, seguro e de alta performance configurado para rodar de forma **100% local e privada** no seu computador utilizando **Ollama** e **LangChain**.

O projeto conta com uma interface web de design limpo inspirada nas melhores aplicações de IA do mercado (ChatGPT, Claude), com streaming de respostas, gerenciamento de modelos e ferramentas de produtividade.

---

## ✨ Principais Funcionalidades

### 🖥️ Interface Web Streamlit (Hermes Studio)
- **Design Moderno:** Tema escuro com tipografia Google Outfit, microanimações e contraste aprimorado.
- **Detecção Automática do Ollama:** Monitora a conexão do Ollama local em tempo real com status visual pulsante.
- **Seletor de Modelos em Tempo Real:** Detecta automaticamente todos os modelos instalados no seu Ollama (`openhermes`, `llama3`, `mistral`, etc.) permitindo alterná-los na barra superior ou nas configurações.
- **Cards Interativos de Início Rápido:** Sugestões selecionáveis na tela inicial para desenvolvimento, engenharia de dados, IA e análise de documentos.
- **Unidades de Trabalho Interativas em Cada Resposta:**
  - 📋 **Copiar resposta ou código:** Copie o texto ou código formatado com um clique no bloco nativo.
  - ✏️ **Editar e reenviar pergunta:** Altere perguntas anteriores mantendo o histórico consistente.
  - 🔄 **Regenerar com outro modelo:** Compare respostas entre diferentes modelos do Ollama para a mesma pergunta.
  - 👍 **Feedback de respostas:** Avalie a precisão das respostas com sistema de aprovação/reprovação.
  - 📄 **Exportar documento:** Baixe qualquer resposta diretamente em Markdown (`.md`) ou Texto (`.txt`).
  - 📝 **Caderno de Notas:** Salve insights e respostas diretamente no seu caderno pessoal na barra lateral.

### 💬 Outras Interfaces
- **Chainlit App:** Interface conversacional com streaming contínuo palavra por palavra e histórico estruturado.
- **Terminal CLI:** Script Python para testes diretos via terminal via API REST do Ollama.

---

## 📂 Estrutura do Repositório

```text
llm-Cortex-hermes/
├── app.py                 # Interface principal web em Streamlit
├── chainlit_app.py        # Interface de chat conversacional em Chainlit
├── agent_hermes.py        # Interface CLI via terminal (requests)
├── chainlit.md            # Mensagem de apresentação do Chainlit
├── .streamlit/
│   └── config.toml        # Configuração de tema escuro e comportamento
├── Passo a Passo.md       # Guia complementar de execução
└── README.md              # Documentação oficial do projeto
```

---

## 🛠️ Pré-requisitos

1. **Python 3.9+** instalado.
2. **Ollama instalado e em execução**:
   - Baixe no site oficial: [ollama.com](https://ollama.com).
   - Baixe os modelos que deseja utilizar no seu terminal:
     ```bash
     ollama pull openhermes
     ollama pull llama3
     ```

---

## 🚀 Como Executar

### 1. Clonar o repositório e entrar na pasta
```bash
git clone https://github.com/luasampaio/llm-Cortex-hermes.git
cd llm-Cortex-hermes
```

### 2. Criar e ativar o ambiente virtual

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as dependências
```bash
pip install requests streamlit chainlit langchain-ollama langchain-core langchain-community
```

### 4. Executar as Aplicações

#### 🌐 Opção A: Interface Web Streamlit (Principal)
```bash
streamlit run app.py
```
> Acesse no seu navegador em `http://localhost:8501`.

#### 💬 Opção B: Interface Chainlit
```bash
chainlit run chainlit_app.py -w
```
> Acesse em `http://localhost:8000`.

#### 💻 Opção C: Terminal CLI
```bash
python agent_hermes.py
```

---

## ⚙️ Configurações e Modelos

- O modelo ativo pode ser alterado diretamente pela **Barra Superior** ou no menu **Configurações** na barra lateral.
- Para adicionar novos modelos ao Ollama para uso no Hermes:
  ```bash
  ollama run deepseek-r1:8b
  ollama run mistral
  ollama run qwen2.5:7b
  ```
- O Hermes detectará automaticamente os novos modelos instalados na próxima execução ou atualização de página.

---

## 👩‍💻 Autoria e Contato

Desenvolvido por **Luciana Sampaio**.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/luciana-sampaio/)
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@luciana.sampaio84)

