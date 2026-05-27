def rem_ambos(Offspring, Pop, Parents):
    """
    Reemplazo de ambos padres (Replace Both Parents)
    """
    # Reemplazamos los cromosomas de los padres con los de la descendencia.
    # El uso de .copy() sigue siendo indispensable para evitar que 
    # los individuos en 'Pop' queden anclados a la memoria de 'Offspring'.
    Pop.cromo[Parents.index1, :] = Offspring.crom1.copy()
    Pop.cromo[Parents.index2, :] = Offspring.crom2.copy()
    
    # Reemplazamos la aptitud (Fitness)
    Pop.J[Parents.index1] = Offspring.J1
    Pop.J[Parents.index2] = Offspring.J2
    
    # Reemplazamos las restricciones
    Pop.R[Parents.index1] = Offspring.R1
    Pop.R[Parents.index2] = Offspring.R2
    
    return Pop