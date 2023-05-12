# creando una funcion que suma numeros
def suma_dos():
    # iniciando un bucle
    while True:
        # pidiendo numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        # intentando convertirlos a enteros y sumarlos
        try:
            resultado = int(a) + int(b)
        # si lanzo una excepcion, pedirle que reingrese los dos numeros
        except ValueError as e:
            print('te pedi un numero salame, no te detengas')
            print(f"Error: {e}")
        # si todo salio bien terminamos el bucle
        else:
            break
        # el finally se ejecuta siempre
        finally:
            print('Manejo de exepcion finalizado')
    return resultado


# mostrando el resultado
print(suma_dos())
