import random

# Definición local de Struct por si ejecutas esta función en un archivo independiente
class Struct:
    pass

def random_sel(Pop):
    """
    Selección Aleatoria
    """
    Parents = Struct()
    
    # random.randint(a, b) incluye ambos extremos, así que usamos Pop.N - 1
    num_crom1 = random.randint(0, Pop.N - 1)
    num_crom2 = random.randint(0, Pop.N - 1)
    
    # Bucle para asegurar que no se seleccione al mismo padre dos veces
    while num_crom1 == num_crom2:
        num_crom2 = random.randint(0, Pop.N - 1)
        
    Parents.index1 = num_crom1
    Parents.index2 = num_crom2
    
    # Asignación de cromosomas (usando .copy() por seguridad con arreglos de NumPy)
    Parents.crom1 = Pop.cromo[Parents.index1, :].copy()
    Parents.crom2 = Pop.cromo[Parents.index2, :].copy()
    
    # Asignación de las aptitudes (J) y restricciones (R)
    Parents.J1 = Pop.J[Parents.index1]
    Parents.J2 = Pop.J[Parents.index2]
    
    Parents.R1 = Pop.R[Parents.index1]
    Parents.R2 = Pop.R[Parents.index2]
    
    return Parents