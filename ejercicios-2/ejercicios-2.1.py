#falto el profe y los pibes van a armar la clase.
#primero pedir el nombre y la edad de los companieros que vinieron hoy a clase


def obtener_companeros(cantidad):

    #creando la lista con los companeros
    companeros = []

    #ejecutando un for para pedir informacion de cada companero
    for i in range(cantidad):
        nombre = input("ingresa el nombre del companero: ");
        edad = int(input("ingresa la edad del companero: "))
        companero = (nombre,edad)

        #agregando la informacion a la lista
        companeros.append(companero)

    # ordenandolos de menor a maor segun su edad
    companeros.sort(key=lambda x:x[1])

    #companeros[x] devuelve una tupla con (nombre, edad) y despues accedemos al nombre
    # para definir al asistente y profesor
    asistente = companeros[0][0]
    profesor = companeros[-1][0]

    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion
asistente, profesor =obtener_companeros(3)

#mostrando el resultado
print(f"el profesor es: {profesor} y su asistente e {asistente}")