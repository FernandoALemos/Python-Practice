# importar librería json
import json
# ¿Qué es un json?

# creamos un json solamente debe usarse las comillas simples para los json

jsonPerson = {'name':'jose', 'apellidos':'Gonzalez', 'age':28, 'city':'Madrid'}
json_book = {'tittle':'StarFinder', 'type':'Basics rules', 'language':'Spanish', 'editorial':'Devir', 'price':'17000'}

jsonPersonString = json.dumps(jsonPerson)
json_book_string = json.dumps(json_book)

jsonPersonConver = json.loads(jsonPersonString)
json_book_conver = json.loads(json_book_string)

print(jsonPersonConver['name']+ " "+ jsonPersonConver['apellidos'])
print(json_book_conver['tittle']+ " "+ json_book_conver['type'])