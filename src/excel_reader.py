import pandas as pd

def obtener_datos(ruta_archivo):
    df = pd.read_excel(ruta_archivo)
    # Filtra solo las filas donde la primera columna (Mes) sea un número
    return df[pd.to_numeric(df.iloc[:, 0], errors='coerce').notnull()]