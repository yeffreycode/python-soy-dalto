import re
text = 'reemplazando todas las vocales por el asteriscos'

new_text = re.sub('[aeiou]', '*', text)

print(new_text)
