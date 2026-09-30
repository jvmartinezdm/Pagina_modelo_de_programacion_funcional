# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:00:00 2026

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
    calcular_jubilacion,
    calcular_jubilacion_lambda,
    calcular_gastos_acumulados_jubilacion
)


# ============================================================
# TÍTULO
# ============================================================

st.title("🏖️ Cálculo para la jubilación")

st.write(
    "Calcula cuánto dinero necesitas para jubilarte "
    "considerando tu gasto mensual actual y los años "
    "que faltan para tu retiro."
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
        calcular_jubilacion,

    "Función lambda":
        calcular_jubilacion_lambda,
}


funcion_elegida = metodos[metodo]


# ============================================================
# DATOS DE ENTRADA
# ============================================================

col1, col2 = st.columns(2)


with col1:

    gasto_mensual_actual = st.number_input(
        "Gasto mensual actual (MXN):",
        min_value=1000.0,
        value=15000.0,
        step=500.0
    )


with col2:

    años_para_jubilarse = st.number_input(
        "Años que faltan para jubilarte:",
        min_value=1,
        value=30,
        step=1
    )


# ============================================================
# BOTÓN DE CÁLCULO
# ============================================================

if st.button(
    "Calcular fondo para jubilación"
):

    resultado = funcion_elegida(
        gasto_mensual_actual,
        años_para_jubilarse
    )


    # ========================================================
    # RESULTADOS
    # ========================================================

    st.subheader(
        "🏖️ Resultado de la jubilación"
    )


    col1, col2 = st.columns(2)


    col1.metric(
        "Gasto mensual futuro",
        f"${resultado['Gasto mensual al jubilarse (MXN)']:,.2f}"
    )


    col2.metric(
        "Fondo necesario",
        f"${resultado['Fondo total necesario (MXN)']:,.2f}"
    )


    # ========================================================
    # DETALLE DEL CÁLCULO
    # ========================================================

    with st.expander(
        "ℹ️ Detalle del cálculo"
    ):

        for clave, valor in resultado.items():

            st.write(
                f"- **{clave}:** {valor}"
            )


    # ========================================================
    # MENSAJE FINAL
    # ========================================================

    st.success(
        f"🏖️ Para jubilarte en "
        f"{años_para_jubilarse} años "
        f"con un gasto actual de "
        f"**${gasto_mensual_actual:,.2f} MXN al mes**, "
        f"necesitarás aproximadamente un fondo de "
        f"**${resultado['Fondo total necesario (MXN)']:,.2f} MXN**."
    )


    # ========================================================
    # INFORMACIÓN ADICIONAL
    # ========================================================

    st.info(
        f"📌 El cálculo utiliza una inflación anual "
        f"fija de **3.26%** y una tasa de retiro "
        f"anual del **4%**. "
        f"Tu gasto mensual estimado al momento "
        f"de jubilarte será de "
        f"**${resultado['Gasto mensual al jubilarse (MXN)']:,.2f} MXN**."
    )


    # ========================================================
    # PROGRAMACIÓN FUNCIONAL - REDUCE
    # ========================================================

    st.divider()

    st.subheader(
        "➕ Programación funcional: reduce()"
    )


    st.write(
        "Se calcula el gasto anual proyectado para "
        "cada año considerando la inflación. "
        "Posteriormente **reduce()** acumula todos "
        "los valores y produce un único resultado."
    )


    gastos = (
        calcular_gastos_acumulados_jubilacion(
            gasto_mensual_actual,
            años_para_jubilarse
        )
    )


    # ========================================================
    # DATOS PROCESADOS
    # ========================================================

    st.write(
        "### Datos procesados antes de reduce()"
    )


    df_gastos = pd.DataFrame(
        gastos["Gastos anuales"]
    )


    st.dataframe(
        df_gastos,
        use_container_width=True,
        hide_index=True
    )


    # ========================================================
    # GRÁFICA
    # ========================================================

    st.write(
        "### Evolución del gasto anual"
    )


    st.line_chart(
        df_gastos.set_index(
            "Año"
        )[["Gasto anual"]]
    )


    # ========================================================
    # RESULTADO DE REDUCE
    # ========================================================

    st.write(
        "### Resultado de reduce()"
    )


    st.metric(
        "Gasto total acumulado hasta la jubilación",
        f"${gastos['Total acumulado']:,.2f} MXN"
    )


    st.success(
        "reduce() tomó todos los gastos anuales "
        "proyectados y los acumuló en un único "
        "valor utilizando una función lambda."
    )