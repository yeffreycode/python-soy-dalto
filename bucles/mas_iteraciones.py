#creando las listas.
frutas = ['banana', 'manzana', 'ciruela','pera', 'naranja', 'granada', 'durazno']
cadena = 'Hola Dalto'
numeros = [1,2,3,4,5,6,7,8,9,10]
#evitando que se coma una manzana con la sentencia continue.
for fruta in frutas:
    if (fruta) == 'granada':
        continue
    print(f"Me voy a comer una {fruta}")


#evitar que el bucle se siga ejecutando con la sentencia break.(el else no se ejecuta tampoco)
for fruta in frutas:
    print(f"Me voy a comer una {fruta}")
    if (fruta) == 'pera':
        break
else:
    print("terminado")



#recorrer una cadena de texto
for letra in cadena:
    print(letra)

#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [2*num for num in numeros]
print(numeros_duplicados)