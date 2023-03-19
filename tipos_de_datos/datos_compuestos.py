# listas: conjuntos de datos en python
#tuplas: en lugar de usar corchetes usa parentesis, la tupla no se puede modificar.
#conjunto: son elementos desordenados y que pueden cambiar (no se puede modificar elementos, no se pueden repetir los datos, para acceder a los datos de un conjunto se hace con bucles porque con indices no se puede acceder)
#diccionarios: es igual a los json de js. key: value, comas = cantidad de elementos menos 1



#Creando una lista (se pueden modificar)
lista = ["Lucas Dalto", "Soy Dalto", True, 1.85]
print(lista)

print(lista[0]) #leer el elemento de una lista por indice.


#Creando una tipla (no se puede modificar)
tupla = ("Lucas Dalto", "Soy Dalto", True, 1.85)

#esto no es validido
#tupla[3] = "Maquinola"

#Creando un conjunto (set)

conjunto = {"Lucas Dalto", "Soy Dalto", True, 1,85}

conjunto = {"jajaj maquinola te jodi"}

#no podemos acceder por el indice al elemnto del conjunto.
#print(conjunto[1]) -> no puede acceder al elemento


#Creando un diccionario
diccionario = {
        'nombre': "Lucas Dalto",
        'canal': "Soy Dalto",
        'esta_emocionado': True,
        'altura': 1.85
        }

print(diccionario['nombre'])
