from pymongo import MongoClient

# Conexão com o banco de dados MongoDB
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["loja"]
colecao = db["produtos"]

# Produtos com preço entre 50 e 100
produtos_50_100 = colecao.find({"preco": {"$gte": 50, "$lte": 100}})
print("\nProdutos com preço entre 50 e 100:")
for produto in produtos_50_100:
    print(produto)

# Produtos cujo nome começa com "C"
produtos_com_C = colecao.find({"nome": {"$regex": "^C"}})
print("\nProdutos cujo nome começa com 'C':")
for produto in produtos_com_C:
    print(produto)

# Produtos ordenados por preço em ordem decrescente
produtos_ordenados = colecao.find().sort("preco", -1)
print("\nProdutos ordenados por preço em ordem decrescente:")
for produto in produtos_ordenados:
    print(produto)

cliente.close()
