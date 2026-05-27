import random

def mut_uno(Offspring):
    """
    Mutación de un gen (Single-bit Mutation)
    """
    longitud = len(Offspring.crom1)
    
    # Seleccionamos un índice aleatorio válido.
    # Como random.randint(a, b) incluye ambos extremos, usamos (0, longitud - 1)
    idx1 = random.randint(0, longitud - 1)
    idx2 = random.randint(0, longitud - 1)
    
    # Invertimos el bit seleccionado mediante la resta (1 - valor_actual).
    # Si es 0 se vuelve 1; si es 1 se vuelve 0.
    Offspring.crom1[idx1] = 1 - Offspring.crom1[idx1]
    Offspring.crom2[idx2] = 1 - Offspring.crom2[idx2]
    
    return Offspring