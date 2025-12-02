# EduRisk — Sistema de Alertas Tempranas Educativas

**EduRisk** es una herramienta diseñada para identificar estudiantes en riesgo académico mediante análisis de datos, métricas cuantitativas y modelos de riesgo.  
Permite a instituciones educativas tomar decisiones informadas para prevenir repitencia, mejorar desempeño y orientar intervenciones pedagógicas.

---

## Características principales

- Carga de datos desde CSV o Excel  
- Cálculo automático de:
  - Promedios por estudiante  
  - Tendencia de notas  
  - Ausentismo  
  - Variabilidad en desempeño  
  - Porcentaje de no entrega  
- **Modelo de riesgo académico (Bajo / Medio / Alto)**  
- Generación de alertas explicativas y detalladas  
- Dashboard interactivo construido con **Streamlit**  
- Gráficos de:
  - Evolución de notas por grupo
  - Distribución de estudiantes según nivel de riesgo  
- Exportación de resultados procesados

---

## Arquitectura del proyecto
EDURISK/

  ├── dashboard.py # Interfaz principal Streamlit

  ├── preprocessing.py # Carga, validación y limpieza de datos

  ├── metrics.py # Cálculo de métricas base

  ├── risk_model.py # Lógica del riesgo académico

  ├── alerts.py # Generación de alertas detalladas

  ├── sample_data.csv # Dataset de ejemplo

  └── README.md # Documentación del proyecto


---

## Instalación

Clonar el repositorio:

```
git clone https://github.com/tu-user/edurisk.git
```
##  Instalacion Entorno Virtual (OPCIONAL)
```bash
cd edurisk
python -m venv edurisk
edurisk\Scripts\activate
```

## Ejecución
```bash
pip install -r requirements.txt
pip install streamlit pandas plotly openpyxl
streamlit run dashboard.py
```




