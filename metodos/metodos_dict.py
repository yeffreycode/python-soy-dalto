diccionario = {
    "nombre": "Lucas",
    "apellido": "dalto",
    "subs": 1000000
}

# keys() => devuelve las claves (tambien nos sirver para iterar)
claves = diccionario.keys(); 
print(claves);


# obteniendo un elemento un elemento con get() si no encuentra nada el programa continua
valor_de_nombre = diccionario.get("nombre");# diccionario["key"] devuelve el valor que tiene esa clave en el diccionario
print(valor_de_nombre);

# eleiminando un elemento de un diccionario
diccionario.pop("nombre", "subs"); #recive mas de un parametro
print(diccionario);

#obtenido un elemento dict_items iterable
diccionario_iterable = diccionario.items();
print(diccionario_iterable);

#eliminando todo del diccionario
diccionario.clear()
print(diccionario);