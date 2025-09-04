from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from conect import inserir_fabricantes

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/api/fabricantes', methods=['POST'])
def receber_dados():
    data = request.get_json()

    nome = data.get('nome')
    descricao = data.get('descricao')

    try:
        if not nome or not descricao:
            return jsonify({"erro": "Campos faltando"}), 400
        inserir_fabricantes(nome, descricao)
        return jsonify({"mensagem": "Inserido com sucesso"}), 201

    except Exception as e:
        return jsonify({"erro": str(e)}), 500  # <-- RETORNA ERRO REAL

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
