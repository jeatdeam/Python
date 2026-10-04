import pandas as pd

# Abre, lee y cierra el archivo automáticamente en una sola línea
df = pd.read_csv("peliculas_streaming_1000.csv")

# Tus listas se crean igual de fácil
peliculas = df['titulo'].tolist()
generos = df['genero'].tolist()
# plataformas = df['plataforma'].tolist()
# anios = df['anio'].tolist()
# duraciones = df['duracion'].tolist()

# Ahora puedes imprimirlo sin problemas
print(df)
