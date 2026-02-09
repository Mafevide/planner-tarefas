from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tarefas = [
    {"titulo": "Estudar Python", "status": "inicial"},
    {"titulo": "Revisar HTML", "status": "inicial"}
]

@app.route("/")
def index():
    return render_template("tarefas.html", tarefas=tarefas)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = request.form["titulo"]

    tarefas.append({
        "titulo": titulo,
        "status": "inicial"
    })

    return redirect("/")

@app.route("/apagar/<int:index>", methods=["POST"])
def apagar(index):
    tarefas.pop(index)
    return redirect("/")


@app.route("/andamento/<int:index>", methods=["POST"])
def marcar_andamento(index):
    tarefas[index]["status"] = "andamento"
    return redirect("/")


@app.route("/concluir/<int:index>", methods=["POST"])
def marcar_concluida(index):
    tarefas[index]["status"] = "concluida"

    concluidas = [t for t in tarefas if t["status"] == "concluida"]

    # se passar de 5, remove a mais antiga
    if len(concluidas) > 5:
        for i, tarefa in enumerate(tarefas):
            if tarefa["status"] == "concluida":
                tarefas.pop(i)
                break

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
