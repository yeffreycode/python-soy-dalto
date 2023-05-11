import pandas as pd

# usando la fncion read_csv para leer el archivo csv
df = pd.read_csv("archivos\\datos.csv")  # df = data frame
df2 = pd.read_csv("archivos\\datos.csv")  # df = data frame


# obteniendo los datos de la columna nombre
# nombres = df['nombre']

# ordenando el dataframe por la edad
df_orden_ascendente = df.sort_values("nombre")


# ordenandolo de forma descendente
df_orden_descendete = df.sort_values("nombre", ascending=False)


# concatenando los dos dataframes
df_concatenado = pd.concat([df, df2])


# accediendo a las primeras 3 filas con head()
primeras_filas = df.head(2)

# accediendo alas ultimas 3 filas con tail
ultimas_filas = df.tail(2)


# accediendo a la cantidad de filas y columnas con shape
filas_totales, columnas_totales = df.shape

# obteniendo data estadistica del dataframe
df_info = df.describe()

# accediendo al nombre de la fila 2
elemento_especifico_loc = df.loc[2, 'nombre']

# accediendo a la edad de la fila 2 con iloc
elemento_especifico_loc = df.iloc[2, 2]

# accediendo a todos los nombres con loc
nombres_loc = df.loc[:, 'nombre']

# accediendo a todos los nombres con iloc

nombres_iloc = df.iloc[:, 1]

# accediendo a la fila 3 con loc
fila_3_loc = df.loc[2, :]

# accediendo a la fila 3 con iloc
fila_3_iloc = df.iloc[2, :]

# accediendo a filas con edad mayor que 30
mayor_que_30 = df.loc[df["edad"] < 30, :]

print(mayor_que_30)
