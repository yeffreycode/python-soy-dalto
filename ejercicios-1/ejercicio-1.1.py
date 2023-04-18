##=========== Ejercicio A================
#Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso =1.5

# Diferencias de duracion en porcentaje. 
diferencia_con_min = 100 - dalto_curso / otros_cursos_min*100
diferencia_con_max = 100 - dalto_curso*1000 // otros_cursos_max/10
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio*100

#mostrando las diferencias de duración
print("----------------Ejercicio A.--------------------")
print(f"El curso de Dalto dura un {diferencia_con_min}% menos que el más rápido. ")
print(f"El curso de Dalto dura un {diferencia_con_max}% menos que el que tiene más duración.")
print(f"El curso de Dalto dura un {diferencia_con_promedio}% menos que el promedio. ")

##============ Ejercicio B==========0
#Duracion de crudos
crudo_promedio = 5
crudo_dalto=3.5

#Calculando el porcentaje de tiempo vacio
tiempo_vacio_promedio =100 - otros_cursos_promedio*1000 // crudo_promedio/10
tiempo_vacio_dalto =100 - dalto_curso*1000 // crudo_dalto/10

#mostrando la cantidad de espacios vacion que se remueven (ejercicio B)
print("----------------Ejercicio B.--------------------")
print(f"Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio. ")
print(f"Este curso  eliminó el  {tiempo_vacio_dalto}% de tiempo vacio. ")

##============ Ejercicio B==========0
#Mostrando diferencias si los cursos duran 10 horas.
print("----------------Ejercicio C.--------------------")
print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos")
print(f"Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso")