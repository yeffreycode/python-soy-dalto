frase = input("Decime una frase y te claculo cuanto tardarías si tuviera que decirlo: ")

palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f"Dijiste {cantidad_de_palabras} palabras, y tardarías {cantidad_de_palabras/2} segundo en decirlo")
print(f"Dalto lo diría en {cantidad_de_palabras*100//2*.7/100} segundos en decirlo.")

if cantidad_de_palabras > 120:
    print("Para flaco tampoco te pedi un testamento")