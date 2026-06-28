import matplotlib.pyplot as plt
import os
import numpy as np # Importante: agregamos numpy para los cálculos
from excel_reader import obtener_datos

def graficar_pronostico(ruta_archivo, nombre_salida):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_dir = os.path.join(base_dir, 'output')
    os.makedirs(output_dir, exist_ok=True)

    # 1. Obtener datos limpios (usando tu reader mejorado)
    df = obtener_datos(ruta_archivo)
    
    x = df.iloc[:, 0].values # Meses
    y = df.iloc[:, 1].values # Demanda Real
    
    plt.figure(figsize=(10, 6))
    
    # 2. Graficar la Demanda Real
    plt.plot(x, y, marker='o', linestyle='-', label='Demanda Real')
    
    # 3. Lógica automática: Si es Regresión lineal, calculamos la línea nosotros mismos
    if 'Regresión lineal' in nombre_salida:
        m, b = np.polyfit(x, y, 1) # Cálculo matemático puro
        y_pronostico = m * x + b
        plt.plot(x, y_pronostico, marker='x', linestyle='--', color='red', label='Pronóstico (Regresión)')
    else:
        # Para otros archivos (Promedio Móvil, etc.), graficamos columnas restantes
        y_cols = df.columns[1:]
        for col in y_cols:
            plt.plot(x, df[col], marker='o', linestyle='--', label=col)

    # 4. Formato final del gráfico
    plt.title(f'Pronóstico: {os.path.basename(ruta_archivo)}')
    plt.xlabel(df.columns[0])
    plt.ylabel('Valores')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # 5. Guardar
    ruta_final = os.path.join(output_dir, nombre_salida)
    plt.savefig(ruta_final)
    plt.close()