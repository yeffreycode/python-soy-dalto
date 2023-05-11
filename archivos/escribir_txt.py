with open("archivos\\texto_de_dalto.txt", 'w', encoding="utf-8") as archivo:
    # sobreescribiendo el archivo
    # archivo.write('jajajaj te la recontra tecleee')

    # agregando 2 lineas con writeline
    archivo.writelines(['- Hola maestro como andas\n', '- misericoradia\n'])
    # agregando otras dos lineas
    archivo.writelines(['- no se porque dijiste eso\n', '- yo tampoco'])
