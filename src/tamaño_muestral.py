from scipy.stats import norm

import pandas as pd


def enoe(z, p, r, tnr, deff, tnp, phv):
    q = 1 - p
    n = (z**2 * q * deff) / (r**2 * p * (1 - tnr) * tnp * phv)
    return n


def nivel_confianza(nivel_confianza):
    porcentaje = nivel_confianza/100
    probabilidad_acumulada = 1 - (1 - porcentaje) / 2
    z = norm.ppf(probabilidad_acumulada)
    return z
