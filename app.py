import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

# Configuração da página com tema escuro e ícone moderno
st.set_page_config(
    page_title="Hermes Assistant",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

# Função para instanciar o modelo
def get_llm():
    return ChatOllama(model=model_name, temperature=0.7)

# Renderizando o histórico na tela
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
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
