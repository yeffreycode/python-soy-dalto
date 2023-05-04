# #forma no optima de sumar valores
# def suma(lista):
#     numeros_sumados =0
#     for numero in lista:
#         numeros_sumados=numeros_sumados+numero
#     return numeros_sumados;

# resultado = suma([5,9])
# print(resultado)

#utilizando el operador * como argumento (*args)
def suma(nombre,*numeros):
   return f"{nombre} las suma de todos tus numeros es: {sum(numeros)}"

resultado = suma("lucas",4,5,6,9)
print(resultado)

# lo mismo que arriba pero utilizando el operador * como argumento (*args)
def suma_total(numeros):
   return sum([*numeros]);

resultado2 = suma_total([5,3,2,3,5,9])
print(resultado2);