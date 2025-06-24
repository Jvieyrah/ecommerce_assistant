from functions import atualizar_status_pedido, registrar_reclamacao, gerar_cupom_desconto, obter_politica_ecomerce_generica
import os
import gradio as gr
import google.generativeai as genai
from google.api_core.exceptions import InvalidArgument
import time

# --- Configuração da API Gemini ---
genai.configure(api_key=os.environ.get('GEMINI_API')) # Usar .get para evitar erro se a variável não estiver setada

# --- Regras de Negócio como Instrução do Sistema ---
# Este texto instruirá o modelo sobre seu papel e as funções que ele pode usar.
# A vírgula tripla permite strings multilinha.
SYSTEM_INSTRUCTIONS = """
Você é um assistente de e-commerce prestativo e amigável, focado em ajudar os clientes com suas compras.
Sua principal tarefa é entender a intenção do usuário e usar as ferramentas disponíveis para fornecer a melhor resposta ou ação.

Siga estas regras de negócio estritamente:

### 1. Entendimento da Intenção do Usuário
Priorize a identificação da intenção principal do usuário na mensagem:
* **Dúvida Geral:** Responder a perguntas sobre o e-commerce, produtos, funcionamento.
* **Consulta de Pedido:** Acompanhar status, detalhes, rastreamento de pedidos.
* **Oferta/Desconto:** Oferecer promoções e cupons.
* **Reclamação/Problema:** Registrar queixas sobre produtos, serviços ou entregas.
* **Saudação/Despedida:** Iniciar ou encerrar a conversa.
* **Feedback/Elogio:** Agradecer e reconhecer a satisfação.
* **Informações de Contato:** Fornecer canais para atendimento humano.

### 2. Fluxos de Atendimento e Uso das Ferramentas
* **Para Dúvida Geral:**
    * **Ação:** Use a ferramenta `obter_politica_ecomerce_generica` para buscar informações.
    * **Regra:** Se a dúvida não puder ser respondida com as políticas, ofereça transferência para atendimento humano ou indique canais de contato.
    * **Exemplo:** Usuário: "Como funciona a política de troca?". Você: "Nossa política de troca garante... [resposta da política]"
* **Para Consulta de Pedido:**
    * **Ação:** Solicite o número do pedido ou o CPF. Use a ferramenta `atualizar_status_pedido`.
    * **Regra:** Se ambos forem fornecidos, priorize o número do pedido. Se o pedido não for encontrado, peça para o usuário verificar os dados.
    * **Exemplo:** Usuário: "Qual o status do meu pedido 001?". Você: "Seu pedido PED001 está em trânsito."
* **Para Oferta/Desconto:**
    * **Ação:** Use a ferramenta `gerar_cupom_desconto`.
    * **Parâmetros:** Gere um cupom com um prefixo relevante (e.g., "BEMVINDO", "CHATBOT"), valor (e.g., 10.0 para percentual, 50.0 para fixo) e validade (e.g., 7 dias). Escolha o tipo "percentual" ou "fixo" conforme a situação.
    * **Retorno:** Apresente o código do cupom, valor/percentual e validade de forma clara.
    * **Exemplo:** Usuário: "Tem algum desconto?". Você: "Claro! Use o cupom CHATBOT-XYZ123 para 10% de desconto..."
* **Para Reclamação/Problema:**
    * **Ação:** Solicite o CPF do cliente, o ID do pedido (se aplicável, mas opcional) e a descrição detalhada. Use a ferramenta `registrar_reclamacao`.
    * **Confirmação:** Confirme o registro e informe sobre os próximos passos.
    * **Exemplo:** Usuário: "Quero fazer uma reclamação, meu produto veio quebrado." Você: "Sinto muito. Por favor, me informe seu CPF, ID do pedido (se tiver) e o problema..."

### 3. Gerenciamento de Contexto e Solicitação de Informações
* **Regra:** Se o usuário iniciar um fluxo mas não fornecer todas as informações, solicite a informação faltante.
* **Regra:** Tente manter o contexto da conversa.

### 4. Tratamento de Erros e Inputs Inválidos
* **Regra:** Se não entender a intenção ou o input for inválido, informe o erro de forma amigável e ofereça opções de ajuda.
* **Regra:** Se a dificuldade persistir, sugira transferência para um atendente.

### 5. Transferência para Atendimento Humano
* **Regra:** Se o usuário solicitar explicitamente ("falar com atendente") ou a questão for muito complexa, forneça canais de contato humano (telefone, e-mail, horário de atendimento).

### 6. Linguagem e Tom
* **Regra:** Mantenha um tom amigável, prestativo e profissional.
* **Regra:** Use linguagem clara, concisa e evite jargões técnicos.

### 7. Saudação e Despedida
* **Regra:** Inicie com uma saudação e opções de ajuda.
* **Regra:** Finalize agradecendo e oferecendo ajuda futura.
"""

# --- Inicialização do Modelo Gemini e Sessão de Chat ---
# O modelo será inicializado com as ferramentas e as instruções do sistema.
magical_if = genai.GenerativeModel(
    "gemini-1.5-flash",
    generation_config={"temperature": 0.5},
    tools=[atualizar_status_pedido, registrar_reclamacao, gerar_cupom_desconto, obter_politica_ecomerce_generica],
    system_instruction=SYSTEM_INSTRUCTIONS # As regras de negócio aqui!
)

# A sessão de chat deve ser iniciada UMA VEZ para manter o contexto.
# Gradio lida com o estado da conversa (_history), mas a sessão de chat do Gemini
# é crucial para que ele "lembre" das interações e use as ferramentas corretamente.
# No Gradio, '_history' contém as mensagens anteriores, mas para o modelo Gemini,
# precisamos passá-las na sessão de chat ou ao chamar generate_content.
# Para manter a simplicidade e focar na correção do erro, vamos iniciar o chat aqui.
# Em um ambiente de produção real, você precisaria gerenciar o estado da sessão de chat
# por usuário (e.g., em um banco de dados ou cache).

# Para o Gradio ChatInterface, a função `fn` é chamada para cada nova mensagem.
# A sessão de chat deve ser inicializada ou passada de forma que mantenha o contexto.
# Uma forma simples para demos com Gradio é re-criar a sessão com o histórico.
# No entanto, para o uso correto das ferramentas, o `magical_if.start_chat()` é o ideal.

# Vamos ajustar `gradio_wrapper` para gerenciar a sessão de chat.
# O `_history` do Gradio já nos dá o histórico da conversa.
# Vamos usá-lo para alimentar a sessão de chat do Gemini.

def gradio_wrapper(message: dict[str, any], history: list[list[str]]) -> str:
    # `history` do Gradio é uma lista de tuplas/listas [user_msg, bot_msg]
    # Precisamos convertê-lo para o formato de mensagens do Gemini.
    gemini_history = []
    for user_msg, bot_msg in history:
        gemini_history.append({"role": "user", "parts": [user_msg]})
        gemini_history.append({"role": "model", "parts": [bot_msg]})

    # Inicia uma nova sessão de chat com o histórico, permitindo ao modelo "lembrar"
    chat_session = magical_if.start_chat(history=gemini_history)

    user_input_content = assemble_prompt(message)

    try:
        # Envia a mensagem do usuário para o modelo Gemini usando a sessão de chat
        response = chat_session.send_message(user_input_content)
        return response.text
    except InvalidArgument as e:
        # Se houver um erro de argumento inválido (ex: arquivo não suportado)
        return (
            f"Sinto muito, houve um problema com o arquivo que você enviou. "
            f"Eu só consigo processar alguns tipos de arquivos, como texto ou imagens (JPG, PNG). "
            f"Por favor, tente enviar um arquivo diferente ou descreva sua solicitação em texto."
        )
    except Exception as e:
        # Captura outros erros inesperados
        print(f"Ocorreu um erro inesperado: {e}")
        return "Desculpe, ocorreu um erro inesperado. Por favor, tente novamente mais tarde ou entre em contato com nosso suporte."

# --- Funções Auxiliares (mantidas como estão) ---
def assemble_prompt(message):
   prompt = [message["text"]]
   uploaded_files = upload_files(message)
   prompt.extend(uploaded_files)
   return prompt

def upload_files(message):
    uploaded_files = []
    if message["files"]:
        print(f"Detectados {len(message['files'])} arquivos para upload.") # Log para depuração
        for file_gradio_data in message["files"]:
            try:
                print(f"Tentando fazer upload de: {file_gradio_data['path']}")
                uploaded_file = genai.upload_file(file_gradio_data["path"])
                # Esperar o upload e processamento
                max_retries = 10
                retry_count = 0
                while uploaded_file.state.name == "PROCESSING" and retry_count < max_retries:
                    print(f"Arquivo {uploaded_file.name} ainda em processamento... Tentativa {retry_count+1}")
                    time.sleep(2) # Espera menos tempo para uploads rápidos
                    uploaded_file = genai.get_file(uploaded_file.name)
                    retry_count += 1
                if uploaded_file.state.name == "PROCESSING":
                    print(f"Erro: Arquivo {uploaded_file.name} ainda em processamento após {max_retries} tentativas. Pulando.")
                    continue # Pula este arquivo se não processou a tempo
                uploaded_files.append(uploaded_file)
                print(f"Upload de {uploaded_file.name} concluído.")
            except Exception as e:
                print(f"Erro ao fazer upload do arquivo {file_gradio_data['path']}: {e}")
                # Decide se você quer que o erro pare o processo ou apenas pule o arquivo
                continue
    return uploaded_files


# --- Interface Gradio ---
iface = gr.ChatInterface(
    fn=gradio_wrapper,
    title="Assistente Virtual da Loja",
    multimodal=True,
    theme="soft" # Um tema mais suave
)

# --- Lançamento do Gradio ---
if __name__ == "__main__":
    iface.launch()