# creando un conjunto con set

#solo reciven dato iterable con datos inmutables 
conjunto = set(["dato1", ("datoenlista"),"dato2"])

conjunto1 = frozenset(["dato1", "dato2"])
conjunto2 = {conjunto1, "dato3"}
print(conjunto2);

#Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,5,7}

#verificar is es un subconjunto
resultado = conjunto2.issubset(conjunto1);
resultado = conjunto2 <= conjunto1 # tambien se puede verificar asi
print(resultado)

#verificar is es un subconjunto
resultado = conjunto1.issuperset(conjunto2);
resultado = conjunto1 > conjunto2 # tambien se puede verificar asi
print(resultado);

#verificar si hay algun numero en comun retorna falso si  hay.
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado);