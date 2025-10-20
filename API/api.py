from flask import Flask, jsonify

app = Flask(__name__)

dadosAPI = [{
    "id":1,
    "nome":"celo",
    "idade": 19
  },
  {
    "id":2,
    "nome":"Nami",
    "idade": 18
  },
  {
    "id":3,
    "nome":"Bath",
    "idade": 44
  }
]


@app.route('/')
def home():
  return "Oláaaaa"

@app.route('/dados/api')
def get_dado():
  return jsonify(dadosAPI)


@app.route('/dados/api/<int:id>')
def pesquisa(id):
  item_encontrado = None
  for item in dadosAPI:
    if item['id'] == id:
      item_encontrado = item
      break
  if item_encontrado:
    return jsonify(item_encontrado)
  else:
    return jsonify({"erro": "ID não encontrado"}), 404



if __name__ == '__main__':
  app.run(host='0.0.0.0',port=5000,debug=True)