# importando un modulo y asignandole el nombre m_saludar
# import modulo_saludar as m_saludar

# desde ese modulo importamos dos funciones  y le cambiamos el nombre
from modulo_saludar import Saludar as saludar_normal, saludar_raro as saludar_como_coscu

# from modulo_saludar import * # esto es una mala practica(de las peores)
# creamos las variables con los saludos
saludo = saludar_normal("Carlos")
saludo_raro = saludar_como_coscu("Fran")

# mostramos los saludos
print(saludo)
print(saludo_raro)


# para ver las propiedades y metodos del namespace
# print(dir(m_saludar))

# accedemos al nombre de este modulo
print(__name__)

# accedemos al nombre del modulo llamado
# print(m_saludar.__name__)
