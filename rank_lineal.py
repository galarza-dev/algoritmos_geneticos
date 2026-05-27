import numpy as np

def rank_lineal(Pop, Param_sel):
    """
    Selección basada en Rango Lineal (LRS) - Probabilidades
    """
    # Rango matemático de 1 a N
    i = np.arange(1, Pop.N + 1)
    
    # Extraemos las variables para mayor claridad en la fórmula
    N = Pop.N
    cmin = Param_sel.cmin
    cmax = Param_sel.cmax
    
    # Aplicamos la fórmula lineal vectorizada
    P_rank = (1 / N) * (cmin + (cmax - cmin) * (i - 1) / (N - 1))
    
    # Cálculo de la probabilidad acumulada
    Param_sel.Pa = np.cumsum(P_rank)
    
    return Param_sel