import random

def rem_al(Offspring, Pop):
    """
    Reemplazo Aleatorio (Random Replacement)
    """
    # random.sample extrae 2 índices únicos de la población (0 a Pop.N - 1)
    # Reemplaza directamente a randperm(Pop.N, 2)
    idx1, idx2 = random.sample(range(Pop.N), 2)
    
    # Reemplazamos los cromosomas de los individuos seleccionados.
    # Es muy importante usar .copy() para que los individuos de la población 
    # no queden referenciados a la misma dirección de memoria que la descendencia.
    Pop.cromo[idx1, :] = Offspring.crom1.copy()
    Pop.cromo[idx2, :] = Offspring.crom2.copy()
    
    # Reemplazamos la aptitud (Fitness)
    Pop.J[idx1] = Offspring.J1
    Pop.J[idx2] = Offspring.J2
    
    # Reemplazamos las restricciones
    Pop.R[idx1] = Offspring.R1
    Pop.R[idx2] = Offspring.R2
    
    return Pop