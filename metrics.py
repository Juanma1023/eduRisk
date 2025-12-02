import pandas as pd
import numpy as np

def compute_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula todas las métricas necesarias para evaluar riesgo.
    """

    # Promedio actual
    df["promedio_actual"] = df[["nota1", "nota2", "nota3"]].mean(axis=1)

    # Variabilidad (desviación estándar)
    df["variabilidad"] = df[["nota1", "nota2", "nota3"]].std(axis=1)

    # Tendencia frente al periodo anterior
    df["tendencia"] = df["promedio_actual"] - df["promedio_anterior"]

    # Porcentaje de no entrega
    entregas_total = df["entregas"] + df["no_entregas"]
    if entregas_total[1] == 0:
        entregas_total = np.where(entregas_total == 0, 1, entregas_total)
    df["ratio_no_entrega"] = df["no_entregas"] / entregas_total

    # Ausentismo
    df["porcentaje_faltas"] = df["faltas"] / (df["faltas"] + df["tardanzas"] + 1)

    # Percentil del grupo por curso
    df["percentil"] = df.groupby("curso")["promedio_actual"].rank(pct=True)

    return df
