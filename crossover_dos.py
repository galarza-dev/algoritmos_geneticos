import numpy as np
import random

def crossover_dos(Offspring, Parents):
    """
    Cruzamiento de dos puntos (Two-point Crossover)
    """
    longitud = len(Parents.crom1)
    
    # random.sample(poblacion, k) elige k elementos únicos.
    # range(1, longitud) genera valores desde 1 hasta longitud - 1.
    # Esto equivale exactamente a randperm(length(Parents.crom1)-1, 2)
    puntos = random.sample(range(1, longitud), 2)
    
    # Ordenamos los puntos para saber cuál es el primer corte y cuál el segundo
    cp1, cp2 = sorted(puntos)
    
    # Es vital hacer copias (.copy()) para no modificar la estructura de los padres
    Offspring.crom1 = Parents.crom1.copy()
    Offspring.crom2 = Parents.crom2.copy()
    
    # Intercambio del segmento central.
    # El rebanado [cp1:cp2] en Python reemplaza de forma natural a la 
    # sintaxis (cross_point(1)+1:cross_point(2)) de MATLAB.
    Offspring.crom1[cp1:cp2] = Parents.crom2[cp1:cp2]
    Offspring.crom2[cp1:cp2] = Parents.crom1[cp1:cp2]
    
    return Offspring