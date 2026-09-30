# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:15:00 2026

@author: Profesor D
"""

import sys
from pathlib import Path

# Añade la raíz del proyecto al sys.path
# para poder importar 'services'
sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

import streamlit as st
import pandas as pd

from services.calculations import (
    simular_cuenta_bancaria,
    simular_cuenta_bancaria_lambda,
    transformar_capitales
)


# ============================================================
# TÍTULO
# ============================================================

st.title("🏦 Simulación de cuenta bancaria a 10 años")

st.write(
    "Simula el crecimiento de una cuenta bancaria con "
    "interés compuesto y aportaciones anuales durante 10 años."
)


# ============================================================
# SELECCIÓN DEL MÉTODO
# ============================================================

metodo = st.radio(
    "Selecciona el método de cálculo:",
    options=[
        "Función tradicional",
        "Función lambda"
    ],
    horizontal=True,
)


metodos = {
    "Función tradicional":
        simular_cuenta_bancaria,

    "Función lambda":
        simular_cuenta_bancaria_lambda,
}


funcion_elegida = metodos[metodo]


# ============================================================
# DATOS DE ENTRADA
# ============================================================

col1, col2, col3 = st.columns(3)


with col1:

    capital_inicial = st.number_input(
        "Capital inicial (MXN):",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )


with col2:

    aportacion_anual = st.number_input(
        "Aportación anual (MXN):",
        min_value=0.0,
        value=500.0,
        step=100.0
    )


with col3:

    tasa_interes = st.number_input(
        "Tasa de interés anual (%):",
        min_value=0.0,
        max_value=100.0,
        value=5.0,
        step=0.1
    )


# ============================================================
# BOTÓN DE SIMULACIÓN
# ============================================================

if st.button("Simular 10 años"):

    resultados = funcion_elegida(
        capital_inicial,
        aportacion_anual,
        tasa_interes,
        años=10
    )

    df = pd.DataFrame(resultados)


    # ========================================================
    # RESULTADOS ORIGINALES
    # ========================================================

    st.subheader("📋 Detalle año a año")

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


    st.subheader("📈 Evolución del capital")

    st.line_chart(
        df.set_index("Año")[["Capital final"]]
    )


    capital_final = (
        df["Capital final"].iloc[-1]
    )

    total_aportado = (
        capital_inicial
        + aportacion_anual * 10
    )

    total_intereses = (
        capital_final
        - total_aportado
    )


    st.subheader("💰 Resumen final")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Capital final",
        f"{capital_final:,.2f} MXN"
    )

    col2.metric(
        "Total aportado",
        f"{total_aportado:,.2f} MXN"
    )

    col3.metric(
        "Intereses generados",
        f"{total_intereses:,.2f} MXN"
    )


    st.success(
        f"🏦 Tras 10 años tendrás "
        f"**{capital_final:,.2f} MXN**, "
        f"de los cuales "
        f"**{total_intereses:,.2f} MXN** "
        f"son intereses."
    )


    # ========================================================
    # PROGRAMACIÓN FUNCIONAL - MAP
    # ========================================================

    st.divider()

    st.subheader(
        "🔄 Programación funcional: map()"
    )

    st.write(
        "La función **map()** transforma cada registro "
        "de la simulación bancaria aplicando una función "
        "lambda a todos los elementos."
    )


    # La función devuelve un objeto map.
    # En este momento todavía no se han procesado
    # todos sus elementos: Lazy Evaluation.
    datos_map = transformar_capitales(
        resultados
    )


    st.write(
        "**Tipo de dato antes de evaluarlo:**",
        str(type(datos_map))
    )

    st.info(
        "map() utiliza evaluación perezosa. "
        "Los valores se procesan cuando el iterador "
        "es consumido."
    )


    # En este punto se consume el iterador.
    datos_transformados = list(datos_map)


    st.write(
        "### Datos procesados con map()"
    )


    df_map = pd.DataFrame(
        datos_transformados
    )


    st.dataframe(
        df_map,
        use_container_width=True,
        hide_index=True
    )


    st.write(
        "Cada registro fue transformado mediante "
        "una función anónima **lambda**."
    )