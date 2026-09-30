# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:30:00 2026

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
    calcular_consumo_gasolina,
    calcular_consumo_gasolina_lambda,
    filtrar_consumos_altos
)


# ============================================================
# TÍTULO
# ============================================================

st.title("⛽ Cálculo de consumo de gasolina")

st.write(
    "Calcula el consumo de combustible y su coste "
    "para un trayecto, teniendo en cuenta el nivel "
    "de tráfico."
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
        calcular_consumo_gasolina,

    "Función lambda":
        calcular_consumo_gasolina_lambda,
}


funcion_elegida = metodos[metodo]


# ============================================================
# DATOS DE ENTRADA
# ============================================================

col1, col2 = st.columns(2)


with col1:

    distancia_km = st.number_input(
        "Distancia del trayecto (km):",
        min_value=0.1,
        value=100.0,
        step=1.0
    )

    rendimiento_km_l = st.number_input(
        "Rendimiento del vehículo (km/L):",
        min_value=0.1,
        value=15.0,
        step=0.5
    )


with col2:

    precio_litro = st.number_input(
        "Precio de la gasolina (MXN/L):",
        min_value=0.1,
        value=25.00,
        step=0.10
    )

    factor_trafico = st.select_slider(
        "Nivel de tráfico:",
        options=[
            1.0,
            1.5,
            2.0
        ],
        value=1.0,

        format_func=lambda x: {
            1.0: "🟢 Fluido",
            1.5: "🟡 Moderado",
            2.0: "🔴 Congestionado",
        }[x],
    )


# ============================================================
# LÍMITE PARA FILTER
# ============================================================

st.subheader(
    "🔎 Configuración de filter()"
)

limite_consumo = st.number_input(
    "Mostrar escenarios con consumo mayor a (L):",
    min_value=0.0,
    value=8.0,
    step=0.5
)


# ============================================================
# BOTÓN CALCULAR
# ============================================================

if st.button("Calcular consumo"):

    resultado = funcion_elegida(
        distancia_km=distancia_km,
        rendimiento_km_l=rendimiento_km_l,
        precio_litro=precio_litro,
        factor_trafico=factor_trafico,
    )


    # ========================================================
    # RESULTADO DEL TRAYECTO
    # ========================================================

    st.subheader(
        "⛽ Resultado del trayecto"
    )

    col1, col2, col3 = st.columns(3)


    col1.metric(
        "Consumo total",
        f"{resultado['Consumo total (L)']:.2f} L"
    )


    col2.metric(
        "Coste total",
        f"${resultado['Coste total (MXN)']:,.2f} MXN"
    )


    col3.metric(
        "Coste por km",
        f"${resultado['Coste por km (MXN/km)']:.3f} MXN/km"
    )


    # ========================================================
    # DETALLE
    # ========================================================

    with st.expander(
        "ℹ️ Detalle del cálculo"
    ):

        for clave, valor in resultado.items():

            st.write(
                f"- **{clave}:** {valor}"
            )


    nombres_trafico = {
        1.0: "🟢 Fluido",
        1.5: "🟡 Moderado",
        2.0: "🔴 Congestionado"
    }


    st.success(
        f"🚗 Para un trayecto de "
        f"{distancia_km} km con tráfico "
        f"**{nombres_trafico[factor_trafico]}**, "
        f"consumirás "
        f"**{resultado['Consumo total (L)']:.2f} L** "
        f"y gastarás "
        f"**${resultado['Coste total (MXN)']:,.2f} MXN**."
    )


    # ========================================================
    # PROGRAMACIÓN FUNCIONAL - FILTER
    # ========================================================

    st.divider()

    st.subheader(
        "🔎 Programación funcional: filter()"
    )

    st.write(
        "Se generan escenarios para tráfico fluido, "
        "moderado y congestionado. Después "
        "**filter()** selecciona solamente aquellos "
        "cuyo consumo supera el límite establecido."
    )


    # Esta función devuelve un objeto filter.
    escenarios_filtrados = (
        filtrar_consumos_altos(
            distancia_km,
            rendimiento_km_l,
            precio_litro,
            limite_consumo
        )
    )


    # Todavía es un iterador.
    st.write(
        "**Tipo de dato antes de evaluarlo:**",
        str(type(escenarios_filtrados))
    )


    st.info(
        "filter() utiliza evaluación perezosa "
        "(Lazy Evaluation). Los elementos se "
        "procesan cuando se consume el iterador."
    )


    # Aquí se consume el objeto filter.
    datos_filtrados = list(
        escenarios_filtrados
    )


    st.write(
        f"### Escenarios con consumo mayor "
        f"a {limite_consumo:.2f} L"
    )


    if datos_filtrados:

        df_filter = pd.DataFrame(
            datos_filtrados
        )

        st.dataframe(
            df_filter,
            use_container_width=True,
            hide_index=True
        )

    else:

        st.warning(
            "Ningún escenario supera el "
            "límite de consumo seleccionado."
        )


    st.write(
        "La condición utilizada por **filter()** "
        "se implementa mediante una función "
        "anónima **lambda**."
    )