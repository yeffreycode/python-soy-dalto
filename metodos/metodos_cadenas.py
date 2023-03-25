cadena1 = "Hola soy Dalto"
cadena2 = "Bienvenido maquinola"

print(dir(cadena1))
print(dir(["hola"]))


#convierte a mayuscula
resultado1  = cadena1.upper()
print(resultado1)

#convierte a minuscula
resultado2 = cadena1.lower()
print(resultado2)

#convierte la primera letra a mayuscula
resultado3 = cadena1.capitalize()
print(resultado3)

#buscamos una cadena en otra cadena, si no hay conincidencias devuelve -1
resultado4 = cadena1.find("Hola")
print(resultado4)

#buscamos una cadena en otra cadena, si no hay conincidencias lanza una exepcion.
resultado5 = cadena1.index("l")
print(resultado5)

#si es numerico, devolvemos true, sino devolvemos false
resultado6 = cadena1.isnumeric()
print(resultado6)

#si es alfanumerico devolvemos true, sino devolvemos false, de a -z
resultado7 = cadena1.isalpha()
print(resultado7)

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincide con la cadena a buscar.

resultado8 = cadena1.count("a")
print(resultado8)

#contamos cuantos caracteres tiene una cadena, len no es un metodo, es funcion.
resultado9 = len(cadena1)
print(resultado9)


#verificamos si una cadena empienza con otra cadena dadaa, si es asi devuelve true
resultado10 = cadena1.startswith("Hola")
print(resultado10)

#verificamos si una cadena termina con otra cadena dadaa, si es asi devuelve true
resultado11 = cadena1.endswith("a")
print(resultado11)

#si el valor 1, se encuentra en la cadena, reemplza el valor 1 de la misma por el valor 2
resultado12 = cadena1.replace("la", "lu");
print(resultado12)

#separar cadenas con la cadena q lo pasemos, devuelve una lista

resultado13 = cadena1.split(",")#separamos la cadena por cada coma que haya



