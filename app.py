import streamlit as st
import requests
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

# Configuração da página
st.set_page_config(
    page_title="Hermes Assistant",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo mínimo (apenas balões de chat e ajuste de layout)
st.markdown("""
    <style>
    /* Container principal com max-width para não espalhar demais em telas grandes */
    .block-container {
        max-width: 900px !important;
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    /* Balão de Chat Especial para o Assistant */
    [data-testid="stChatMessage"]:nth-child(even) {
        background-color: rgba(168, 85, 247, 0.05) !important;
        border-left: 4px solid #a855f7 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Inicializando o histórico do chat no session_state para evitar AttributeError
if "messages" not in st.session_state:
    st.session_state.messages = []

# Função para checar status do Ollama
@st.cache_data(ttl=5)
def check_ollama_status():
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code == 200:
            return True, "Conectado"
    except Exception:
        pass
    return False, "Offline"

is_connected, status_text = check_ollama_status()

# Configuração na barra lateral
with st.sidebar:
    st.logo("https://raw.githubusercontent.com/ollama/ollama/main/docs/ollama.png")
    st.header("Status & Modelos", divider="rainbow")
    
    if is_connected:
        st.success(f"**Ollama:** {status_text}", icon=":material/wifi:")
    else:
        st.error(f"**Ollama:** {status_text}", icon=":material/wifi_off:")
    
    st.markdown("**Selecione o modelo**")
    model_name = st.selectbox(
        label="Selecione o modelo",
        options=["openhermes", "llama3", "mistral", "phi3"],
        index=0,
        label_visibility="collapsed"
    )
    
    st.caption("Atenção: Modelos de IA podem gerar respostas imprecisas ou especulativas. Sempre verifique fatos importantes.")
    st.space(1)
    
    if st.button("Limpar Histórico", type="primary"):
        st.session_state.messages = []
        st.rerun()
        
    # Funcionalidade de exportar para Markdown
    if len(st.session_state.messages) > 0:
        chat_history = "# Histórico da Conversa com Hermes AI\n\n"
        for msg in st.session_state.messages:
            role = "Você" if isinstance(msg, HumanMessage) else "Hermes"
            chat_history += f"### {role}:\n{msg.content}\n\n---\n\n"
            
        st.download_button(
            label="📄 Exportar Conversa (MD)",
            data=chat_history,
            file_name="historico_hermes.md",
            mime="text/markdown",
            type="secondary"
        )
    
    st.space(3)
    st.caption("Desenvolvido com 💜 por Luciana Sampaio")

# Título Principal ou Saudação Inicial
if not st.session_state.messages:
    # Se o chat estiver vazio, mostramos a saudação em grande destaque
    st.markdown("<h1 style='text-align: center; margin-top: 2rem;'>👋 Olá Luciana! O que vamos explorar hoje?</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #9ca3af; margin-bottom: 3rem;'>Selecione uma opção ou digite sua pergunta abaixo.</p>", unsafe_allow_html=True)
    
    # Grade 2x2 de Sugestões
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("### :material/database: Databricks")
            st.caption("Quais foram as principais novidades anunciadas recentemente?")
            if st.button("Perguntar", key="q1"):
                st.session_state.initial_prompt = "Quais foram as novidades do Databricks?"
                st.rerun()
                
        with st.container(border=True):
            st.markdown("### :material/code: PySpark")
            st.caption("Como criar um pipeline de CDC em PySpark?")
            if st.button("Perguntar", key="q2"):
                st.session_state.initial_prompt = "Crie um pipeline de CDC em PySpark"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.markdown("### :material/analytics: Delta Lake")
            st.caption("Explique os fundamentos e vantagens de forma simples.")
            if st.button("Perguntar", key="q3"):
                st.session_state.initial_prompt = "Explique Delta Lake de forma simples"
                st.rerun()
                
        with st.container(border=True):
            st.markdown("### :material/attach_money: FinOps")
            st.caption("Quais as melhores práticas para reduzir custos na nuvem?")
            if st.button("Perguntar", key="q4"):
                st.session_state.initial_prompt = "Quais as melhores práticas de FinOps para reduzir custos na nuvem?"
                st.rerun()
else:
    # Se já tiver conversa, mostra apenas um cabeçalho mais compacto
    st.title("Hermes AI", icon=":material/smart_toy:")
    st.caption("Assistente local alimentado por LangChain e Ollama")
    st.space("medium")

# Função para instanciar o modelo
def get_llm():
    return ChatOllama(model=model_name, temperature=0.7)

# Renderizando o histórico na tela
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user", avatar=":material/person:"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant", avatar=":material/robot_2:"):
            st.markdown(msg.content)

prompt = st.chat_input("Pergunte sobre Databricks, PySpark, Delta Lake...")

# Verifica se o usuário clicou em um dos botões de sugestão
if "initial_prompt" in st.session_state:
    prompt = st.session_state.initial_prompt
    del st.session_state.initial_prompt

# Input de chat do usuário
if prompt:
    # Mostra e armazena a mensagem do usuário
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user", avatar=":material/person:"):
        st.markdown(prompt)

    # Gera a resposta do assistente
    with st.chat_message("assistant", avatar=":material/robot_2:"):
        if not is_connected:
            st.error("O Ollama não está rodando no momento. Certifique-se de iniciá-lo no seu computador antes de enviar mensagens.", icon=":material/wifi_off:")
            st.stop()
            
        try:
            llm = get_llm()
            
            # Streaming nativo
            def stream_response():
                for chunk in llm.stream(st.session_state.messages):
                    yield chunk.content
                    
            response_text = st.write_stream(stream_response())
            st.session_state.messages.append(AIMessage(content=response_text))
        
        except Exception as e:
            st.error(f"Ocorreu um erro ao gerar a resposta. Verifique se o modelo '{model_name}' está baixado (`ollama pull {model_name}`). Detalhes: {e}", icon=":material/error:")
