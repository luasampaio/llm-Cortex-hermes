# 🤖 llm-Cortex-hermes

> 🚀 **Desenvolvido por Luciana Sampaio**

Este repositório contém a implementação do **Hermes**, um agente assistente virtual inteligente e amigável configurado para rodar de forma **100% local** em sua máquina utilizando o **Ollama** e o framework **LangChain**.


O projeto oferece três interfaces diferentes para interação com o agente:
1. **Interface CLI (Terminal):** Um script simples que envia solicitações via requisições HTTP REST diretamente para a API local do Ollama.
2. **Interface Streamlit (Web UI):** Uma interface gráfica web dinâmica com suporte a histórico de conversação mantido em sessão.
3. **Interface Chainlit (Chat App profissional):** Uma interface conversacional moderna de alto nível com suporte a **streaming de tokens em tempo real** (resposta gerada palavra por palavra) e gerenciamento avançado de histórico através das abstrações do LangChain.

---

## 📂 Estrutura do Projeto

O diretório principal está estruturado da seguinte forma:

*   [`agent_hermes.py`](./agent_hermes.py): Script Python para interação com o Ollama através do terminal utilizando a biblioteca `requests`.
*   [`app.py`](./app.py): Aplicação web interativa construída com **Streamlit** e `ChatOllama` do LangChain.
*   [`chainlit_app.py`](./chainlit_app.py): Aplicação conversacional avançada construída com **Chainlit**, suportando streaming de respostas e histórico de mensagens.
*   [`chainlit.md`](./chainlit.md): Tela de boas-vindas exibida na interface do Chainlit.


---

## 🛠️ Pré-requisitos

Para rodar o projeto localmente, você precisará ter instalado em sua máquina:

1.  **Python 3.9+** (recomendado usar ambiente virtual `.venv`).
2.  **Ollama**:
    *   Baixe e instale a partir do site oficial: [ollama.com](https://ollama.com).
    *   Com o Ollama rodando no seu sistema, baixe o modelo desejado (o padrão configurado é o `openhermes`, mas você pode alterar para o que preferir, como `llama3`, `mistral`, `gemma`, etc.):
        ```bash
        ollama pull openhermes
        ```

---

## 🚀 Instalação e Configuração

### 1. Clonar o repositório e acessar a pasta
```bash
cd llm-Cortex-hermes
```

### 2. Configurar o Ambiente Virtual
Crie e ative um ambiente virtual do Python:

**No Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**No Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar as Dependências
Instale os pacotes necessários rodando o seguinte comando:
```bash
pip install requests streamlit chainlit langchain-ollama langchain-core langchain-community
```

---

## 💻 Como Executar

Certifique-se de que o **Ollama** esteja em execução em segundo plano antes de iniciar qualquer uma das interfaces.

### Opção A: Executar a CLI (Linha de Comando)
Uma interação simples direto no seu terminal:
```bash
python agent_hermes.py
```

### Opção B: Executar a Interface Streamlit
Para abrir o painel web interativo no seu navegador:
```bash
streamlit run app.py
```
*   **Nota:** Na barra lateral da interface do Streamlit, você pode alterar dinamicamente o nome do modelo que deseja utilizar e limpar o histórico da conversa.

### Opção C: Executar a Interface Chainlit (Recomendado)
Para rodar a interface de chat premium com streaming de tokens em tempo real:
```bash
chainlit run chainlit_app.py -w
```
*   O parâmetro `-w` ativa o *auto-reload* (recarregamento automático) ao fazer alterações no código.

---

## ⚙️ Personalização

Se você quiser trocar o modelo padrão ou ajustar as instruções de comportamento do sistema, altere os arquivos:
*   **Em `chainlit_app.py`:** Altere o argumento `model="openhermes"` na linha 11 e mude o prompt do sistema na linha 15 (`"Você é o Hermes..."`).
*   **Em `app.py`:** Altere o valor padrão de `model_name` no input da barra lateral ou o parâmetro `temperature` no método `get_llm()`.
*   **Em `agent_hermes.py`:** Altere o parâmetro `model` na chamada da função principal.

---

<p align="center">
  <sub>Desenvolvido com 🧠 e 💻 por <b>Luciana Sampaio</b>.</sub>
</p>

