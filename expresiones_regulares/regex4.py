import re

email = 'example@example.com'

pattern = '[a-zA-Z0-9.%+-+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

result = re.match(pattern, email)

if result:
    print('Direccion de correco valida')
else:
    print("Direccion de correo invalida")
