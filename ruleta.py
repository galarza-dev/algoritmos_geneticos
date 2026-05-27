import numpy as np
import random

def ruleta(Param_sel):
    """
    Selección por Ruleta (Roulette Wheel Selection)
    """
    # Generamos el número aleatorio entre 0.0 y 1.0
    num_al = random.random()
    
    # np.searchsorted encuentra el primer índice donde 'num_al' debe ir 
    # para mantener el orden del arreglo. Como 'Pa' es una suma acumulada 
    # (y por tanto está ordenada), esto equivale exactamente a 
    # find(Param_sel.Pa >= num_al, 1, 'first')
    num_crom = np.searchsorted(Param_sel.Pa, num_al)
    
    # Retornamos el índice como un número entero nativo de Python
    return int(num_crom)