nombre = "Lucas Dalto" #las variables se declaran y se definen.
print(nombre);

numero = 10
print(numero)

numero+=1
print(numero)

numero+=3
print(numero)

numero -= 5
print(numero)

# concatenar.
bienvenida = "hola " + nombre + ", como estas?"
print(bienvenida)

## la mejor forma de concatenar
edad = 20
bienvenida = f"hola {nombre} como estas?, tu edad es {edad} ?" # se llama los fString (toma un dato y lo convierte a texto
print(bienvenida)

variable_eliminada = "variable eliminada"
del variable_eliminada ## elimina la variable, ya no existe ahora.


#nota: python tiene operadores de pertencia como: in, not in.
# print("Lucas" in bienvenida)
# en python es preferible usar snake case por ejemplo snake_case

variable_snake_case = "variable con snake case"

#no es comun usar camel case
variableEnCamelCase = "variable con camel case"


