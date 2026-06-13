import requests
import json

def chat_with_hermes(prompt, model="openhermes"):
    """
    Função para enviar um prompt para o modelo Hermes rodando localmente via Ollama.
    A porta padrão do Ollama é 11434.
    """
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        response.raise_for_status()
        
        result = response.json()
        return result.get("response", "")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com Ollama: {e}")
        print("Certifique-se de que o Ollama está rodando e o modelo especificado está instalado.")
        return None

if __name__ == "__main__":
    print("Iniciando conexão com Hermes Agent (Ollama Local)...")
    
    # Teste simples de conexão
    user_prompt = "Olá! Descreva brevemente quem é você."
    print(f"\nUser: {user_prompt}")
    
    # IMPORTANTE: Altere 'openhermes' para o nome exato do modelo que você baixou no Ollama
    # Exemplos comuns: 'openhermes', 'nous-hermes2', 'hermes2-pro', etc.
    resposta = chat_with_hermes(user_prompt, model="openhermes")
    
    if resposta:
        print("\nHermes:")
        print(resposta)
