# 2 listas, una con nombres, otra con apellidos

nombres = ["Lucas", "Matias", "Camila", "Pedro", "Roberto"]
apellidos = ["Dalto", "Zing", "Dalto", "Robetix", "Tarado"]


# Registrar esta informacion en un TXT de forma optima

with open("archivos_problemas\\nombres_y_apellidos.txt", 'w') as arch:
    arch.writelines("los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n---------\n")
     for n, a in zip(nombres, apellidos)]
