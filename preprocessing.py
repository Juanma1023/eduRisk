import pandas as pd

REQUIRED_COLUMNS = [
    "estudiante",
    "curso",
    "nota1",
    "nota2",
    "nota3",
    "faltas",
    "tardanzas",
    "entregas",
    "no_entregas",
    "promedio_anterior"
]

def load_data(file) -> pd.DataFrame:
    """
    Carga un archivo CSV o Excel subido por Streamlit (UploadedFile)
    o un archivo desde disco (str).
    """

    # Caso 1: archivo subido por Streamlit → tiene atributo "name"
    if hasattr(file, "name"):
        filename = file.name.lower()

        if filename.endswith(".csv"):
            df = pd.read_csv(file)
        elif filename.endswith(".xlsx") or filename.endswith(".xls"):
            df = pd.read_excel(file)
        else:
            raise ValueError("Formato no soportado. Usa CSV o Excel.")

    # Caso 2: archivo local con ruta en string
    elif isinstance(file, str):
        if file.lower().endswith(".csv"):
            df = pd.read_csv(file)
        elif file.lower().endswith(".xlsx") or file.lower().endswith(".xls"):
            df = pd.read_excel(file)
        else:
            raise ValueError("Formato no soportado. Usa CSV o Excel.")

    else:
        raise ValueError("Tipo de archivo no reconocido.")

    validate_columns(df)
    df = clean_data(df)
    return df


def validate_columns(df):
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(f"Faltan columnas requeridas: {missing}")


def clean_data(df):
    numeric_cols = [
        "nota1", "nota2", "nota3",
        "faltas", "tardanzas",
        "entregas", "no_entregas",
        "promedio_anterior"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    df["estudiante"] = df["estudiante"].astype(str)

    return df
