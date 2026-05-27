def rem_peor(Offspring, Pop, Parents):
    """
    Reemplazo Basado en Peor Rendimiento (Torneo Padre vs. Hijo)
    """
    # Si el Hijo 1 tiene mejor aptitud (mayor J) que el Padre 1, lo reemplaza
    if Offspring.J1 > Parents.J1:
        # Se usa .copy() para evitar referencias de memoria vinculadas
        Pop.cromo[Parents.index1, :] = Offspring.crom1.copy()
        Pop.J[Parents.index1] = Offspring.J1
        Pop.R[Parents.index1] = Offspring.R1
        
    # Si el Hijo 2 tiene mejor aptitud (mayor J) que el Padre 2, lo reemplaza
    if Offspring.J2 > Parents.J2:
        Pop.cromo[Parents.index2, :] = Offspring.crom2.copy()
        Pop.J[Parents.index2] = Offspring.J2
        Pop.R[Parents.index2] = Offspring.R2
        
    return Pop