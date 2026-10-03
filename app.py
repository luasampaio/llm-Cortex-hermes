import streamlit as st
<<<<<<< HEAD
import requests
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

# Configuração da página
=======
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

# Configuração da página com tema escuro e ícone moderno
>>>>>>> 178103b479c28cfff51b213af005eeba9116238d
st.set_page_config(
    page_title="Hermes Assistant",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

<<<<<<< HEAD
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
=======
# Injeção de CSS Premium
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

    /* Definição de fontes e cores principais */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        font-family: 'Outfit', sans-serif;
        background-color: #0b0d13 !important;
        color: #f3f4f6 !important;
    }
    
    /* Customização do bloco de chat */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 16px !important;
        padding: 1.25rem !important;
        margin-bottom: 1rem !important;
        backdrop-filter: blur(12px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fadeInUp 0.5s ease-out;
    }
    
    .stChatMessage:hover {
        background: rgba(255, 255, 255, 0.04) !important;
        border-color: rgba(165, 180, 252, 0.2) !important;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.4);
        transform: translateY(-2px);
    }

    /* Container principal */
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        max-width: 900px !important;
    }
    
    /* Título com gradiente premium e brilho */
    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #a5b4fc 0%, #c084fc 50%, #e879f9 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
        text-align: center;
        filter: drop-shadow(0 2px 10px rgba(168, 85, 247, 0.2));
    }
    
    .main-subtitle {
        font-size: 1rem;
        color: #9ca3af;
        text-align: center;
        margin-bottom: 2.5rem;
        font-weight: 300;
        letter-spacing: 0.5px;
    }

    /* Customização da Sidebar */
    [data-testid="stSidebar"] {
        background-color: #06070a !important;
        border-right: 1px solid rgba(255, 255, 255, 0.04) !important;
    }
    
    .sidebar-header {
        font-size: 1.5rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 1.5rem;
        background: linear-gradient(135deg, #a5b4fc 0%, #e879f9 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Botão Limpar Histórico */
    .stButton>button {
        width: 100% !important;
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.6rem 1.5rem !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(124, 58, 237, 0.5) !important;
        color: #ffffff !important;
    }

    /* Inputs da Sidebar */
    .stTextInput>div>div>input {
        background-color: #0f121d !important;
        color: #f3f4f6 !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 10px !important;
        padding: 0.5rem 0.8rem !important;
    }

    .stTextInput>div>div>input:focus {
        border-color: #a855f7 !important;
        box-shadow: 0 0 0 2px rgba(168, 85, 247, 0.2) !important;
    }

    /* Balão de Chat Especial para o Assistant */
    [data-testid="stChatMessage"] {
        border-left: 4px solid #a855f7 !important;
    }

    /* Animação */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(15px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    </style>
""", unsafe_allow_html=True)

# Título e Subtítulo da Interface Premium
st.markdown('<h1 class="main-title">🔮 Hermes AI Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="main-subtitle">Experiência inteligente local alimentada por LangChain & Ollama</p>', unsafe_allow_html=True)

# Configuração na barra lateral para o nome do modelo
with st.sidebar:
    st.markdown('<h2 class="sidebar-header">Configurações</h2>', unsafe_allow_html=True)
    model_name = st.text_input("Modelo Ollama:", value="openhermes")
    st.info("💡 Certifique-se de que o Ollama está rodando e que você fez o pull do modelo no terminal (ex: `ollama pull openhermes`).")
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("✨ Limpar Histórico"):
        st.session_state.messages = [
            AIMessage(content="Olá Luciana, sou seu agente Hermes. Em que posso ajudar?")
        ]
        st.rerun()
    
    st.markdown("<br><br><hr style='border-color: rgba(255,255,255,0.05);'>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #6b7280; font-size: 0.8rem;'>Desenvolvido com 💜 por Luciana Sampaio</p>", unsafe_allow_html=True)

# Inicializando o histórico do chat no session_state
if "messages" not in st.session_state:
    st.session_state.messages = [
        AIMessage(content="Olá Luciana, sou seu agente Hermes. Em que posso ajudar?")
    ]
>>>>>>> 178103b479c28cfff51b213af005eeba9116238d

# Função para instanciar o modelo
def get_llm():
    return ChatOllama(model=model_name, temperature=0.7)

# Renderizando o histórico na tela
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
<<<<<<< HEAD
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
=======
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# Input de chat do usuário
if prompt := st.chat_input("Como o Hermes pode te ajudar hoje?"):
    # Mostra e armazena a mensagem do usuário
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Gera a resposta do assistente
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        with st.spinner("Hermes está pensando..."):
            try:
                llm = get_llm()
                # O LangChain passa todo o histórico de mensagens para o modelo
                response = llm.invoke(st.session_state.messages)
                response_text = response.content
                
                # Exibe a resposta
                message_placeholder.markdown(response_text)
                
                # Adiciona a resposta ao histórico
                st.session_state.messages.append(AIMessage(content=response_text))
            
            except Exception as e:
                st.error(f"Erro de conexão: Não foi possível se conectar ao Ollama. Verifique se ele está rodando. Detalhes: {e}")
>>>>>>> 178103b479c28cfff51b213af005eeba9116238d
