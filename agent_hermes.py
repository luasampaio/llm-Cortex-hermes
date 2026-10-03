import requests
import json
import sys

class HermesAgent:
    """
    Agente Hermes para interagir com modelos locais via Ollama.
    Mantém histórico de conversas e suporta streaming de respostas.
    """
    def __init__(self, model="openhermes", host="http://localhost:11434"):
        self.model = model
        self.host = host
        self.url = f"{self.host}/api/chat"
        self.history = []

    def clear_history(self):
        """Limpa o histórico da conversa atual."""
        self.history = []

    def add_system_prompt(self, prompt):
        """Adiciona um prompt de sistema ao início da conversa."""
        self.history.append({"role": "system", "content": prompt})

    def chat(self, user_message, stream=True):
        """
        Envia uma mensagem do usuário e recebe a resposta do agente.
        Por padrão, faz o streaming da resposta no terminal.
        """
        self.history.append({"role": "user", "content": user_message})
        
        payload = {
            "model": self.model,
            "messages": self.history,
            "stream": stream
        }
        
        headers = {"Content-Type": "application/json"}
        
        full_response = ""
        
        try:
            if stream:
                response = requests.post(self.url, json=payload, headers=headers, stream=True)
                response.raise_for_status()
                
                print("Hermes: ", end="", flush=True)
                for line in response.iter_lines():
                    if line:
                        chunk = json.loads(line.decode("utf-8"))
                        message_chunk = chunk.get("message", {}).get("content", "")
                        print(message_chunk, end="", flush=True)
                        full_response += message_chunk
                        
                        if chunk.get("done"):
                            break
                print() # Quebra de linha no final do streaming
            else:
                response = requests.post(self.url, json=payload, headers=headers)
                response.raise_for_status()
                
                result = response.json()
                full_response = result.get("message", {}).get("content", "")
                print(f"Hermes: {full_response}")
                
            # Adicionar a resposta final ao histórico
            self.history.append({"role": "assistant", "content": full_response})
            return full_response
            
        except requests.exceptions.RequestException as e:
            print(f"\n[Erro ao conectar com Ollama]: {e}")
            print("Certifique-se de que o Ollama está rodando e o modelo especificado está instalado.")
            self.history.pop() # Remove a mensagem do usuário já que falhou
            return None

if __name__ == "__main__":
    # IMPORTANTE: Altere 'openhermes' para o nome exato do modelo que você baixou no Ollama
    # Exemplos comuns: 'openhermes', 'nous-hermes2', 'llama3', etc.
    agent = HermesAgent(model="openhermes")
    
    print(f"Iniciando conexão com Hermes Agent (Ollama Local - Modelo: {agent.model})...")
    print("Digite 'sair' ou 'quit' para encerrar a conversa.\n")
    
    while True:
        try:
            user_input = input("Você: ")
            if user_input.lower() in ['sair', 'quit', 'exit']:
                break
                
            if not user_input.strip():
                continue
                
            agent.chat(user_input)
            print("-" * 50)
        except KeyboardInterrupt:
            print("\nSaindo...")
            break
        except EOFError:
            break
