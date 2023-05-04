#creando una funcion simple
def saludar():
    print("Hola Lucas, mi maestro, como andas?")

#ejecutando funcion simple
saludar()

# creando una funcion que tenga parametro.
def saludar2(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == 'mujer'):
        adjetivo = 'reina'
    elif sexo == 'hombre':
        adjetivo = 'titan'
    else:
        adjetivo='amor'
    print("Hola", nombre, "mi", adjetivo, "como andas?")

saludar2("Dalto", "mujer")
saludar2("Camila", 'Hombre')
saludar2("fran", 'no binario')

#crear una funcion que retorne valor
def crear_random_password(num):
    chars ='abcdefghij'
    num_entero =str(num)
    num = int(num_entero[0])
    c1 = num-2
    c2 = num
    c3 = num -5
    password = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return (password, num)

#desempaquetando la funcion
password, num = crear_random_password(1)

#mostrando los resultados obtenidos y los datos utilizados para obtenerla.
frase = f"Tu nueva contraseña es: {password}"
print(frase);
frase = f"el numero utilizado para crearla es: {num}"
print(frase);