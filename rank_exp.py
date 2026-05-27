import numpy as np

def rank_exp(Pop, Param_sel):
    """
    Selección basada en Rango Exponencial (ERS) - Probabilidades
    """
    # En la fórmula matemática, 'i' va de 1 a N. 
    # np.arange(1, Pop.N + 1) genera exactamente ese vector: [1, 2, ..., N]
    i = np.arange(1, Pop.N + 1)
    
    # Extraemos las variables para que la fórmula sea más limpia de leer
    r = Param_sel.r
    N = Pop.N
    
    # Aplicamos la fórmula matemática vectorizada
    # El operador ** en arreglos de NumPy equivale al .^ de MATLAB
    P_rank = ((r ** (N - i)) * (1 - r)) / (1 - (r ** N))
    
    # Cálculo de la probabilidad acumulada
    Param_sel.Pa = np.cumsum(P_rank)
    
    return Param_sel