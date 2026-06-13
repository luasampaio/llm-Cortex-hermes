import chainlit as cl
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

@cl.on_chat_start
async def on_chat_start():
    # 1. Instancia o modelo local do Ollama
    # Altere "openhermes" para o nome do modelo que você tem baixado
    model = ChatOllama(model="openhermes", temperature=0.7)
    
    # 2. Define o Prompt do Sistema e o espaço para o histórico
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Você é o Hermes, um assistente de IA amigável, inteligente e muito útil."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{question}")
    ])
    
    # 3. Cria a cadeia (Chain) do LangChain
    chain = prompt | model
    
    # 4. Inicializa a memória da sessão atual
    cl.user_session.set("history", ChatMessageHistory())
    
    # 5. Adiciona o gerenciamento automático de histórico ao chain
    runnable = RunnableWithMessageHistory(
        chain,
        lambda session_id: cl.user_session.get("history"),
        input_messages_key="question",
        history_messages_key="history"
    )
    
    cl.user_session.set("runnable", runnable)
    
    # Envia a mensagem de boas-vindas na tela
    await cl.Message(
        content="👋 **Olá! Eu sou o Hermes.** Estou rodando localmente via Ollama.\n\nComo posso te ajudar hoje?"
    ).send()

@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")
    
    # Cria uma mensagem vazia que será preenchida progressivamente (Streaming)
    msg = cl.Message(content="")
    await msg.send()

    # O astream permite que a resposta apareça letra por letra, igual ao ChatGPT
    async for chunk in runnable.astream(
        {"question": message.content},
        config={"configurable": {"session_id": "sessao_local"}}
    ):
        await msg.stream_token(chunk.content)
        
    # Atualiza a interface indicando que a mensagem terminou
    await msg.update()
