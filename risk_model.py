import pandas as pd

def compute_risk(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica reglas de negocio y calcula el índice de riesgo final.
    """

    # Reglas binarias (1 = activa, 0 = no activa)
    df["R1_bajo_promedio"] = (df["promedio_actual"] < 3.0).astype(int)
    df["R2_tendencia_neg"] = (df["tendencia"] < -0.5).astype(int)
    df["R3_ausentismo"] = (df["porcentaje_faltas"] > 0.10).astype(int)
    df["R4_variabilidad"] = (df["variabilidad"] > 0.8).astype(int)
    df["R5_no_entrega"] = (df["ratio_no_entrega"] > 0.30).astype(int)

    # Índice de riesgo (ponderado)
    df["riesgo"] = (
        0.25 * df["R1_bajo_promedio"] +
        0.20 * df["R2_tendencia_neg"] +
        0.20 * df["R3_ausentismo"] +
        0.15 * df["R4_variabilidad"] +
        0.20 * df["R5_no_entrega"]
    )

    # Clasificación final
    df["nivel_riesgo"] = df["riesgo"].apply(classify_risk)

    return df


def classify_risk(score: float) -> str:
    if score >= 0.70:
        return "ALTO"
    elif score >= 0.40:
        return "MEDIO"
    else:
        return "BAJO"
