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

# Função principal
def main():
    # Conexão com o MongoDB
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["loja"]
    colecao = db["produtos"]

    # Criar índice no campo "nome" ao iniciar o programa
    try:
        colecao.create_index([("nome", ASCENDING)], unique=True)
        print("\nÍndice criado com sucesso no campo 'nome'.")
    except pymongo.errors.OperationFailure as e:
        print(f"\nErro ao criar índice: {e}")

    # Loop para interação com o usuário
    while True:
        print("\nEscolha uma opção:")
        print("1. Inserir novo produto")
        print("2. Atualizar preço de um produto")
        print("3. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            inserir_produto(colecao)
        elif opcao == "2":
            atualizar_preco(colecao)
        elif opcao == "3":
            break
        else:
            print("\nOpção inválida. Por favor, digite 1, 2 ou 3.\n")

    # Fechar conexão com o MongoDB
    cliente.close()
    print("\nConexão com MongoDB fechada.")

if __name__ == "__main__":
    main()
