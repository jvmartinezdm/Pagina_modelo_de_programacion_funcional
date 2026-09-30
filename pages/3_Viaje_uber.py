import sys
from pathlib import Path

# Añade la raíz del proyecto al sys.path para poder importar 'services'
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st

from services.calculations import (
    calcular_tiempo_uber,
    calcular_tiempo_uber_lambda,
)


# ==============================
# TÍTULO
# ==============================

st.title("🚗 Simulación de viaje Uber")

st.write(
    "Calcula el tiempo estimado de un viaje Uber según "
    "la distancia y la velocidad media."
)


# ==============================
# SELECCIÓN DEL MÉTODO
# ==============================

metodo = st.radio(
    "Selecciona el método de cálculo:",
    options=[
        "Función tradicional",
        "Función lambda"
    ],
    horizontal=True,
)


# Relaciona cada opción con su función
metodos = {
    "Función tradicional": calcular_tiempo_uber,
    "Función lambda": calcular_tiempo_uber_lambda,
}


# Guarda la función seleccionada
funcion_elegida = metodos[metodo]


# ==============================
# DATOS DE ENTRADA
# ==============================

col1, col2 = st.columns(2)


with col1:

    distancia_km = st.number_input(
        "Distancia del viaje (km):",
        min_value=0.1,
        value=8.0,
        step=0.5
    )


with col2:

    velocidad_media = st.number_input(
        "Velocidad media (km/h):",
        min_value=1.0,
        value=30.0,
        step=1.0
    )


# ==============================
# BOTÓN CALCULAR
# ==============================

if st.button("Calcular tiempo de viaje"):

    # Ejecuta la función seleccionada
    resultado = funcion_elegida(
        distancia_km,
        velocidad_media
    )


    # ==============================
    # RESULTADOS
    # ==============================

    st.subheader("⏱️ Resultado del viaje")


    col1, col2 = st.columns(2)


    col1.metric(
        "Tiempo de conducción",
        f"{resultado['Tiempo de conducción (min)']:.1f} min"
    )


    col2.metric(
        "Tiempo total",
        f"{resultado['Tiempo total (min)']:.1f} min"
    )


    # ==============================
    # MENSAJE FINAL
    # ==============================

    st.success(
        f"🚗 Tu viaje de {distancia_km} km tardará aproximadamente "
        f"**{resultado['Tiempo total (min)']:.1f} minutos**."
    )