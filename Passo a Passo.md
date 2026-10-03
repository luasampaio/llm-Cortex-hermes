# 📘 Passo a Passo: Hermes AI Assistant

> 🚀 **Desenvolvido por [Luciana Sampaio](https://www.linkedin.com/in/luciana-sampaio/)** &nbsp;|&nbsp; ✍️ **[Medium](https://medium.com/@luciana.sampaio84)**

Este guia prático orienta como configurar o ambiente, iniciar o Ollama, executar a aplicação e utilizar todos os recursos interativos do **Hermes AI Assistant**.

---

## 🛠️ 1. Requisitos Prévios

### A. Ollama Instalado e em Execução
1. Faça o download no site oficial caso ainda não tenha instalado: [ollama.com](https://ollama.com).
2. Certifique-se de que o **Ollama está aberto e ativo em segundo plano** (ícone visível na bandeja do Windows).

### B. Baixar os Modelos Desejados
Abra o seu terminal (PowerShell ou CMD) e faça o download dos modelos que deseja utilizar:
```powershell
# Modelo padrão recomendado
ollama pull openhermes

# Modelos adicionais para comparar respostas (opcional)
ollama pull llama3
ollama pull mistral
```

---

## 💻 2. Ativação do Ambiente e Dependências

Abra o terminal do PowerShell na raiz do projeto:

```powershell
# 1. Acessar a pasta do projeto
cd d:\Projetos_2026_agents\llm-Cortex-hermes

# 2. Ativar o ambiente virtual
.\.venv\Scripts\Activate.ps1

# 3. Garantir que as dependências estão instaladas
pip install -r requirements.txt
```

---

## 🚀 3. Executando as Aplicações

### Opção A: Interface Web Streamlit (Principal)
Para iniciar a aplicação web do Hermes com o design escuro e recursos interativos:
```powershell
streamlit run app.py
```
> O navegador abrirá automaticamente em: 👉 **[http://localhost:8501](http://localhost:8501)**

### Opção B: Interface Conversacional Chainlit
Caso queira testar a interface conversacional com streaming contínuo:
```powershell
chainlit run chainlit_app.py -w
```
> Acesse em: 👉 **[http://localhost:8000](http://localhost:8000)**

---

## 🎯 4. Guia de Recursos e Unidades de Trabalho

A interface do Hermes foi projetada para que cada interação seja uma unidade de trabalho produtiva:

### ⚡ 1. Troca Dinâmica de Modelos
- **Na Barra Superior (Top Bar):** Um seletor suspenso detecta e lista automaticamente todos os modelos instalados no seu Ollama local.
- **Nas Configurações da Barra Lateral:** Você pode conferir quais modelos estão instalados ou digitar qualquer modelo customizado para ativá-lo na hora.

### 💡 2. Cards de Início Rápido (Splash Screen)
- Ao abrir uma nova conversa, são exibidos 4 cartões clicáveis:
  - **Desenvolvimento** *(Python, Spark e arquitetura)*
  - **Engenharia de dados** *(SQL, Databricks e pipelines)*
  - **Inteligência artificial** *(LLMs, RAG e agentes)*
  - **Análise de documentos** *(Resumir e extrair informações)*
- Clicar em qualquer card inicia a conversa instantaneamente com uma pergunta de alto nível.

### 📋 3. Copiar Resposta ou Código
- Embaixo de qualquer resposta do Hermes, clique no botão **Copiar** (`:material/content_copy:`).
- Abre uma prévia em bloco com botão de cópia nativo no canto superior direito para copiar tudo com apenas 1 clique.

### ✏️ 4. Editar e Reenviar Pergunta
- Ao lado da sua pergunta enviada, clique no ícone de lápis (`:material/edit:`).
- Um editor *inline* será aberto para que você ajuste o texto. Ao clicar em **Salvar e reenviar**, o Hermes responde imediatamente à nova versão.

### 🔄 5. Regenerar com Outro Modelo
- No botão **Regenerar** (`:material/refresh:`), selecione outro modelo do Ollama e clique em **Regenerar agora**.
- O sistema refaz a resposta usando o novo modelo escolhido, facilitando a comparação de raciocínio entre diferentes LLMs.

### 👍 6. Avaliar com Feedback
- Avalie cada resposta com os ícones de polegar (👍 / 👎) com confirmação visual instantânea (*toast*).

### 📄 7. Exportar e Caderno de Notas
- No botão **Documento** (`:material/description:`):
  - **Baixar Markdown (.md):** Exporta o conteúdo formatado.
  - **Baixar Texto (.txt):** Exporta em formato de texto simples.
  - **Salvar no Caderno de Notas:** Armazena a nota na barra lateral, onde você pode consultá-la, baixá-la individualmente ou excluí-la quando quiser.

---

## 👩‍💻 Autoria
 
Desenvolvido por **[Luciana Sampaio](https://www.linkedin.com/in/luciana-sampaio/)** &nbsp;|&nbsp; Siga no **[Medium](https://medium.com/@luciana.sampaio84)**

