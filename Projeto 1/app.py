from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)

# Conexão com o MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["loja"]
colecao = db["produtos"]

# Rota principal para exibir o formulário de inserção
@app.route("/", methods=["GET", "POST"])
def inserir_produto():
    if request.method == "POST":
        nome = request.form["nome"]
        preco = float(request.form["preco"])
        estoque = int(request.form["estoque"])

        produto = {
            "nome": nome,
            "preco": preco,
            "estoque": estoque
        }

        # Inserir na coleção
        resultado = colecao.insert_one(produto)
        print(f"Produto inserido com sucesso! ID: {resultado.inserted_id}")

        # Redirecionar para a página principal após a inserção
        return redirect(url_for("inserir_produto"))

    # Se o método for GET, renderizar o formulário HTML
    return render_template("inserir_produto.html")

if __name__ == "__main__":
    app.run(debug=True)
