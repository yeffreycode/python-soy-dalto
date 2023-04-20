# creando un diccionario con dict()
diccionario = dict(nombre="Lucas", apellido="Dalto")
print(diccionario)  # {'nombre': 'Lucas', 'apellido': 'Dalto'} => otra forma de crear diccionario.

#creando diccionarion con fromkeys()
diccionario = dict.fromkeys(["nombre", "edad", "pais"])

print(diccionario)
print(diccionario["nombre"])