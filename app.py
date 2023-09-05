from flask import Flask, render_template


app = Flask("Meu App")

posts = [
    {
        "titulo":"minha primeira postagem",
        "texto":"teste"
    },
    {
        "titulo":"minha segunda postagem",
        "texto":" outro teste" 
    },


]

@app.route('/')
def exibir_entradas():
    entradas = posts #mock das postagens 
    return render_template('exibir_entradas.html', entradas=entradas)