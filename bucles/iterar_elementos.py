animales = ["gato", "perro", "loro", "cocodrilo"]
numeros = [10, 62, 12,72];

#recorriendo la lista de animales
for animal in animales:
    print(f'ahora la variable animal tiene el valor {animal}')
    print('-------------------')


# recorriendo la lista de numeros y multiplicandolos por 10
for numero in numeros:
    print(f'ahora la variable numero tiene el valor {numero*10}')
    print('-------------------')



for num in range(5,10):
    print(num)

for i in range(10):
    print(i)


# no funciona para conjuntos, porque no tiene indice
#forma no optima de recorrer una lista 
for num in range(len(numeros)):
    print(numeros[num])

#usando el for con else
for num in range(len(numeros)):
    print(numeros[num])
else:
    print('fin del ciclo for')

#funciona para listas, conjuntos y tuplas
#forma correcta de recorrer una lista con su indice.
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'indice es: {indice} y valor es: {valor}')

# recorriendo la lista de animales y numeros y multiplicandolos por 10
# zip permite combinar listas,  en este caso combinamos las listas animales y numeros, y tienen la misma cantidad de elementos
for numero, animal in zip(numeros, animales):
    print(f'ahora la variable numero tiene el valor {numero*10} y la variable animal tiene el valor {animal}')
    print('-------------------')