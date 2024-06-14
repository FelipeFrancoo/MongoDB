from pymongo import MongoClient

# Conexão com o banco de dados MongoDB
cliente = MongoClient("mongodb://localhost:27017/")
db = cliente["loja"]
colecao = db["produtos"]

# Recuperar todos os documentos
todos_os_produtos = colecao.find()
print("\nTodos os produtos:")
for produto in todos_os_produtos:
    print(produto)

# Recuperar produtos com preço menor que 50
produtos_baratos = colecao.find({"preco": {"$lt": 50}})
print("\nProdutos com preço menor que 50:")
for produto in produtos_baratos:
    print(produto)

# Recuperar produtos em estoque menor ou igual a 50
produtos_em_estoque = colecao.find({"estoque": {"$lte": 50}})
print("\nProdutos em estoque menor ou igual a 50:")
for produto in produtos_em_estoque:
    print(produto)

cliente.close()
