# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 09:40:23 2026

@author: Profesor D
"""


import sys
from pathlib import Path

# Añade la raíz del proyecto al sys.path para poder importar 'services'
sys.path.append(str(Path(__file__).resolve().parent.parent))


import streamlit as st
from datetime import date

from services.calculations import (
    calcular_dias_vividos,
    calcular_dias_vividos_lambda,
)


st.title("🎂 Días vividos")

st.write("Calcula cuántos días has vivido desde tu nacimiento.")


# Selector del método de cálculo: tradicional o lambda
metodo = st.radio(
    "Selecciona el método de cálculo:",
    options=["Función tradicional", "Función lambda"],
    horizontal=True,
)

# Mapeo del nombre visible a la función real
metodos = {
    "Función tradicional": calcular_dias_vividos,
    "Función lambda": calcular_dias_vividos_lambda,
}
funcion_elegida = metodos[metodo]


# Entrada de la fecha de nacimiento, limitada entre 1900 y hoy
fecha_nacimiento = st.date_input(
    "Selecciona tu fecha de nacimiento:",
    min_value=date(1900, 1, 1),
    max_value=date.today(),
)


if st.button("Calcular días vividos"):
    # Se llama a la función elegida dinámicamente según el radio
    dias = funcion_elegida(fecha_nacimiento)
    st.success(f"🎉 Has vivido {dias:,} días.")