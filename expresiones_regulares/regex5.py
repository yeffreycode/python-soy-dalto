import re

text = 'Este es un ejemplo de web: https://proyectodalto.com una pagina web: https://www.example.com y tambien podemos '

pattern = 'https?://[a-zA-z0-9.-]+\.[a-zA-Z]{2,}'

result = re.findall(pattern, text)

print(result)
