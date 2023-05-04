#creando una funcion de 3 parametros
#def frase(nombre,apellido,adjetivo):
    #return f"Hola {nombre} {apellido}, tu {adjetivo} es increible"

#utilizando keywods arguments
# frase_resultante = frase(adjetivo="capo", nombre="Lucas", apellido="Dalto")
# print(frase_resultante)


#creando la misma funcion con un parametro opcional y un valor por defecto
def frase(nombre,apellido,adjetivo="Tonto"):
    return f"Hola {nombre} {apellido}, tu {adjetivo} es increible"

frase_resultante = frase("Lucas", "Dalto", adjetivo="inteligente")
print(frase_resultante)