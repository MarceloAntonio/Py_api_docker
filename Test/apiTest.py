import requests


IDpesquisa= input("Digite qual o id que deseja buscar: ")

try:

  url = f"http://127.0.0.1:5001/{IDpesquisa}"


  response = requests.get(url)
  dados = response.json()

  
  print(f"\nO ID selecionado é o: {IDpesquisa}")
  print(f"\nNome: {dados['nome']}")
  print(f"\nIdade: {dados['idade']}")

except (BaseException):
  print("ID não foi encontrado")