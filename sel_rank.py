import numpy as np
from ruleta import ruleta

def sel_rank(Pop, Parents, Param_sel):
    """
    Ordenamiento y Selección basada en Rango (LRS/ERS)
    """
    # np.argsort devuelve los índices que ordenarían el arreglo de menor a mayor.
    # Esto replica el comportamiento de [Pop.J, I] = sort(Pop.J) de MATLAB.
    I = np.argsort(Pop.J)
    
    # Reordenamos toda la población en base a esos índices para mantener la coherencia
    Pop.J = Pop.J[I]
    Pop.cromo = Pop.cromo[I, :]
    Pop.R = Pop.R[I]
    
    # Inicializamos los índices con el mismo valor para forzar la entrada al bucle while
    Parents.index1 = 0
    Parents.index2 = 0
    
    # Bucle para asegurar que no se seleccione al mismo padre dos veces
    # Se hace la llamada a la función ruleta() que ya tradujimos
    while Parents.index1 == Parents.index2:
        Parents.index1 = ruleta(Param_sel)
        Parents.index2 = ruleta(Param_sel)
        
    # Asignación de cromosomas. El .copy() evita referencias vinculadas en memoria.
    Parents.crom1 = Pop.cromo[Parents.index1, :].copy()
    Parents.crom2 = Pop.cromo[Parents.index2, :].copy()
    
    # Asignación de los valores de Aptitud (J) y Restricción (R)
    Parents.J1 = Pop.J[Parents.index1]
    Parents.J2 = Pop.J[Parents.index2]
    
    Parents.R1 = Pop.R[Parents.index1]
    Parents.R2 = Pop.R[Parents.index2]
    
    return Pop, Parents