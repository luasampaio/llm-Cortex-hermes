# Passo a Passo: Executar o Hermes Assistant com Interface Premium

Este guia orienta sobre como configurar o ambiente virtual, instalar as dependências corretas e rodar o Hermes Assistant com a nova interface Streamlit premium.

## 🚀 Requisitos Prévios

1. **Ollama instalado e rodando:**
   - Faça o download em [ollama.com](https://ollama.com).
   - Certifique-se de que ele está ativo em segundo plano (você deve ver o ícone na barra de tarefas do Windows).
2. **Modelo baixado:**
   - Abra o terminal (PowerShell ou CMD) e baixe o modelo padrão do Hermes:
     ```powershell
     ollama pull openhermes
     ```

---

## 🛠️ Configuração e Execução

### 1. Acessar a pasta do projeto
Certifique-se de que você está no terminal na raiz do projeto:
```powershell
cd d:\Projetos_2026_agents\llm-Cortex-hermes
```

### 2. Ativar o Ambiente Virtual (Python 3.13)
O ambiente virtual foi atualizado para o Python 3.13 para evitar problemas de compatibilidade. Ative-o com:
```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Instalar/Verificar as Dependências
Todas as dependências necessárias para a interface premium e conectividade local já estão configuradas. Para garantir que tudo esteja atualizado, execute:
```powershell
pip install -r requirements.txt
```

### 4. Executar a Interface Premium do Streamlit
Para inicializar o servidor local do Streamlit e abrir o app no seu navegador, execute:
```powershell
streamlit run app.py
```

Se o seu navegador não abrir automaticamente, clique no link abaixo ou copie e cole no navegador:
👉 **[http://localhost:8501](http://localhost:8501)**

---

## 🎨 Principais Recursos da Interface Premium
- **Tema Dark Moderno:** Baseado em tons escuros e degradês de roxo/indigo.
- **Mensagem Personalizada:** Exibição imediata de *"Olá Luciana, sou seu agente Hermes. Em que posso ajudar?"*.
- **Micro-animações:** Transição de surgimento suave ao receber ou enviar mensagens.
- **Configurações Rápidas:** Barra lateral interativa para alternar o modelo do Ollama e limpar o histórico.
