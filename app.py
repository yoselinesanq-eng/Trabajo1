# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# Configuración general
# =========================
st.set_page_config(
    page_title="Análisis de Datos - Proyecto Portafolio",
    page_icon="📊",
    layout="wide"
)

# =========================
# Programación Orientada a Objetos
# =========================
class Author:
    def __init__(self, nombre, curso, anio, descripcion):
        self.nombre = nombre
        self.curso = curso
        self.anio = anio
        self.descripcion = descripcion

    def full_signature(self) -> str:
        return f"{self.nombre} · {self.curso} · {self.anio}"

class ProjectInfo:
    def __init__(self, titulo, objetivo, dataset_desc, tecnologias):
        self.titulo = titulo
        self.objetivo = objetivo
        self.dataset_desc = dataset_desc
        self.tecnologias = tecnologias

    def tech_list(self) -> str:
        return " · ".join(self.tecnologias)

# Instancias de ejemplo (puedes editar con tus datos reales)
author = Author(
    nombre="Yoseline Carolina Sanchez Quino",
    curso="Especialización en Python  For Analytics – Python DMC",
    anio="2026",
    descripcion="Análisis de datos y desarrollo de aplicaciones interactivas."
)

project = ProjectInfo(
    titulo="Análisis Exploratorio de Datos de BankMarketing",
    objetivo=(
        "Explorar, limpiar y visualizar un conjunto de datos para obtener insights clave "
        "que apoyen la toma de decisiones."
    ),
    dataset_desc=(
        "El dataset contiene información demográfica, financiera y de comportamiento de clientes bancarios, junto con datos sobre interacciones realizadas durante campañas de marketing."
        "lo que permite analizar perfiles de clientes, patrones de respuesta y factores que influyen en la efectividad de campañas de marketing directo."
    ),
    tecnologias=[
        "Python",
        "NumPy",
        "Pandas",
        "Matplotlib",
        "Seaborn",
        "Streamlit"
    ]
)

# =========================
# CLASE POO PARA EL ANÁLISIS
# =========================
class DataAnalyzer:
    def __init__(self, df):
        self.df = df

    # Clasificación de variables
    def clasificar_variables(self):
        numericas = self.df.select_dtypes(include=["int64", "float64"]).columns.tolist()
        categoricas = self.df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()
        return numericas, categoricas

    # Estadísticas descriptivas
    def estadisticas(self):
        return self.df.describe().T

    # Valores faltantes
    def faltantes(self):
        return self.df.isnull().sum()

    # Histograma
    def plot_histograma(self, variable, bins=20, kde=True):
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.histplot(self.df[variable].dropna(), bins=bins, kde=kde, color="skyblue", ax=ax)
        ax.set_title(f"Distribución de {variable}")
        return fig

    # Barras categóricas
    def plot_barras(self, variable, top_n=10):
        fig, ax = plt.subplots(figsize=(6, 4))
        self.df[variable].value_counts().head(top_n).plot(kind="bar", ax=ax, color="orange")
        ax.set_title(f"Frecuencia de categorías: {variable}")
        return fig

    # Boxplot numérico vs categórico
    def plot_boxplot(self, num, cat):
        fig, ax = plt.subplots(figsize=(7, 4))
        sns.boxplot(x=self.df[cat], y=self.df[num], ax=ax)
        ax.set_title(f"{num} vs {cat}")
        plt.xticks(rotation=45)
        return fig

    # Heatmap categórico vs categórico
    def plot_heatmap_cat(self, cat1, cat2):
        tabla = pd.crosstab(self.df[cat1], self.df[cat2])
        fig, ax = plt.subplots(figsize=(7, 4))
        sns.heatmap(tabla, annot=True, fmt="d", cmap="Blues", ax=ax)
        ax.set_title(f"Relación entre {cat1} y {cat2}")
        return fig

# =========================
# Sidebar
# =========================
st.sidebar.title("📂 Navegación")
modulo = st.sidebar.radio(
    "Selecciona un módulo:",
    ["Home", "Módulo 2"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.subheader("Información del proyecto")
st.sidebar.write(project.titulo)
st.sidebar.caption(project.objetivo)

# =========================
# MÓDULO 1: HOME
# =========================
if modulo == "Home":
    # Título principal
    st.title("📊 Proyecto de Análisis de Datos")
    st.subheader(project.titulo)

    st.markdown("---")

    # Layout principal
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 🎯 Objetivo del proyecto")
        st.write(project.objetivo)

        st.markdown("### 🧾 Descripción del dataset")
        st.write(project.dataset_desc)

        st.markdown("### 🛠️ Tecnologías utilizadas")
        st.write(project.tech_list())

    with col2:
        st.markdown("### 👤 Autor")
        st.write(author.full_signature())
        st.info(author.descripcion)

        st.markdown("### ℹ️ Detalles adicionales")
        st.write(
            "Este proyecto forma parte de mi portafolio profesional, "
            "enfocado en el uso de Python para análisis de datos y "
            "desarrollo de aplicaciones interactivas con Streamlit."
        )

    st.markdown("---")

    # Tabs solo para organización visual del Home (no análisis aún)
    tab_intro, tab_dataset, tab_tecnologias = st.tabs(
        ["Presentación", "Dataset", "Tecnologías"]
    )

    with tab_intro:
        st.markdown("#### Resumen del proyecto")
        st.write(
            "En este proyecto se aplican conceptos fundamentales de programación en Python, "
            "incluyendo variables, funciones, POO, manejo de datos con NumPy y Pandas, "
            "y visualización con Matplotlib y Seaborn, integrados en una app interactiva con Streamlit."
        )

    with tab_dataset:
        st.markdown("#### Contexto del dataset")
        st.write(
            "Aquí se explicará el origen del dataset, su fuente, el periodo de tiempo que cubre "
            "y las principales variables de interés."
        )
        st.caption("Más adelante se mostrarán ejemplos de las primeras filas y estadísticas descriptivas.")

    with tab_tecnologias:
        st.markdown("#### Stack tecnológico")
        st.write("- Python")
        st.write("- NumPy y Pandas para manipulación de datos")
        st.write("- Matplotlib y Seaborn para visualización")
        st.write("- Streamlit para la interfaz interactiva")
        st.caption("Este módulo solo presenta el proyecto; el análisis se desarrollará en el siguiente módulo.")

# =========================
# PLACEHOLDERS PARA OTROS MÓDULOS
# =========================

# =========================
# MÓDULO 2: CARGA DEL DATASET + EDA
# =========================
elif modulo == "Módulo 2":
    st.title("📂 Módulo 2: Carga del Dataset y Análisis Exploratorio (EDA)")
    st.write("Carga un archivo CSV y explora el dataset mediante diferentes herramientas de análisis.")

    # -------------------------
    # 1. CARGA DEL ARCHIVO
    # -------------------------
    st.subheader("📁 Cargar archivo CSV")

    archivo = st.file_uploader("BankMarketing.csv", type=["csv"])

    if archivo is None:
        st.warning("⚠️ Por favor carga un archivo CSV para habilitar el análisis.")
        st.stop()

    try:
        df = pd.read_csv(archivo)
    except Exception as e:
        st.error(f"❌ Error al leer el archivo: {e}")
        st.stop()

    st.success("✔️ Archivo cargado correctamente")

    # Instancia POO
    analyzer = DataAnalyzer(df)

    # Vista previa
    st.markdown("### 👀 Vista previa del dataset")
    st.dataframe(df.head())

    # Dimensiones
    st.markdown("### 📏 Dimensiones del dataset")
    col_dim1, col_dim2 = st.columns(2)
    with col_dim1:
        st.metric("Filas", df.shape[0])
    with col_dim2:
        st.metric("Columnas", df.shape[1])

    st.markdown("---")

    # Clasificación de variables
    numericas, categoricas = analyzer.clasificar_variables()

    # =========================
    # TABS DEL EDA (10 ÍTEMS)
    # =========================
    (
        tab1, tab2, tab3, tab4, tab5,
        tab6, tab7, tab8, tab9, tab10
    ) = st.tabs([
        "1. Info general",
        "2. Clasificación de variables",
        "3. Estadísticas descriptivas",
        "4. Valores faltantes",
        "5. Distribución numérica",
        "6. Variables categóricas",
        "7. Bivariado numérico vs categórico",
        "8. Bivariado categórico vs categórico",
        "9. Análisis dinámico",
        "10. Hallazgos clave",
    ])

    # ============================================================
    # ÍTEM 1 — INFORMACIÓN GENERAL
    # ============================================================
    with tab1:
        st.header("📌 1. Información general del dataset")

        import io
        buffer = io.StringIO()
        df.info(buf=buffer)
        st.text(buffer.getvalue())

        st.markdown("#### 🔠 Tipos de datos")
        st.write(df.dtypes)

        st.markdown("#### ❗ Conteo de valores nulos")
        st.write(analyzer.faltantes())

    # ============================================================
    # ÍTEM 2 — CLASIFICACIÓN DE VARIABLES
    # ============================================================
    with tab2:
        st.header("📌 2. Clasificación de variables")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("🔢 Variables numéricas")
            st.write(numericas)
            st.write(f"Total: **{len(numericas)}**")

        with col2:
            st.subheader("🔤 Variables categóricas")
            st.write(categoricas)
            st.write(f"Total: **{len(categoricas)}**")

    # ============================================================
    # ÍTEM 3 — ESTADÍSTICAS DESCRIPTIVAS
    # ============================================================
    with tab3:
        st.header("📌 3. Estadísticas descriptivas")

        st.dataframe(analyzer.estadisticas())

        st.markdown("#### 🧠 Conceptos estadísticos aplicados")
        st.info("""
        - **Media:** tendencia central.
        - **Mediana:** valor central, útil con datos sesgados.
        - **Moda:** categoría o valor más frecuente.
        - **Dispersión:** desviación estándar, rango.
        """)

    # ============================================================
    # ÍTEM 4 — VALORES FALTANTES
    # ============================================================
    with tab4:
        st.header("📌 4. Análisis de valores faltantes")

        faltantes = analyzer.faltantes()
        st.write(faltantes)

        faltantes_filtrados = faltantes[faltantes > 0]

        if not faltantes_filtrados.empty:
            fig, ax = plt.subplots(figsize=(6, 3))
            faltantes_filtrados.plot(kind="bar", ax=ax, color="tomato")
            ax.set_title("Valores faltantes por variable")
            st.pyplot(fig)
        else:
            st.success("No hay valores faltantes.")

        st.caption("Variables con muchos valores faltantes requieren imputación o eliminación.")

    # ============================================================
    # ÍTEM 5 — DISTRIBUCIÓN NUMÉRICA
    # ============================================================
    with tab5:
        st.header("📌 5. Distribución de variables numéricas")

        if numericas:
            var = st.selectbox("Selecciona variable numérica:", numericas)
            bins = st.slider("Número de bins:", 5, 50, 20)
            kde = st.checkbox("Mostrar KDE", True)

            fig = analyzer.plot_histograma(var, bins=bins, kde=kde)
            st.pyplot(fig)

            st.caption("La forma del histograma permite identificar sesgos y outliers.")
        else:
            st.warning("No hay variables numéricas.")

    # ============================================================
    # ÍTEM 6 — VARIABLES CATEGÓRICAS
    # ============================================================
    with tab6:
        st.header("📌 6. Análisis de variables categóricas")

        if categoricas:
            var = st.selectbox("Selecciona variable categórica:", categoricas)
            top_n = st.slider("Top categorías:", 3, 20, 10)

            st.write(df[var].value_counts().head(top_n))
            st.write(df[var].value_counts(normalize=True).head(top_n))

            fig = analyzer.plot_barras(var, top_n)
            st.pyplot(fig)
        else:
            st.warning("No hay variables categóricas.")

    # ============================================================
    # ÍTEM 7 — BIVARIADO NUMÉRICO VS CATEGÓRICO
    # ============================================================
    with tab7:
        st.header("📌 7. Análisis bivariado (numérico vs categórico)")

        if numericas and categoricas:
            num = st.selectbox("Variable numérica:", numericas)
            cat = st.selectbox("Variable categórica:", categoricas)

            fig = analyzer.plot_boxplot(num, cat)
            st.pyplot(fig)

            st.caption("Comparación de grupos mediante distribución.")
        else:
            st.warning("Se requieren variables numéricas y categóricas.")

    # ============================================================
    # ÍTEM 8 — BIVARIADO CATEGÓRICO VS CATEGÓRICO
    # ============================================================
    with tab8:
        st.header("📌 8. Análisis bivariado (categórico vs categórico)")

        if len(categoricas) >= 2:
            cat1 = st.selectbox("Variable categórica 1:", categoricas)
            cat2 = st.selectbox("Variable categórica 2:", categoricas)

            fig = analyzer.plot_heatmap_cat(cat1, cat2)
            st.pyplot(fig)
        else:
            st.warning("Se requieren al menos dos variables categóricas.")

    # ============================================================
    # ÍTEM 9 — ANÁLISIS DINÁMICO
    # ============================================================
    with tab9:
        st.header("📌 9. Análisis dinámico según parámetros seleccionados")

        cols = st.multiselect("Selecciona columnas:", df.columns.tolist())

        if cols:
            st.dataframe(df[cols].head())

            if all(c in numericas for c in cols) and len(cols) >= 2:
                st.markdown("#### 📈 Correlación entre columnas seleccionadas")
                fig, ax = plt.subplots(figsize=(6, 4))
                sns.heatmap(df[cols].corr(), annot=True, cmap="coolwarm", ax=ax)
                st.pyplot(fig)
        else:
            st.info("Selecciona columnas para continuar.")

    # ============================================================
    # ÍTEM 10 — HALLAZGOS CLAVE
    # ============================================================
    with tab10:
        st.header("📌 10. Hallazgos clave del EDA")

        resumen = st.text_area(
            "El análisis reveló patrones importantes en la distribución de los datos, presencia de valores atípicos, correlaciones relevantes entre variables y tendencias claras que permiten comprender mejor el comportamiento general del conjunto. Además, se identificaron aspectos de calidad de datos que deben considerarse en futuros análisis.",
            value=(
                "- MonthlyCharges y TotalCharges son las variables con mayor dispersión.\n"
                "- Se observaron relaciones importantes entre Tenure–TotalCharges y MonthlyCharges–Churn.\n"
                "- Existen outliers en cargos mensuales y totales, asociados a clientes con consumos altos.\n"
                "- Las variables categóricas muestran patrones claros: mayor churn en contratos mensuales, pagos con Electronic Check y usuarios de fibra óptica.\n"
            ),
            height=200
        )


