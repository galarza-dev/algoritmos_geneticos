import random

def mut_dos(Offspring):
    """
    Mutación de dos genes (Two-bit Mutation)
    """
    longitud = len(Offspring.crom1)
    
    # random.sample(poblacion, k) nos da k índices únicos.
    # range(longitud) genera los índices válidos desde 0 hasta longitud - 1.
    idx1 = random.sample(range(longitud), 2)
    idx2 = random.sample(range(longitud), 2)
    
    # Invertimos los bits seleccionados (0 se vuelve 1, 1 se vuelve 0)
    # NumPy permite pasar una lista de índices (idx1 e idx2) para modificar 
    # varios elementos al mismo tiempo.
    Offspring.crom1[idx1] = 1 - Offspring.crom1[idx1]
    Offspring.crom2[idx2] = 1 - Offspring.crom2[idx2]
    
    return Offspring