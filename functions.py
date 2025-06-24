# main_app.py
from typing import List, Dict, Any, Optional
import random
import string
from datetime import datetime, timedelta

# Importa as funções status_pedido e nova_reclamacao do arquivo database.py
from database import status_pedido, nova_reclamacao

def atualizar_status_pedido(numeroPedido: Optional[str] = None, cpf: Optional[str] = None) -> List[Dict[str, Any]]:
  """
  Recebe o número do pedido ou o CPF e, se este bater com o database,
  retorna o dicionário(s) equivalente(s) com o status.

  Args:
      numeroPedido (Optional[str]): O número/ID do pedido a ser buscado.
      cpf (Optional[str]): O CPF do cliente para buscar os pedidos.

  Returns:
      List[Dict[str, Any]]: Uma lista de dicionários dos pedidos encontrados.
                            Retorna uma lista vazia se nenhum pedido for encontrado
                            ou a entrada for inválida.
  """
  # Validar que pelo menos um parâmetro foi fornecido
  if not numeroPedido and not cpf:
    print("Erro: Por favor, forneça o número do pedido ou o CPF para consultar o status.")
    return []

  # Lidar com o caso de ambos os parâmetros serem fornecidos
  if numeroPedido and cpf:
    print("Aviso: Ambos 'numeroPedido' e 'cpf' foram fornecidos. Priorizando a busca por 'numeroPedido'.")
    # A função status_pedido espera 'id_pedido' para o ID
    return status_pedido(id_pedido=numeroPedido)
  elif numeroPedido:
    # A função status_pedido espera 'id_pedido' para o ID
    return status_pedido(id_pedido=numeroPedido)
  else: # Se não for numeroPedido, deve ser CPF (já validado que pelo menos um existe)
    # A função status_pedido espera 'cpf' para o CPF
    return status_pedido(cpf=cpf)

def registrar_reclamacao(id_pedido: Optional[str], cpf: str, reclamacao_texto: str) -> Optional[Dict[str, Any]]:
   """
    Registra uma nova reclamação no sistema.

    Args:
        id_pedido (Optional[str]): O ID do pedido ao qual a reclamação está associada.
                                    Pode ser None se a reclamação não estiver ligada a um pedido específico.
        cpf (str): O CPF do cliente que está fazendo a reclamação.
        reclamacao_texto (str): O texto descritivo da reclamação.

    Returns:
        Optional[Dict[str, Any]]: O dicionário da reclamação recém-criada se for bem-sucedida,
                                  ou None se a reclamação não puder ser registrada (ex: CPF não encontrado
                                  ou dados de entrada inválidos).
   """
   if not cpf or not reclamacao_texto: # id_pedido can be None, so we only check cpf and reclamacao_texto
     print("Erro: É preciso informar o CPF e o texto da reclamação para registrar.")
     return None # Return None to match the type hint
   else:
    return nova_reclamacao(id_pedido=id_pedido, cpf=cpf, reclamacao_texto=reclamacao_texto)
   
def gerar_cupom_desconto(
    prefixo: str = "DESC",
    comprimento_codigo: int = 8,
    valor_desconto: float = 0.0,
    tipo_desconto: str = "percentual", # 'percentual' ou 'fixo'
    dias_validade: Optional[int] = None
) -> Dict[str, Any]:
    """
    Gera um cupom de desconto com um código único e detalhes configuráveis.

    Args:
        prefixo (str): Prefixo para o código do cupom (ex: "BLACKFRIDAY", "NATAL").
                       Padrão: "DESC".
        comprimento_codigo (int): Comprimento do segmento alfanumérico do código.
                                  Padrão: 8.
        valor_desconto (float): O valor do desconto a ser aplicado (ex: 10.0 para 10% ou R$10).
                                Padrão: 0.0.
        tipo_desconto (str): Tipo de desconto ('percentual' ou 'fixo').
                             Padrão: 'percentual'.
        dias_validade (Optional[int]): Número de dias a partir de hoje para o cupom ser válido.
                                       Se None, o cupom não terá data de expiração.

    Returns:
        Dict[str, Any]: Um dicionário contendo os detalhes do cupom gerado,
                        ou um dicionário vazio se houver um erro.
    """
    if not isinstance(comprimento_codigo, int) or comprimento_codigo <= 0:
        print("Erro: O comprimento do código deve ser um número inteiro positivo.")
        return {}

    if tipo_desconto not in ["percentual", "fixo"]:
        print("Erro: O tipo de desconto deve ser 'percentual' ou 'fixo'.")
        return {}

    # Gerar o segmento alfanumérico aleatório
    caracteres = string.ascii_uppercase + string.digits
    codigo_aleatorio = ''.join(random.choice(caracteres) for _ in range(comprimento_codigo))

    # Combinar prefixo e código aleatório
    codigo_cupom = f"{prefixo}-{codigo_aleatorio}"

    data_expiracao: Optional[str] = None
    if dias_validade is not None and dias_validade > 0:
        expiracao = datetime.now() + timedelta(days=dias_validade)
        data_expiracao = expiracao.strftime("%Y-%m-%d") # Formato AAAA-MM-DD

    cupom = {
        "codigo": codigo_cupom,
        "valor": valor_desconto,
        "tipo": tipo_desconto,
        "data_geracao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data_expiracao": data_expiracao,
        "ativo": True,
        "usos_restantes": 1 # Pode ser alterado para um número maior para múltiplos usos
    }

    print(f"Cupom gerado com sucesso: {codigo_cupom}")
    return cupom

def obter_politica_ecomerce_generica() -> Dict[str, Any]:
    """
    Devolve um dicionário contendo uma política genérica de e-commerce,
    abrangendo termos de uso, política de privacidade, política de troca e devolução,
    e política de frete.

    Returns:
        Dict[str, Any]: Um dicionário com os detalhes da política.
    """

    politica: Dict[str, Any] = {
        "titulo_geral": "Políticas do E-commerce",
        "introducao": "Bem-vindo às nossas políticas! Elas foram criadas para garantir uma experiência de compra transparente e segura para todos os nossos clientes.",
        "secoes": [
            {
                "titulo": "1. Termos e Condições de Uso",
                "id_secao": "termos_condicoes",
                "descricao": "Ao acessar e utilizar nosso website/aplicativo, você concorda com os termos e condições aqui descritos. Reservamo-nos o direito de modificar estas políticas a qualquer momento, sem aviso prévio. É sua responsabilidade revisar periodicamente as atualizações.",
                "detalhes": [
                    "**Aceitação:** O uso contínuo de nossos serviços implica na aceitação total destes termos.",
                    "**Registro de Conta:** Ao criar uma conta, você se responsabiliza pela veracidade das informações fornecidas e pela segurança de sua senha.",
                    "**Propriedade Intelectual:** Todo o conteúdo do site (textos, imagens, logotipos) é de nossa propriedade ou licenciado para nós, e não pode ser reproduzido sem autorização expressa.",
                    "**Conduta do Usuário:** É proibido o uso de nossos serviços para fins ilegais ou que violem os direitos de terceiros."
                ]
            },
            {
                "titulo": "2. Política de Privacidade",
                "id_secao": "politica_privacidade",
                "descricao": "Sua privacidade é muito importante para nós. Coletamos e usamos suas informações pessoais apenas para fornecer e melhorar nossos serviços, sempre em conformidade com a Lei Geral de Proteção de Dados (LGPD).",
                "detalhes": [
                    "**Dados Coletados:** Nome, CPF, endereço, e-mail, telefone e dados de pagamento. Coletamos informações de navegação para melhorar sua experiência.",
                    "**Uso dos Dados:** Seus dados são usados para processar pedidos, entregar produtos, personalizar sua experiência e enviar comunicações relevantes (com sua permissão).",
                    "**Compartilhamento de Dados:** Não compartilhamos suas informações pessoais com terceiros não relacionados, exceto quando necessário para processamento de pagamentos, entrega (transportadoras) ou exigência legal.",
                    "**Segurança:** Implementamos medidas de segurança para proteger seus dados contra acesso não autorizado."
                ]
            },
            {
                "titulo": "3. Política de Troca e Devolução",
                "id_secao": "politica_troca_devolucao",
                "descricao": "Nosso objetivo é sua satisfação. Caso precise trocar ou devolver um produto, siga as orientações abaixo, respeitando o Código de Defesa do Consumidor.",
                "detalhes": [
                    "**Direito de Arrependimento:** Você tem até **7 (sete) dias corridos** a partir do recebimento do produto para desistir da compra. O produto deve estar em sua embalagem original, sem sinais de uso e com todos os acessórios e manuais.",
                    "**Produto com Defeito:** Se o produto apresentar defeito em até **90 (noventa) dias corridos** após o recebimento, entre em contato conosco para análise. Faremos a troca ou o reparo, conforme o caso.",
                    "**Condições para Troca/Devolução:** O produto deve estar acompanhado da nota fiscal e ser enviado na embalagem original.",
                    "**Procedimento:** Entre em contato com nosso Serviço de Atendimento ao Cliente (SAC) para iniciar o processo. Você receberá as instruções de como enviar o produto de volta.",
                    "**Reembolso/Estorno:** Após a análise e aprovação da devolução, o reembolso será processado de acordo com a forma de pagamento original."
                ]
            },
            {
                "titulo": "4. Política de Frete e Entrega",
                "id_secao": "politica_frete_entrega",
                "descricao": "Trabalhamos para que seu pedido chegue até você da forma mais rápida e segura possível.",
                "detalhes": [
                    "**Prazos de Entrega:** Os prazos são calculados com base no CEP de destino e na disponibilidade do produto. Você poderá visualizar o prazo estimado no carrinho de compras.",
                    "**Valor do Frete:** O valor do frete varia de acordo com o peso, dimensões do produto e localidade de entrega. Pode haver promoções de frete grátis em períodos específicos.",
                    "**Rastreamento:** Após o envio do pedido, você receberá um código de rastreamento para acompanhar a entrega.",
                    "**Áreas de Entrega:** Realizamos entregas em todo o território nacional. Em algumas regiões com restrição de entrega, o pedido poderá ser direcionado para retirada em uma agência dos Correios ou transportadora."
                ]
            }
        ],
        "contato": "Para qualquer dúvida sobre nossas políticas, entre em contato com nosso SAC."
    }
    return politica
