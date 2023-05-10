# si el modulo estuviera dentro de una carpeta en la misma ruta
# import funciones_buenas.saludar as m_saludar

import saludar as modulo_saludo
import sys
# print(sys.builtin_module_names)
# print(m_saludar.Saludar("Lucas"))
sys.path.append(
    "c:\\Users\\yeffr\\projects\\learn\\python\\soy_dalto\\funciones_buenas")
# print(sys.path)
# ver todos los modulos (built-in)
# print(sys.builtin_module_names)


print(modulo_saludo.saludar("Dalto"))
