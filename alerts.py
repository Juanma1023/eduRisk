import pandas as pd

def generate_alerts(df: pd.DataFrame) -> pd.DataFrame:
    """
    Genera alertas detalladas y explicativas por estudiante,
    combinando reglas con datos cuantitativos.
    """

    messages = []

    for _, row in df.iterrows():
        alert_list = []

        # --- ALERTA 1: Promedio bajo ---
        if row.get("R1_bajo_promedio", 0) == 1:
            alert_list.append(
                f"Promedio bajo ({row['promedio_actual']:.1f}). "
                f"Percentil del curso: {row.get('percentil', 0)*100:.0f}%."
            )

        # --- ALERTA 2: Tendencia negativa ---
        if row.get("R2_tendencia_neg", 0) == 1:
            alert_list.append(
                f"Tendencia negativa: cayó {abs(row['tendencia']):.1f} puntos desde el periodo anterior."
            )

        # --- ALERTA 3: Ausentismo ---
        if row.get("R3_ausentismo", 0) == 1:
            alert_list.append(
                f"Ausentismo alto: {row['faltas']} faltas y {row['tardanzas']} tardanzas."
            )

        # --- ALERTA 4: Variabilidad (desempeño inestable) ---
        if row.get("R4_variabilidad", 0) == 1:
            alert_list.append(
                f"Desempeño inestable: variabilidad {row['variabilidad']:.2f} entre notas."
            )

        # --- ALERTA 5: No entrega ---
        if row.get("R5_no_entrega", 0) == 1:
            total_tareas = row['entregas'] + row['no_entregas']
            alert_list.append(
                f"No entrega crítica: {row['no_entregas']} de {total_tareas} tareas sin entregar "
                f"({row['ratio_no_entrega']*100:.0f}%)."
            )

        # --- Si no hay alertas ---
        if len(alert_list) == 0:
            messages.append("Sin alertas.")
        else:
            messages.append(" | ".join(alert_list))

    df["alertas"] = messages
    return df
