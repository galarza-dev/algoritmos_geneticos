import numpy as np
import random

def crossover_uno(Offspring, Parents):
    """
    Cruzamiento de un punto (Single-point Crossover)
    """
    longitud = len(Parents.crom1)
    
    # Se elige un punto de cruce aleatorio. 
    # random.randint(a, b) incluye ambos extremos, por lo que va de 1 a (longitud - 1).
    # Esto asegura que al menos un gen se intercambie y no cortemos en los bordes nulos.
    cross_point = random.randint(1, longitud - 1)
    
    # Slicing (rebanado) con NumPy y concatenación:
    # array[:cross_point] toma los elementos desde el inicio hasta cross_point-1
    # array[cross_point:] toma los elementos desde cross_point hasta el final
    Offspring.crom1 = np.concatenate((Parents.crom1[:cross_point], Parents.crom2[cross_point:]))
    Offspring.crom2 = np.concatenate((Parents.crom2[:cross_point], Parents.crom1[cross_point:]))
    
    return Offspring