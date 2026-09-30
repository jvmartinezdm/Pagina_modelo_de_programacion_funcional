# -*- coding: utf-8 -*-
"""
Aplicación de Programación Funcional
Tema 2 - Modelo de Programación Funcional
"""

import streamlit as st


# ============================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Programación Funcional",
    page_icon="💻",
    layout="wide"
)


# ============================================================
# ENCABEZADO
# ============================================================

st.title("💻 Programación Funcional con Python")

st.subheader("Tema 2 - Modelo de Programación Funcional")

st.write(
    """
    Esta aplicación presenta diferentes problemas de la vida cotidiana
    resueltos mediante **Python** y el paradigma de **programación funcional**.

    El objetivo es aplicar funciones tradicionales y conceptos funcionales
    como **lambda, map, filter y reduce**, observando cómo permiten
    transformar, seleccionar y acumular datos de una manera clara y
    reutilizable.
    """
)

st.divider()


# ============================================================
# CONCEPTOS PRINCIPALES
# ============================================================

st.header("Conceptos aplicados")

col1, col2 = st.columns(2)

with col1:

    st.subheader("λ Lambda")

    st.write(
        """
        Las funciones **lambda** permiten crear funciones anónimas
        de forma compacta. En los ejercicios se utilizan como una
        alternativa a las funciones tradicionales.
        """
    )

    st.subheader("🧭 Map")

    st.write(
        """
        **map()** permite aplicar una función a cada elemento de un
        conjunto de datos para obtener una transformación.

        En esta aplicación se utiliza en la simulación de la
        **cuenta bancaria**.
        """
    )


with col2:

    st.subheader("🔎 Filter")

    st.write(
        """
        **filter()** permite seleccionar únicamente los elementos
        de un conjunto de datos que cumplen una determinada condición.

        En esta aplicación se utiliza en el cálculo del
        **consumo de gasolina**.
        """
    )

    st.subheader("➕ Reduce")

    st.write(
        """
        **reduce()** permite acumular los elementos de una colección
        hasta obtener un único resultado.

        En esta aplicación se utiliza en el cálculo para la
        **jubilación**.
        """
    )


st.divider()


#

# ============================================================
# EVALUACIÓN PEREZOSA
# ============================================================

st.header("⚡ Lazy Evaluation")

st.write(
    """
    Una característica importante utilizada en el proyecto es la
    **evaluación perezosa (Lazy Evaluation)**.

    En Python, funciones como **map()** y **filter()** generan
    iteradores. Esto significa que los elementos no tienen que
    procesarse todos inmediatamente, sino conforme son requeridos.

    Esta característica permite trabajar con conjuntos de datos de
    una manera eficiente y forma parte de los conceptos aplicados
    dentro del paradigma funcional.
    """
)


# ============================================================
# MENSAJE FINAL
# ============================================================

st.success(
    "👈 Selecciona uno de los programas desde el menú lateral "
    "para comenzar a utilizar la aplicación."
)