from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Ruta principal
@app.route("/", methods=["GET", "POST"])
def home():
    books = []
    total = 0
    query = ""

    if request.method == "POST":
        query = request.form.get("search")
        if query:
            # Usamos la API de OpenLibrary
            url = f"https://openlibrary.org/search.json?q={query}"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                total = data.get("numFound", 0)
                books = data.get("docs", [])[:10]  # solo primeros 10 resultados
    return render_template("index.html", books=books, total=total, query=query)

if __name__ == "__main__":
    app.run(debug=True)
