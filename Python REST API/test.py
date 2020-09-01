import requests

BASE = "http://127.0.0.1:5000/"

data = [{"id": 1, "nome": "joão", "telefone": "8198257829", "CPF": "06071925428"}]

for i in range(len(data)):
    response = requests.put(BASE + "Pessoa/" + str(i), data[i])
    print(response.json())

response = requests.get(BASE + "Pessoa/2")
print(response.json())
