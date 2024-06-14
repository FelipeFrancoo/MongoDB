from pymongo import MongoClient, ASCENDING
import pymongo

# Função para inserir um novo produto no MongoDB
def inserir_produto(colecao):
    print("\nInserindo um novo produto:")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    estoque = int(input("Digite o estoque do produto: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    }

    # Inserir na coleção
    resultado = colecao.insert_one(produto)
    print(f"\nProduto inserido com sucesso! ID: {resultado.inserted_id}\n")

# Função para atualizar o preço de um produto
def atualizar_preco(colecao):
    nome_produto = input("Digite o nome do produto para atualizar o preço: ")
    novo_preco = float(input("Digite o novo preço do produto: "))

    # Verifica se o produto existe na coleção
    produto = colecao.find_one({"nome": nome_produto})
    if produto:
        # Atualiza o preço do produto
        colecao.update_one({"_id": produto["_id"]}, {"$set": {"preco": novo_preco}})
        print(f"\nPreço do produto '{nome_produto}' atualizado para R$ {novo_preco}\n")
    else:
        print(f"\nProduto '{nome_produto}' não encontrado.\n")

# Função para remover quantidade específica de um produto
def remover_produto(colecao):
    nome_produto = input("Digite o nome do produto para remover: ")
    quantidade = int(input(f"Digite a quantidade a ser removida (ou digite '0' para remover todo o estoque): "))

    # Verifica se o produto existe na coleção
    produto = colecao.find_one({"nome": nome_produto})
    if produto:
        estoque_atual = produto["estoque"]

        if quantidade <= estoque_atual:
            # Remove a quantidade especificada
            if quantidade > 0:
                novo_estoque = estoque_atual - quantidade
            else:
                novo_estoque = 0

            # Atualiza o estoque do produto
            colecao.update_one({"_id": produto["_id"]}, {"$set": {"estoque": novo_estoque}})
            print(f"\nQuantidade de {quantidade} unidades removida do produto '{nome_produto}'. Novo estoque: {novo_estoque}\n")
        else:
            print(f"\nNão há estoque suficiente do produto '{nome_produto}' para remover {quantidade} unidades.\n")
    else:
        print(f"\nProduto '{nome_produto}' não encontrado.\n")

# Função para criar índice no campo nome
def criar_indice(colecao):
    try:
        colecao.create_index([("nome", ASCENDING)], unique=True)
        print("\nÍndice criado com sucesso no campo 'nome'.")
    except pymongo.errors.OperationFailure as e:
        print(f"\nErro ao criar índice: {e}")

# Função principal
def main():
    # Conexão com o MongoDB
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["loja"]
    colecao = db["produtos"]

    # Criar índice no campo "nome" ao iniciar o programa
    criar_indice(colecao)

    # Loop para interação com o usuário
    while True:
        print("\nEscolha uma opção:")
        print("1. Inserir novo produto")
        print("2. Atualizar preço de um produto")
        print("3. Remover quantidade de um produto")
        print("4. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            inserir_produto(colecao)
        elif opcao == "2":
            atualizar_preco(colecao)
        elif opcao == "3":
            remover_produto(colecao)
        elif opcao == "4":
            break
        else:
            print("\nOpção inválida. Por favor, digite 1, 2, 3 ou 4.\n")

    # Fechar conexão com o MongoDB
    cliente.close()
    print("\nConexão com MongoDB fechada.")

if __name__ == "__main__":
    main()
