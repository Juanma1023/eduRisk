import streamlit as st
import pandas as pd
import plotly.express as px

from preprocessing import load_data
from metrics import compute_metrics
from risk_model import compute_risk
from alerts import generate_alerts

st.set_page_config(page_title="EduRisk - Sistema de Alertas", layout="wide")

st.title("📊 EduRisk - Sistema de Alertas Tempranas")
st.write("Sube un archivo CSV o Excel para analizar el riesgo académico de tu institución.")

# ======================
# 1. CARGA DEL ARCHIVO
# ======================

file = st.file_uploader("Sube el archivo CSV o Excel", type=["csv", "xlsx"])

if file:
    # Cargar datos
    df = load_data(file)
    
    # Calcular métricas
    df = compute_metrics(df)
    
    # Calcular riesgo
    df = compute_risk(df)
    
    # Generar alertas
    df = generate_alerts(df)

    st.success("Datos procesados correctamente.")
    
    # ======================
    # 2. FILTROS
    # ======================
    st.sidebar.header("🔍 Filtros")

    cursos = sorted(df["curso"].unique())
    filtro_curso = st.sidebar.multiselect("Filtrar por curso", cursos, default=cursos)

    niveles = ["BAJO", "MEDIO", "ALTO"]
    filtro_riesgo = st.sidebar.multiselect("Filtrar por nivel de riesgo", niveles, default=niveles)

    df_filtrado = df[
        df["curso"].isin(filtro_curso) &
        df["nivel_riesgo"].isin(filtro_riesgo)
    ]

    # ======================
    # 3. TABLA PRINCIPAL
    # ======================

    st.subheader("📋 Resultados")

    st.dataframe(
        df_filtrado[[
            "estudiante", "curso", "promedio_actual", "tendencia",
            "variabilidad", "porcentaje_faltas", "ratio_no_entrega",
            "nivel_riesgo", "alertas"
        ]],
        use_container_width=True
    )

    # ======================
    # 4. GRÁFICOS
    # ======================

    st.subheader("📈 Análisis Visual")

    col1, col2 = st.columns(2)

    with col1:
        fig1 = px.histogram(df_filtrado, x="nivel_riesgo", color="curso", title="Distribución de riesgo por curso")
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        fig2 = px.box(df_filtrado, x="curso", y="promedio_actual", color="curso", title="Promedios por curso")
        st.plotly_chart(fig2, use_container_width=True)

    # --------------------------------------------------------------------
    # 🎯 GRÁFICO: ESTUDIANTES POR NIVEL DE RIESGO
    # --------------------------------------------------------------------

    st.subheader("🎯 Estudiantes por nivel de riesgo")

    cursos = df["curso"].unique()
    curso_sel_riesgo = st.selectbox("Selecciona un curso para ver riesgos", ["Todos"] + list(cursos))

    df_risk = df.copy()

    if curso_sel_riesgo != "Todos":
        df_risk = df_risk[df_risk["curso"] == curso_sel_riesgo]

    # Crear índice para visualizar estudiantes ordenados por riesgo
    df_risk = df_risk.sort_values("nivel_riesgo")
    df_risk["index"] = range(1, len(df_risk) + 1)

    fig_risk = px.scatter(
        df_risk,
        x="index",
        y="promedio_actual",
        color="nivel_riesgo",
        hover_data=["estudiante", "curso", "promedio_actual", "alertas"],
        title="Distribución de estudiantes según nivel de riesgo",
    )

    fig_risk.update_layout(
        xaxis_title="Estudiantes",
        yaxis_title="Promedio actual",
    )

    st.plotly_chart(fig_risk, use_container_width=True)

    # ======================
    # 5. Exportar datos
    # ======================

    st.subheader("⬇ Exportar")

    csv_export = df_filtrado.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Descargar resultados en CSV",
        data=csv_export,
        file_name="edurisk_resultados.csv",
        mime="text/csv"
    )
