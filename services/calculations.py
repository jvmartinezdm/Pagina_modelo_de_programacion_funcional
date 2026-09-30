# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 09:40:49 2026

@author: Profesor D
"""

from datetime import date
from functools import reduce


# ============================================================
# 1. CÁLCULO DE DÍAS VIVIDOS
# ============================================================

def calcular_dias_vividos(fecha_nacimiento):
    """
    Calcula la cantidad de días transcurridos desde la fecha
    de nacimiento hasta la fecha actual.
    """
    fecha_actual = date.today()
    return (fecha_actual - fecha_nacimiento).days


calcular_dias_vividos_lambda = lambda fecha_nacimiento: (
    date.today() - fecha_nacimiento
).days


# ============================================================
# 2. SIMULACIÓN DE CUENTA BANCARIA A 10 AÑOS
# ============================================================

def simular_cuenta_bancaria(
    capital_inicial,
    aportacion_anual,
    tasa_interes,
    años=10
):
    """
    Simula el crecimiento de una cuenta bancaria aplicando
    una aportación anual y posteriormente los intereses.
    """

    resultados = []
    capital = capital_inicial

    for año in range(1, años + 1):

        capital_inicio = capital

        # Se realiza la aportación anual.
        capital += aportacion_anual

        # Se calculan los intereses del año.
        intereses = capital * (tasa_interes / 100)

        # Se agregan los intereses al capital.
        capital += intereses

        resultados.append({
            "Año": año,
            "Capital inicial": round(capital_inicio, 2),
            "Aportación": round(aportacion_anual, 2),
            "Intereses": round(intereses, 2),
            "Capital final": round(capital, 2)
        })

    return resultados


simular_cuenta_bancaria_lambda = lambda capital_inicial, aportacion_anual, tasa_interes, años=10: (
    simular_cuenta_bancaria(
        capital_inicial,
        aportacion_anual,
        tasa_interes,
        años
    )
)


# ============================================================
# MAP - CUENTA BANCARIA
# ============================================================

def transformar_capitales(resultados):
    """
    Utiliza map() para transformar los resultados de cada año.

    Por cada registro se obtiene:
    - Año
    - Capital final
    - Intereses generados
    - Capital final duplicado

    map() devuelve un iterador, por lo que se conserva
    la evaluación perezosa (Lazy Evaluation).
    """

    return map(
        lambda dato: {
            "Año": dato["Año"],
            "Capital final": dato["Capital final"],
            "Intereses generados": dato["Intereses"],
            "Capital final duplicado": round(
                dato["Capital final"] * 2,
                2
            )
        },
        resultados
    )


# ============================================================
# 3. SIMULACIÓN DE VIAJE UBER
# ============================================================

def calcular_tiempo_uber(distancia_km, velocidad_media):
    """
    Calcula el tiempo estimado de un viaje considerando
    tiempo base, espera y tiempo de conducción.
    """

    factor_trafico = 1.0
    tiempo_espera = 5
    tiempo_base = 2

    tiempo_conduccion = (
        distancia_km / velocidad_media
    ) * 60 * factor_trafico

    tiempo_total = (
        tiempo_base
        + tiempo_espera
        + tiempo_conduccion
    )

    return {
        "Distancia (km)": round(distancia_km, 2),
        "Velocidad media (km/h)": round(velocidad_media, 2),
        "Tiempo de conducción (min)": round(
            tiempo_conduccion,
            2
        ),
        "Tiempo total (min)": round(
            tiempo_total,
            2
        ),
    }


calcular_tiempo_uber_lambda = (
    lambda distancia_km, velocidad_media: {

        "Distancia (km)": round(
            distancia_km,
            2
        ),

        "Velocidad media (km/h)": round(
            velocidad_media,
            2
        ),

        "Tiempo de conducción (min)": round(
            (distancia_km / velocidad_media) * 60,
            2
        ),

        "Tiempo total (min)": round(
            2
            + 5
            + (distancia_km / velocidad_media) * 60,
            2
        ),
    }
)


# ============================================================
# 4. CÁLCULO DE CONSUMO DE GASOLINA
# ============================================================

def calcular_consumo_gasolina(
    distancia_km,
    rendimiento_km_l,
    precio_litro,
    factor_trafico=1.0
):
    """
    Calcula el consumo de gasolina y el coste de un trayecto.

    Reglas de negocio:

    Consumo total =
    (distancia / rendimiento) * factor de tráfico

    Coste total =
    consumo total * precio por litro
    """

    consumo_total = (
        distancia_km / rendimiento_km_l
    ) * factor_trafico

    coste_total = (
        consumo_total * precio_litro
    )

    return {
        "Distancia (km)": round(
            distancia_km,
            2
        ),

        "Rendimiento (km/L)": round(
            rendimiento_km_l,
            2
        ),

        "Factor tráfico": factor_trafico,

        "Precio por litro (MXN)": round(
            precio_litro,
            2
        ),

        "Consumo total (L)": round(
            consumo_total,
            2
        ),

        "Coste total (MXN)": round(
            coste_total,
            2
        ),

        "Coste por km (MXN/km)": round(
            coste_total / distancia_km,
            3
        ),
    }


calcular_consumo_gasolina_lambda = (
    lambda distancia_km,
    rendimiento_km_l,
    precio_litro,
    factor_trafico=1.0: {

        "Distancia (km)": round(
            distancia_km,
            2
        ),

        "Rendimiento (km/L)": round(
            rendimiento_km_l,
            2
        ),

        "Factor tráfico": factor_trafico,

        "Precio por litro (MXN)": round(
            precio_litro,
            2
        ),

        "Consumo total (L)": round(
            (
                distancia_km / rendimiento_km_l
            ) * factor_trafico,
            2
        ),

        "Coste total (MXN)": round(
            (
                (
                    distancia_km / rendimiento_km_l
                )
                * factor_trafico
            )
            * precio_litro,
            2
        ),

        "Coste por km (MXN/km)": round(
            (
                (
                    (
                        distancia_km / rendimiento_km_l
                    )
                    * factor_trafico
                )
                * precio_litro
            )
            / distancia_km,
            3
        ),
    }
)


# ============================================================
# FILTER - CONSUMO DE GASOLINA
# ============================================================

def filtrar_consumos_altos(
    distancia_km,
    rendimiento_km_l,
    precio_litro,
    limite_consumo
):
    """
    Genera tres escenarios de tráfico utilizando map()
    y posteriormente selecciona con filter() solamente
    aquellos que superan el límite de consumo indicado.

    Tanto map() como filter() trabajan con evaluación
    perezosa (Lazy Evaluation).
    """

    factores_trafico = [1.0, 1.5, 2.0]

    # MAP transforma cada factor de tráfico
    # en un escenario completo de consumo.
    escenarios = map(
        lambda factor: calcular_consumo_gasolina(
            distancia_km,
            rendimiento_km_l,
            precio_litro,
            factor
        ),
        factores_trafico
    )

    # FILTER selecciona únicamente los escenarios
    # cuyo consumo supera el límite establecido.
    return filter(
        lambda dato: (
            dato["Consumo total (L)"]
            > limite_consumo
        ),
        escenarios
    )


# ============================================================
# 5. CÁLCULO DE DINERO PARA LA JUBILACIÓN
# ============================================================

def calcular_jubilacion(
    gasto_mensual_actual,
    años_para_jubilarse
):
    """
    Calcula el gasto mensual estimado al momento de jubilarse
    considerando una inflación anual del 3.26 %.

    Posteriormente calcula el fondo necesario utilizando
    una tasa de retiro anual del 4 %.
    """

    inflacion_anual = 3.26
    tasa_retiro = 4.0

    factor_inflacion = (
        1 + inflacion_anual / 100
    ) ** años_para_jubilarse

    gasto_futuro_mensual = (
        gasto_mensual_actual
        * factor_inflacion
    )

    fondo_necesario = (
        gasto_futuro_mensual * 12
    ) / (tasa_retiro / 100)

    return {
        "Gasto mensual actual (MXN)": round(
            gasto_mensual_actual,
            2
        ),

        "Años para jubilarse":
            años_para_jubilarse,

        "Gasto mensual al jubilarse (MXN)": round(
            gasto_futuro_mensual,
            2
        ),

        "Fondo total necesario (MXN)": round(
            fondo_necesario,
            2
        ),
    }


calcular_jubilacion_lambda = (
    lambda gasto_mensual_actual,
    años_para_jubilarse: {

        "Gasto mensual actual (MXN)": round(
            gasto_mensual_actual,
            2
        ),

        "Años para jubilarse":
            años_para_jubilarse,

        "Gasto mensual al jubilarse (MXN)": round(
            gasto_mensual_actual
            * (1 + 3.26 / 100)
            ** años_para_jubilarse,
            2
        ),

        "Fondo total necesario (MXN)": round(
            (
                gasto_mensual_actual
                * (1 + 3.26 / 100)
                ** años_para_jubilarse
                * 12
            )
            / (4.0 / 100),
            2
        ),
    }
)


# ============================================================
# REDUCE - JUBILACIÓN
# ============================================================

def calcular_gastos_acumulados_jubilacion(
    gasto_mensual_actual,
    años_para_jubilarse
):
    """
    Calcula el gasto anual proyectado para cada año
    hasta la jubilación.

    map() transforma cada año en su correspondiente
    gasto anual considerando inflación.

    reduce() acumula todos los gastos anuales para
    obtener un único resultado.
    """

    inflacion = 3.26 / 100

    # MAP transforma cada año en su gasto anual proyectado.
    gastos_iterador = map(
        lambda año: {
            "Año": año,
            "Gasto anual": round(
                gasto_mensual_actual
                * (1 + inflacion) ** año
                * 12,
                2
            )
        },
        range(1, años_para_jubilarse + 1)
    )

    # Se convierte a lista porque necesitamos:
    # 1. Mostrar los datos procesados.
    # 2. Utilizarlos posteriormente con reduce().
    gastos_anuales = list(gastos_iterador)

    # REDUCE acumula todos los gastos anuales.
    total_acumulado = reduce(
        lambda acumulador, dato:
            acumulador + dato["Gasto anual"],
        gastos_anuales,
        0
    )

    return {
        "Gastos anuales": gastos_anuales,
        "Total acumulado": round(
            total_acumulado,
            2
        )
    }