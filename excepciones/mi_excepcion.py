# creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self, err):
        print(f"impresionante, cometiste el siguiente error: {err}")


# Lanzando mi propia exepcion
# raise MiExcepcion("jjaajaj, persona poco culta")

# manejandola
try:
    raise MiExcepcion("jjaajaj, persona poco culta")
except:
    print("como vas a cometer ese error?")
