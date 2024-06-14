from pymongo import MongoClient

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

# Função principal
def main():
    # Conexão com o MongoDB
    cliente = MongoClient("mongodb://localhost:27017/")
    db = cliente["loja"]
    colecao = db["produtos"]

    # Loop para inserir produtos
    while True:
        inserir_produto(colecao)
        continuar = input("Deseja inserir outro produto? (s/n): ")
        if continuar.lower() != 's':
            break

    # Fechar conexão com o MongoDB
    cliente.close()
    print("\nConexão com MongoDB fechada.")

if __name__ == "__main__":
    main()
