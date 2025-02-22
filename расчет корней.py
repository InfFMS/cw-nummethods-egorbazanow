import numpy as np
a =  0.1382
b = 3.19 * (10 ** (-5))
R = 8.314
temp_celc = -130
temp_klvn = -130 + 273.15
def vanderwal(V,T):
    P = ((R*T) / (V - b)) - (a / (V**2))
    return P
def solve_ddd(f, d, g, eps=0.01):
    if f(d) * f(g) > 0:
        print("Функция не меняет знак на заданном отрезке. Корень может отсутствовать или быть четным.")
        return None
    while (g - d) / 2 >= eps:
        c = (d + g) / 2
        if f(d) * f(c) <= 0:
            g = c
        else:
            d = c
    return c