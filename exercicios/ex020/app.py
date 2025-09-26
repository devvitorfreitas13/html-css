from flask import Flask, request, render_template_string

app = Flask(__name__)

html = open("index.html").read()

@app.route('/')
def index():
    return html

@app.route('/converter', methods=['POST'])
def converter():
    valor = float(request.form['valor'])
    tipo = request.form['tipo']
    
    if tipo == 'c_para_f':
        resultado = (valor * 9/5) + 32
        resposta = f"{valor}°C = {resultado:.2f}°F"
    else:
        resultado = (valor - 32) * 5/9
        resposta = f"{valor}°F = {resultado:.2f}°C"

    return render_template_string(html + f"<div class='resultado'><h2>Resultado: {resposta}</h2></div>")

if __name__ == '__main__':
    app.run(debug=True)
