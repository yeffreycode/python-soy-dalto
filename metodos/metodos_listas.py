#LIST: creando una lista con list()
lista = list(["hola", "dalto", 34]);
print(lista)

#LEN: funcion len: devuelve la cantidad de elementos de la lista.
cantidad_de_elementos= len(lista)
print(cantidad_de_elementos)

#APPEND: agregando un elemento a la lista a la misma lista
lista.append("JAJAJJAJ");
print(lista)

#INSERT: agregando un elemento a la lista en un indice especifico
lista.insert(2, "TOMA MAMA")
print(lista);

#EXTEND: agregando variaos elementos a una lista (pasando una lista)
lista.extend([False, 2030])
print(lista)

#POP: eliminando un elemento de la lista (por su indice)
lista.pop(0)# para eliminar el ultimo elemento de lista se hace con el indice -1, el -2 para eliminar el penultimo y asi sucesivamente
print(lista)


#REMOVE: removiendo un elemnto de la lista por su valor
lista.remove("TOMA MAMA")
print(lista)


#CLEAR: elimina todos los elemntos de la lista
#lista.clear()
print(lista)

lista_de_numeros = ([1,5,2,10,8])

#SORT: ordena los elementos de una lista
lista_de_numeros.sort() 
#lista_de_numeros.sort(reverse=true): para ordernar descendente.
print(lista_de_numeros)


#REVERSE: invierte los elementos de una lista. el metodo reverse no ordena la lista, solo lo revierte
lista_de_numeros.reverse()
print(lista_de_numeros)


#INDEX: verificando si un elemnto se encuentra en la lista 
elemento_encontrado = lista.index(10) # lanza error si no lo encuentra.
print(elemento_encontrado) 

#nota: en las tuplas son inmutables.
