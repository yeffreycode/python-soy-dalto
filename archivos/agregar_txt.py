with open("archivos\\texto_de_dalto.txt", 'a', encoding="utf-8") as archivo:
    # usando un bucle  para agregar varias lineas
    archivo.write('\n')
    for i in range(5):
        archivo.write(f"linea {i+1} agregada \n")
