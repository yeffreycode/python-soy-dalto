import re
# detectando un numero CABA y ocultandolo

texto = "Hola Pedro, mi numero es +54 11 4321-4321"

pattern = r'\+\d{2}\s\d{2}\s\d{4}-\d{4}'

reemplazo = re.sub(pattern, '(Numero oculto)', texto)

print(reemplazo)
