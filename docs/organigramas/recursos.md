# RECURSOS GRAFICOS

## 1. Organigrama: Supply Chain

```mermaid
graph TD
CEO[Gerencia General]
CEO --> SC[VP Supply Chain]
SC --> SOP[Planeamiento y Demanda]
SC --> PROD[Producción y Envasado]
SC --> LOG[Logística y Distribución]
```


## 2. Promedio Móvil Simple (k=3)

| Mes | Demanda (Dt) | Pronóstico (Pt) | Error Absoluto | Error Cuadrático |
|------|-------------:|----------------:|---------------:|-----------------:|
| Enero   | 12000 | -     | -    | - |
| Febrero | 12500 | -     | -    | - |
| Marzo   | 13200 | -     | -    | - |
| Abril   | 13800 | 12567 | 1233 | 1520289 |
| Mayo    | 14200 | 13167 | 1033 | 1067089 |
| Junio   | 15000 | 13733 | 1267 | 1605289 |
| Julio   | 15500 | 14333 | 1167 | 1361889 |
| Agosto  | 16000 | 14900 | 1100 | 1210000 |

**Figura 3.1. Demanda vs Pronóstico**

[Demanda vs Pronóstico](imagenes/promedio_movil.png)

**Promedio demanda:** 14025

**MAD:** 1160

**MSE:** 1352911


# DAP - DIAGRAMA DE ANÁLISIS DEL PROCESO
## Recepción de Materia Prima en Alicorp S.A.A.

### Visualización del Flujo (Mermaid)

```mermaid
graph TD
    A1[1. Recepción] --> A2[2. Inspección]
    A2 --> A3[3. Transporte]
    A3 --> A4[4. Descarga]
    A4 --> A5[5. Inspección Calidad]
    A5 --> A6[6. Espera Almacén]
    A6 --> A7[7. Transporte Almacén]
    A7 --> A8[8. Clasificación]
    A8 --> A9[9. Almacenamiento Temp]
    A9 --> A10[10. Transporte Producción]
    A10 --> A11[11. Dosificación]
    A11 --> A12[12. Inspección Proceso]
    A12 --> A13[13. Carga Línea]
    A13 --> A14[14. Espera Programación]
    A14 --> A15[15. Producción]
    A15 --> A16[16. Envasado]
    A16 --> A17[17. Inspección Prod. Terminado]
    A17 --> A18[18. Almacenamiento Prod. Terminado]
    A18 --> A19[19. Transporte Distribución]
``` 

### Análisis de Densidad de Símbolos (DAP de Casilleros)

| Símbolo/Columna | Frecuencia | Densidad en el Flujo |
| :--- | :---: | :---: |
| Operación | 8 | 42.1% |
| Transporte | 4 | 21.1% |
| Inspección | 3 | 15.8% |
| Demora | 2 | 10.5% |
| Almacenamiento | 2 | 10.5% |