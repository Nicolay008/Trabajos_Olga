import os
from charts import graficar_pronostico

# Ruta raíz donde están tus docs
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARPETA_EXCEL = os.path.join(BASE_DIR, 'docs', 'tablas_excel')

archivos = [
    'Demanda vs pronostico.xlsx',
    'Promedio Movil.xlsx',
    'Regresión lineal.xlsx'
]

for nombre in archivos:
    ruta_completa = os.path.join(CARPETA_EXCEL, nombre)
    if os.path.exists(ruta_completa):
        print(f"Procesando: {nombre}")
        graficar_pronostico(ruta_completa, nombre.replace('.xlsx', '_grafico.png'))
    else:
        print(f"Archivo no encontrado: {nombre}")