import math
#encontrando el numero mayor de una lista
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
mayor = max(lista_numeros)
print(mayor)

#contrando el numero mas bajo
menor = min(lista_numeros)
print(menor)

#redondeand a 6 decimales.
numero = round(1.2345038296,6)
print(numero);


#retorna False ->0, vacio, False, ninguno, return true si tiene datos no vacios.
resultado =bool(None)
print(resultado)


#retorna true si todos los datos son verdaderos
resultado_all = all([1,2,3,4,"true", True, ])
print(resultado_all)

#suma todos los valores 
sum_total  = sum(lista_numeros)
print(sum_total)