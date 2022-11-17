from app import create_app
from app.migrate import init_db
from flask import render_template

app = create_app()

@app.route('/database')
def create_db():
    init_db()
    return "la base de datos ha sido creada"

@app.route('/')
def index():
    return "index"

@app.route('/todolist')
def prueba():
    lista = ['APEX', 'VALORANT', 'HALO']
    return render_template("prueba.html", x=lista)


if __name__ == "__main__":
    app.run(debug=True, port=5000)

