import math
from .constants import Constants as const


def ng_compressibility_factor(pkr, tkr, p, t):
    return 1 - 0.4273 * (p / pkr) * (t / tkr)**-3.668


def pressure_final(p0, psr, Q, Tsr, Z, R, d, ro_st, k, x):
    """Final pressure pk, Pascal"""
    M = Q * ro_st
    lyamda = 0.067 * (2 * k / d) ** 0.2
    return math.sqrt((p0 ** 2) - (16 * (M ** 2) * lyamda * Z * R * Tsr * x) / (math.pi * d ** 5))


def pressure_medium(p0, pk):
    """Medium pressure psr"""
    return (2 / 3) * (p0 + (pk ** 2) / (p0 + pk))
