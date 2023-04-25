diccionario = {
    "nombre": "Juan",
    "apellido": "Perez",
    "subs": 10000
}

#recorriendo diccionarios para obtener las claves
for key in diccionario:
    print(f"la clave es: {key}")

#recorriendo diccionarios para obtener las claves y valor
for datos in diccionario.items():
    key = datos[0]
    value = datos[1]
    print(f"la  clave es {key} y su valor es {value}")