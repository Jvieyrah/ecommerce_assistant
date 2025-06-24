from ast import List
from typing import List, Dict, Any, Optional

pedidos: Dict[str, Dict[str, Any]] = {
    "pedido_001": {
        "id": "PED001",
        "cpf": "123.456.789-01",
        "endereco_entrega": {
            "rua": "Rua das Flores, 123",
            "cidade": "São Paulo",
            "estado": "SP",
            "cep": "01000-000"
        },
        "valor": 150.75,
        "status_pagamento": "aprovado",
        "status_entrega": "em_transito",
        "itens_comprados": [
            {"nome": "Camiseta Básica", "quantidade": 2, "preco_unitario": 45.00},
            {"nome": "Meia Esportiva (Par)", "quantidade": 3, "preco_unitario": 20.25}
        ]
    },
    "pedido_002": {
        "id": "PED002",
        "cpf": "987.654.321-02",
        "endereco_entrega": {
            "rua": "Avenida Brasil, 456",
            "cidade": "Rio de Janeiro",
            "estado": "RJ",
            "cep": "20000-000"
        },
        "valor": 59.90,
        "status_pagamento": "pendente",
        "status_entrega": "aguardando_envio",
        "itens_comprados": [
            {"nome": "Livro 'Aventura na Floresta'", "quantidade": 1, "preco_unitario": 59.90}
        ]
    },
    "pedido_003": {
        "id": "PED003",
        "cpf": "111.222.333-03",
        "endereco_entrega": {
            "rua": "Travessa da Paz, 789",
            "cidade": "Belo Horizonte",
            "estado": "MG",
            "cep": "30000-000"
        },
        "valor": 1200.00,
        "status_pagamento": "aprovado",
        "status_entrega": "entregue",
        "itens_comprados": [
            {"nome": "Notebook Gamer Xtreme", "quantidade": 1, "preco_unitario": 1100.00},
            {"nome": "Mouse sem Fio RGB", "quantidade": 1, "preco_unitario": 100.00}
        ]
    },
    "pedido_004": {
        "id": "PED004",
        "cpf": "444.555.666-04",
        "endereco_entrega": {
            "rua": "Alameda dos Anjos, 101",
            "cidade": "Curitiba",
            "estado": "PR",
            "cep": "80000-000"
        },
        "valor": 35.50,
        "status_pagamento": "rejeitado",
        "status_entrega": "cancelado",
        "itens_comprados": [
            {"nome": "Caneta Esferográfica (Pacote com 10)", "quantidade": 1, "preco_unitario": 15.00},
            {"nome": "Caderno Universitário", "quantidade": 2, "preco_unitario": 10.25}
        ]
    },
    "pedido_005": {
        "id": "PED005",
        "cpf": "777.888.999-05",
        "endereco_entrega": {
            "rua": "Praça da Liberdade, 202",
            "cidade": "Salvador",
            "estado": "BA",
            "cep": "40000-000"
        },
        "valor": 250.00,
        "status_pagamento": "aprovado",
        "status_entrega": "entregue",
        "itens_comprados": [
            {"nome": "Caixa de Som Bluetooth", "quantidade": 1, "preco_unitario": 180.00},
            {"nome": "Fone de Ouvido sem Fio", "quantidade": 1, "preco_unitario": 70.00}
        ]
    },
    "pedido_006": {
        "id": "PED006",
        "cpf": "333.222.111-06",
        "endereco_entrega": {
            "rua": "Rua do Sol, 303",
            "cidade": "Fortaleza",
            "estado": "CE",
            "cep": "60000-000"
        },
        "valor": 89.99,
        "status_pagamento": "aprovado",
        "status_entrega": "em_transito",
        "itens_comprados": [
            {"nome": "Mochila Escolar Reforçada", "quantidade": 1, "preco_unitario": 89.99}
        ]
    },
    "pedido_007": {
        "id": "PED007",
        "cpf": "666.555.444-07",
        "endereco_entrega": {
            "rua": "Avenida Principal, 404",
            "cidade": "Recife",
            "estado": "PE",
            "cep": "50000-000"
        },
        "valor": 750.20,
        "status_pagamento": "pendente",
        "status_entrega": "aguardando_envio",
        "itens_comprados": [
            {"nome": "Câmera Digital DSLR", "quantidade": 1, "preco_unitario": 600.00},
            {"nome": "Cartão de Memória 128GB", "quantidade": 1, "preco_unitario": 80.20},
            {"nome": "Tripé Profissional", "quantidade": 1, "preco_unitario": 70.00}
        ]
    },
    "pedido_008": {
        "id": "PED008",
        "cpf": "000.111.222-08",
        "endereco_entrega": {
            "rua": "Rua da Amizade, 505",
            "cidade": "Porto Alegre",
            "estado": "RS",
            "cep": "90000-000"
        },
        "valor": 12.99,
        "status_pagamento": "aprovado",
        "status_entrega": "entregue",
        "itens_comprados": [
            {"nome": "Barra de Cereal", "quantidade": 5, "preco_unitario": 2.50},
            {"nome": "Água Mineral (Garrafa 500ml)", "quantidade": 1, "preco_unitario": 0.49}
        ]
    },
    "pedido_009": {
        "id": "PED009",
        "cpf": "999.888.777-09",
        "endereco_entrega": {
            "rua": "Estrada Velha, 606",
            "cidade": "Brasília",
            "estado": "DF",
            "cep": "70000-000"
        },
        "valor": 3000.00,
        "status_pagamento": "aprovado",
        "status_entrega": "em_transito",
        "itens_comprados": [
            {"nome": "Smart TV 65 polegadas 4K", "quantidade": 1, "preco_unitario": 2800.00},
            {"nome": "Soundbar com Subwoofer", "quantidade": 1, "preco_unitario": 200.00}
        ]
    },
    "pedido_010": {
        "id": "PED010",
        "cpf": "121.314.151-10",
        "endereco_entrega": {
            "rua": "Rua Nova, 707",
            "cidade": "Campinas",
            "estado": "SP",
            "cep": "13000-000"
        },
        "valor": 45.00,
        "status_pagamento": "rejeitado",
        "status_entrega": "cancelado",
        "itens_comprados": [
            {"nome": "Copo Térmico 500ml", "quantidade": 1, "preco_unitario": 45.00}
        ]
    }
}

def status_pedido(id_pedido: Optional[str] = None, cpf: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    Retorna pedidos com base no ID do pedido ou no CPF do cliente.

    Args:
        id_pedido (Optional[str]): O ID específico do pedido.
        cpf (Optional[str]): O CPF do cliente para buscar todos os seus pedidos.

    Returns:
        List[Dict[str, Any]]: Uma lista de dicionários contendo os detalhes dos pedidos encontrados.
                              Retorna uma lista vazia se nenhum pedido for encontrado ou se a entrada for inválida.
    """
    pedidos_encontrados: List[Dict[str, Any]] = []

    if id_pedido and cpf:
        print("Aviso: Forneça apenas o ID do pedido OU o CPF, não ambos. Priorizando o ID do pedido.")
        # Se ambos são fornecidos, priorizamos o ID por ser mais específico.
        # Poderíamos também levantar um erro aqui, dependendo da regra de negócio.
        cpf = None

    if id_pedido:
        # Busca por ID de pedido
        # A chave do dicionário 'pedidos' já é um ID interno, então podemos buscar diretamente.
        # No entanto, o seu 'id' dentro do dicionário é o valor "PED00X", então precisamos iterar.
        for key, pedido_data in pedidos.items():
            if pedido_data["id"] == id_pedido:
                pedidos_encontrados.append(pedido_data)
                break  # Encontrou o pedido, não precisa procurar mais
        if not pedidos_encontrados:
            print(f"Pedido com ID '{id_pedido}' não encontrado.")
    elif cpf:
        # Busca por CPF
        for key, pedido_data in pedidos.items():
            if pedido_data["cpf"] == cpf:
                pedidos_encontrados.append(pedido_data)
        if not pedidos_encontrados:
            print(f"Nenhum pedido encontrado para o CPF '{cpf}'.")
    else:
        print("Erro: Por favor, forneça um 'id_pedido' ou um 'cpf'.")

    return pedidos_encontrados

reclamacoes: Dict[str, Dict[str, Any]] = {}

def nova_reclamacao(id_pedido: Optional[str], cpf: str, reclamacao_texto: str) -> Optional[Dict[str, Any]]:
    """
    Registra uma nova reclamação no sistema.

    Args:
        id_pedido (Optional[str]): O ID do pedido ao qual a reclamação está associada.
                                    Pode ser None se a reclamação não estiver ligada a um pedido específico.
        cpf (str): O CPF do cliente que está fazendo a reclamação.
        reclamacao_texto (str): O texto descritivo da reclamação.

    Returns:
        Optional[Dict[str, Any]]: O dicionário da reclamação recém-criada se for bem-sucedida,
                                  ou None se a reclamação não puder ser registrada (ex: CPF não encontrado).
    """
    if not cpf:
        print("Erro: O CPF é obrigatório para registrar uma reclamação.")
        return None

    # Optional: Validate if the CPF exists in any order before allowing a complaint
    # This depends on your business rules. For now, we'll allow it.
    cpf_exists = False
    for pedido_data in pedidos.values():
        if pedido_data["cpf"] == cpf:
            cpf_exists = True
            break
    
    if not cpf_exists:
        print(f"Aviso: CPF '{cpf}' não encontrado em nenhum pedido existente. Reclamação será registrada sem um pedido associado.")
        # Decide if you want to proceed or return None here

    # Generate a unique ID for the new complaint
    # Using the current length + 1 is a simple way, but in a real system,
    # you'd want a more robust ID generation (e.g., UUIDs or a counter).
    novo_id_reclamacao = f"REC{len(reclamacoes) + 1:03d}" # e.g., REC001, REC002

    nova_queixa = {
        "id_reclamacao": novo_id_reclamacao,
        "id_pedido_associado": id_pedido,
        "cpf_cliente": cpf,
        "data_reclamacao": "2025-06-23", # You might want to use datetime.now() here
        "descricao": reclamacao_texto,
        "status": "pendente" # Initial status for a new complaint
    }

    reclamacoes[novo_id_reclamacao] = nova_queixa
    print(f"Reclamação '{novo_id_reclamacao}' registrada com sucesso.")
    return nova_queixa


