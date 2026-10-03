import streamlit as st
import requests
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage

st.set_page_config(
    page_title="Hermes Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');

    html, body, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        font-family: 'Outfit', sans-serif;
    }

    /* Hide Streamlit Deploy button and header menu */
    [data-testid="stDeployButton"],
    .stDeployButton,
    #MainMenu,
    [data-testid="stToolbarActions"],
    [data-testid="stToolbar"],
    footer {
        display: none !important;
    }

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

    .block-container {
        padding-bottom: 2rem !important;
        max-width: 900px !important;
    }

    .main-title {
        font-size: 2.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #a5b4fc 0%, #e879f9 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
        text-align: center;
        letter-spacing: -0.5px;
    }

    .main-subtitle {
        font-size: 1rem;
        color: #9ca3af;
        text-align: center;
        margin-bottom: 2.5rem;
        font-weight: 300;
        letter-spacing: 0.5px;
    }

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
    
    /* Subtle hover for buttons */
    .stButton>button {
        transition: all 0.2s ease !important;
        border-radius: 8px !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(255, 255, 255, 0.05) !important;
    }
    
    /* Top status indicator */
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 0.85rem;
        padding: 5px 12px;
        border-radius: 20px;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.07);
    }
    
    .status-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        display: inline-block;
    }
    .status-dot.online {
        background-color: #22c55e;
        box-shadow: 0 0 8px #22c55e;
    }
    .status-dot.offline {
        background-color: #ef4444;
        box-shadow: 0 0 8px #ef4444;
    }

    /* Prompt suggestion cards (st.button in prompt grid) */
    .prompt-grid .stButton > button {
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: flex-start !important;
        text-align: left !important;
        width: 100% !important;
        min-height: 80px !important;
        padding: 14px 18px !important;
        border-radius: 14px !important;
        background: rgba(255, 255, 255, 0.02) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        cursor: pointer !important;
        margin-bottom: 0.75rem !important;
    }

    .prompt-grid .stButton > button:hover {
        background: rgba(255, 255, 255, 0.05) !important;
        border-color: rgba(165, 180, 252, 0.4) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.35), 0 0 15px rgba(165, 180, 252, 0.1) !important;
    }

    .prompt-grid .stButton > button:active {
        transform: translateY(0) !important;
        background: rgba(255, 255, 255, 0.08) !important;
    }

    /* Icon styling in cards */
    .prompt-grid .stButton > button span:first-child {
        font-size: 1.3rem !important;
        margin-right: 0.6rem !important;
        color: #a5b4fc !important;
    }

    .prompt-grid .stButton > button [data-testid="stMarkdownContainer"] {
        display: flex !important;
        flex-direction: column !important;
        align-items: flex-start !important;
        text-align: left !important;
        width: 100% !important;
    }

    .prompt-grid .stButton > button [data-testid="stMarkdownContainer"] p {
        margin: 0 !important;
        text-align: left !important;
        line-height: 1.4 !important;
    }

    .prompt-grid .stButton > button [data-testid="stMarkdownContainer"] p:first-child strong {
        color: #f1f5f9 !important;
        font-size: 0.95rem !important;
        font-weight: 600 !important;
        letter-spacing: -0.2px !important;
    }

    .prompt-grid .stButton > button [data-testid="stMarkdownContainer"] p:last-child {
        color: #9ca3af !important;
        font-size: 0.82rem !important;
        font-weight: 300 !important;
        margin-top: 2px !important;
    }

    /* Compact action bar buttons inside chat messages */
    [data-testid="stChatMessage"] .stButton > button,
    [data-testid="stChatMessage"] [data-testid="stPopover"] > button,
    [data-testid="stChatMessage"] [data-testid="stDownloadButton"] > button {
        min-height: 32px !important;
        height: 32px !important;
        padding: 4px 10px !important;
        font-size: 0.8rem !important;
        border-radius: 8px !important;
        background: rgba(255, 255, 255, 0.03) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        color: #9ca3af !important;
    }

    [data-testid="stChatMessage"] .stButton > button:hover,
    [data-testid="stChatMessage"] [data-testid="stPopover"] > button:hover,
    [data-testid="stChatMessage"] [data-testid="stDownloadButton"] > button:hover {
        background: rgba(255, 255, 255, 0.08) !important;
        border-color: rgba(165, 180, 252, 0.3) !important;
        color: #f1f5f9 !important;
        transform: translateY(-1px) !important;
    }

    /* Subtle thumbs feedback */
    [data-testid="stChatMessage"] [data-testid="stFeedback"] {
        padding-top: 1px !important;
    }

    /* Top bar model selector styling */
    div[data-testid="stSelectbox"] div[data-baseweb="select"] {
        border-radius: 12px !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        background-color: rgba(255, 255, 255, 0.03) !important;
        backdrop-filter: blur(8px) !important;
        transition: all 0.2s ease !important;
        font-size: 0.88rem !important;
        min-height: 38px !important;
    }

    div[data-testid="stSelectbox"] div[data-baseweb="select"]:hover {
        border-color: rgba(165, 180, 252, 0.4) !important;
        background-color: rgba(255, 255, 255, 0.06) !important;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2) !important;
    }

    div[data-testid="stSelectbox"] svg {
        fill: #9ca3af !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

@st.cache_data(ttl=5)
def get_ollama_status_and_models():
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        if response.status_code == 200:
            data = response.json()
            models = [m.get("name") for m in data.get("models", []) if m.get("name")]
            return True, "Ollama conectado", models
    except Exception:
        pass
    return False, "Ollama desconectado", []

is_connected, status_text, available_models = get_ollama_status_and_models()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "model_name" not in st.session_state:
    if available_models:
        matching = [m for m in available_models if "openhermes" in m]
        st.session_state.model_name = matching[0] if matching else available_models[0]
    else:
        st.session_state.model_name = "openhermes"

# Build list of options for the selector
model_options = list(available_models)
if st.session_state.model_name and st.session_state.model_name not in model_options:
    model_options.insert(0, st.session_state.model_name)
if not model_options:
    model_options = ["openhermes"]


with st.sidebar:
    st.markdown("### :material/smart_toy: Hermes AI")
    
    if st.button("Nova conversa", icon=":material/add:", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    # Active model display badge in sidebar
    st.markdown(
        f"""
        <div style='background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.07); border-radius: 10px; padding: 10px 14px; margin-top: 12px; margin-bottom: 12px;'>
            <div style='font-size: 0.72rem; color: #9ca3af; text-transform: uppercase; font-weight: 600; letter-spacing: 0.5px;'>Modelo Ativo</div>
            <div style='font-size: 0.92rem; font-weight: 600; color: #a5b4fc; margin-top: 4px; display: flex; align-items: center; gap: 6px;'>
                <span>⚡</span> <code>{st.session_state.model_name}</code>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
        
    st.markdown("<p style='color: #6b7280; font-size: 0.75rem; font-weight: bold; margin-top: 1.5rem; margin-bottom: 0.5rem;'>HISTÓRICO</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 0.9rem; margin-bottom: 0.5rem;'>Conversas recentes</p>", unsafe_allow_html=True)
    st.caption("Nenhuma conversa")

    # Caderno de Notas (Saved Notes) in Sidebar
    if "notes" in st.session_state and st.session_state.notes:
        st.markdown("<p style='color: #6b7280; font-size: 0.75rem; font-weight: bold; margin-top: 1.5rem; margin-bottom: 0.5rem;'>CADERNO DE NOTAS</p>", unsafe_allow_html=True)
        with st.expander(f":material/bookmark: Notas Salvas ({len(st.session_state.notes)})", expanded=True):
            for n_idx, note in enumerate(st.session_state.notes):
                st.markdown(f"**{note['title']}**")
                st.caption(f"Modelo: `{note.get('model', 'ollama')}`")
                
                c_dl, c_del = st.columns([0.75, 0.25])
                with c_dl:
                    st.download_button(
                        label="Baixar .md",
                        data=note['content'],
                        file_name=f"{note['title'].replace(' ', '_')}.md",
                        mime="text/markdown",
                        icon=":material/download:",
                        key=f"dl_note_{n_idx}"
                    )
                with c_del:
                    if st.button("🗑️", key=f"del_note_{n_idx}", help="Excluir nota"):
                        st.session_state.notes.pop(n_idx)
                        st.rerun()
                st.markdown("<hr style='margin: 8px 0; border: none; border-top: 1px solid rgba(255,255,255,0.06);'>", unsafe_allow_html=True)
    
    # Spacer
    st.markdown("<div style='margin-top: 25vh;'></div>", unsafe_allow_html=True)
    
    with st.popover("Configurações", icon=":material/settings:", use_container_width=True):
        st.markdown("#### Configuração do Modelo")
        st.caption(f"Modelo ativo: `{st.session_state.model_name}`")
        
        if available_models:
            st.markdown("<p style='font-size: 0.85rem; color: #9ca3af; margin-bottom: 6px;'>Modelos instalados no Ollama:</p>", unsafe_allow_html=True)
            for m in available_models:
                active_marker = " ⚡ *(em uso)*" if m == st.session_state.model_name else ""
                st.markdown(f"- `{m}`{active_marker}")
        else:
            st.warning("Nenhum modelo listado pelo Ollama local.", icon=":material/warning:")

        st.markdown("<hr style='margin: 12px 0; border: none; border-top: 1px solid rgba(255,255,255,0.08);'>", unsafe_allow_html=True)

        def set_custom_model():
            custom = st.session_state.custom_model_input.strip()
            if custom:
                st.session_state.model_name = custom
                st.rerun()

        st.text_input(
            "Digitar outro modelo manualmente:",
            key="custom_model_input",
            placeholder="ex: llama3, mistral, deepseek-r1:8b",
            on_change=set_custom_model,
            help="Pressione Enter após digitar para trocar o modelo"
        )
        st.info("Para baixar novos modelos, use no terminal: `ollama run <modelo>`", icon=":material/info:")
        
    st.button("Ajuda", icon=":material/help_outline:", use_container_width=True)

    # Developer Attribution
    st.markdown(
        """
        <div style='margin-top: 1.5rem; padding-top: 0.85rem; border-top: 1px solid rgba(255, 255, 255, 0.08); text-align: center;'>
            <p style='font-size: 0.75rem; color: #9ca3af; margin: 0 0 6px 0;'>
                Desenvolvido por <strong style="color: #f1f5f9;">Luciana Sampaio</strong>
            </p>
            <div style='display: flex; gap: 8px; justify-content: center; align-items: center;'>
                <a href="https://www.linkedin.com/in/luciana-sampaio/" target="_blank" style="display: inline-flex; align-items: center; gap: 5px; color: #a5b4fc; text-decoration: none; font-weight: 500; font-size: 0.78rem; padding: 4px 10px; border-radius: 8px; background: rgba(165, 180, 252, 0.06); border: 1px solid rgba(165, 180, 252, 0.15); transition: all 0.2s ease;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="#0A66C2"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                    LinkedIn
                </a>
                <a href="https://medium.com/@luciana.sampaio84" target="_blank" style="display: inline-flex; align-items: center; gap: 5px; color: #a5b4fc; text-decoration: none; font-weight: 500; font-size: 0.78rem; padding: 4px 10px; border-radius: 8px; background: rgba(165, 180, 252, 0.06); border: 1px solid rgba(165, 180, 252, 0.15); transition: all 0.2s ease;">
                    <svg xmlns="http://www.w3.org/2000/svg" width="13" height="13" viewBox="0 0 24 24" fill="#FFFFFF"><path d="M13.54 12a6.8 6.8 0 01-6.77 6.82A6.8 6.8 0 010 12a6.8 6.8 0 016.77-6.82A6.8 6.8 0 0113.54 12zM20.96 12c0 3.54-1.51 6.42-3.38 6.42-1.87 0-3.39-2.88-3.39-6.42s1.52-6.42 3.39-6.42 3.38 2.88 3.38 6.42M24 12c0 3.17-.53 5.75-1.19 5.75-.66 0-1.19-2.58-1.19-5.75s.53-5.75 1.19-5.75C23.47 6.25 24 8.83 24 12z"/></svg>
                    Medium
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# Top Bar
top_col1, top_col2 = st.columns([1.5, 1])
with top_col1:
    c_icon, c_sel = st.columns([0.14, 0.86])
    with c_icon:
        st.markdown("<div style='font-size: 1.35rem; padding-top: 3px;'>🤖</div>", unsafe_allow_html=True)
    with c_sel:
        def on_top_model_change():
            st.session_state.model_name = st.session_state.top_model_selector

        current_idx = model_options.index(st.session_state.model_name) if st.session_state.model_name in model_options else 0
        st.selectbox(
            "Modelo Ollama",
            options=model_options,
            index=current_idx,
            key="top_model_selector",
            on_change=on_top_model_change,
            label_visibility="collapsed",
            help="Selecione o modelo do Ollama para a conversa"
        )

with top_col2:
    if is_connected:
        st.markdown(
            f"""<div style='text-align: right; padding-top: 5px;'>
                <span class='status-badge' style='color: #4ade80;'>
                    <span class='status-dot online'></span> {status_text}
                </span>
            </div>""",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""<div style='text-align: right; padding-top: 5px;'>
                <span class='status-badge' style='color: #f87171;'>
                    <span class='status-dot offline'></span> {status_text}
                </span>
            </div>""",
            unsafe_allow_html=True
        )

st.markdown("<br>", unsafe_allow_html=True)

# Main Content Area - Splash Screen
if not st.session_state.messages:
    st.markdown(f"""
    <div style="text-align: center; margin-top: 1rem;">
        <div style="background-color: #21252b; border-radius: 12px; padding: 10px; display: inline-block; margin-bottom: 10px; border: 1px solid rgba(255,255,255,0.05);">
            <span style="font-size: 24px;">🤖</span>
        </div>
        <h1 class="main-title">Hermes AI Assistant</h1>
        <p style="color: #9ca3af; margin-top: 5px; font-size: 1rem; font-weight: 300;">Seu assistente de IA local<br>Privacidade, produtividade e inteligência com Ollama</p>
        <div style="margin-top: 8px;">
            <span style="background: rgba(165,180,252,0.08); border: 1px solid rgba(165,180,252,0.2); border-radius: 20px; padding: 4px 14px; font-size: 0.8rem; color: #c7d2fe;">
                ⚡ Modelo conectado: <b>{st.session_state.model_name}</b>
            </span>
        </div>
        <p style="font-size: 1.45rem; margin-top: 1.75rem; margin-bottom: 1.5rem; font-weight: 500; color: #f1f5f9; letter-spacing: -0.3px;">Olá, Luciana! O que vamos desenvolver hoje?</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="prompt-grid">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button(
            "**Desenvolvimento**\n\nPython, Spark e arquitetura",
            icon=":material/code:",
            key="btn_dev",
            use_container_width=True
        ):
            st.session_state.messages.append(
                HumanMessage(content="Como estruturar um projeto escalável em Python utilizando boas práticas de arquitetura e design patterns?")
            )
            st.rerun()

        if st.button(
            "**Inteligência artificial**\n\nLLMs, RAG e agentes",
            icon=":material/psychology:",
            key="btn_ai",
            use_container_width=True
        ):
            st.session_state.messages.append(
                HumanMessage(content="Explique como arquitetar um sistema de RAG (Retrieval-Augmented Generation) eficiente para produção.")
            )
            st.rerun()

    with col2:
        if st.button(
            "**Engenharia de dados**\n\nSQL, Databricks e pipelines",
            icon=":material/database:",
            key="btn_data",
            use_container_width=True
        ):
            st.session_state.messages.append(
                HumanMessage(content="Quais são as melhores práticas para otimizar pipelines de dados no Databricks utilizando PySpark e Delta Lake?")
            )
            st.rerun()

        if st.button(
            "**Análise de documentos**\n\nResumir e extrair informações",
            icon=":material/description:",
            key="btn_docs",
            use_container_width=True
        ):
            st.session_state.messages.append(
                HumanMessage(content="Como posso extrair informações estruturadas e resumir grandes volumes de documentos usando LLMs?")
            )
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align: center; margin-top: 2rem; margin-bottom: 1rem;">
            <span style="font-size: 0.8rem; color: #6b7280;">Desenvolvido por </span>
            <strong style="color: #cbd5e1; font-size: 0.82rem;">Luciana Sampaio</strong>
            <span style="color: #4b5563; margin: 0 6px;">•</span>
            <a href="https://www.linkedin.com/in/luciana-sampaio/" target="_blank" style="color: #a5b4fc; text-decoration: none; font-size: 0.82rem; font-weight: 500;">LinkedIn ↗</a>
            <span style="color: #4b5563; margin: 0 6px;">•</span>
            <a href="https://medium.com/@luciana.sampaio84" target="_blank" style="color: #a5b4fc; text-decoration: none; font-size: 0.82rem; font-weight: 500;">Medium ↗</a>
        </div>
        """,
        unsafe_allow_html=True
    )


def get_llm():
    return ChatOllama(model=st.session_state.model_name, temperature=0.7)

# Display existing messages as interactive Work Units
for idx, msg in enumerate(st.session_state.messages):
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            if st.session_state.get("editing_idx") == idx:
                with st.container(border=True):
                    st.markdown("**:material/edit: Editar pergunta e reenviar:**")
                    edit_input = st.text_area(
                        "Editar pergunta",
                        value=msg.content,
                        key=f"edit_field_{idx}",
                        label_visibility="collapsed",
                        height=100
                    )
                    col_save, col_cancel = st.columns([0.45, 0.55])
                    with col_save:
                        if st.button("Salvar e reenviar", icon=":material/send:", type="primary", key=f"save_edit_{idx}"):
                            if edit_input.strip():
                                st.session_state.messages = st.session_state.messages[:idx]
                                st.session_state.messages.append(HumanMessage(content=edit_input.strip()))
                                st.session_state.editing_idx = None
                                st.rerun()
                    with col_cancel:
                        if st.button("Cancelar", key=f"cancel_edit_{idx}"):
                            st.session_state.editing_idx = None
                            st.rerun()
            else:
                col_usr_text, col_usr_btn = st.columns([0.93, 0.07])
                with col_usr_text:
                    st.markdown(msg.content)
                with col_usr_btn:
                    if st.button("", icon=":material/edit:", key=f"btn_edit_{idx}", help="Editar e reenviar pergunta"):
                        st.session_state.editing_idx = idx
                        st.rerun()

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)
            
            # Interactive Action Bar / Work Unit
            st.markdown("<div style='margin-top: 10px;'></div>", unsafe_allow_html=True)
            col_act1, col_act2, col_act3, col_act4 = st.columns([1, 1.25, 1, 1.2])
            
            with col_act1:
                with st.popover("Copiar", icon=":material/content_copy:", help="Copiar resposta ou código"):
                    st.markdown("**Copiar Resposta:**")
                    st.caption("Clique no ícone de cópia no canto superior direito do bloco:")
                    st.code(msg.content, language="markdown")
            
            with col_act2:
                with st.popover("Regenerar", icon=":material/refresh:", help="Regenerar esta resposta"):
                    st.markdown("**Regenerar com modelo:**")
                    regen_chosen = st.selectbox(
                        "Modelo para regenerar:",
                        options=model_options,
                        index=model_options.index(st.session_state.model_name) if st.session_state.model_name in model_options else 0,
                        key=f"regen_pick_{idx}"
                    )
                    if st.button("Regenerar agora", icon=":material/autorenew:", type="primary", key=f"do_regen_{idx}"):
                        st.session_state.model_name = regen_chosen
                        # Keep history up to this assistant message (excluding it)
                        st.session_state.messages = st.session_state.messages[:idx]
                        st.rerun()

            with col_act3:
                fb = st.feedback("thumbs", key=f"fb_msg_{idx}")
                if fb is not None:
                    if f"fb_done_{idx}" not in st.session_state:
                        st.session_state[f"fb_done_{idx}"] = fb
                        if fb == 1:
                            st.toast("Obrigado pelo feedback positivo! 👍", icon="⭐")
                        else:
                            st.toast("Feedback registrado! Vamos aprimorar as respostas. 👎", icon="📝")

            with col_act4:
                with st.popover("Documento", icon=":material/description:", help="Exportar ou salvar como nota"):
                    st.markdown("**Exportar ou Salvar:**")
                    st.download_button(
                        label="Baixar Markdown (.md)",
                        data=msg.content,
                        file_name=f"hermes_resposta_{idx}.md",
                        mime="text/markdown",
                        icon=":material/download:",
                        key=f"dl_md_{idx}"
                    )
                    st.download_button(
                        label="Baixar Texto (.txt)",
                        data=msg.content,
                        file_name=f"hermes_resposta_{idx}.txt",
                        mime="text/plain",
                        icon=":material/text_snippet:",
                        key=f"dl_txt_{idx}"
                    )
                    if st.button("Salvar no Caderno de Notas", icon=":material/bookmark_add:", key=f"save_as_note_{idx}"):
                        if "notes" not in st.session_state:
                            st.session_state.notes = []
                        preview = msg.content.strip().split("\n")[0].replace("#", "").strip()
                        if len(preview) > 35:
                            preview = preview[:35] + "..."
                        if not preview:
                            preview = f"Nota {len(st.session_state.notes) + 1}"
                        st.session_state.notes.append({
                            "title": preview,
                            "content": msg.content,
                            "model": st.session_state.model_name
                        })
                        st.toast(f"Nota salva no Caderno!", icon="📝")

# Chat input
prompt = st.chat_input("Como o Hermes pode te ajudar hoje?")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

# If the last message is from the user, generate response
if st.session_state.messages and isinstance(st.session_state.messages[-1], HumanMessage):
    with st.chat_message("assistant"):
        if not is_connected:
            st.error("O Ollama não está rodando no momento. Certifique-se de iniciá-lo no seu computador antes de enviar mensagens.", icon=":material/wifi_off:")
        else:
            try:
                llm = get_llm()

                def stream_response():
                    for chunk in llm.stream(st.session_state.messages):
                        if hasattr(chunk, "content") and chunk.content:
                            yield chunk.content

                response_text = st.write_stream(stream_response())
                st.session_state.messages.append(AIMessage(content=response_text))
                st.rerun()
            except Exception as e:
                st.error(f"Erro de conexão: Não foi possível se conectar ao Ollama. Verifique se ele está rodando. Detalhes: {e}")
