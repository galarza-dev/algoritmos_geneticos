import numpy as np
from ruleta import ruleta

# Definición local de Struct para replicar el comportamiento de MATLAB
# (Si tienes todas tus funciones en un solo archivo, no necesitas volver a declararla)
class Struct:
    pass

def fps_sel(Pop, Parents):
    """
    Selección basada en Fitness (FPS - Roulette Wheel Selection)
    """
    # Se calcula la probabilidad de cada individuo. 
    # Usamos np.sum para la suma total del fitness de la población.
    suma_J = np.sum(Pop.J)
    
    # Prevención de división por cero por si la población inicial tiene un fitness total de 0
    if suma_J == 0:
        P_fps = np.ones(Pop.N) / Pop.N 
    else:
        P_fps = Pop.J / suma_J
        
    # Creamos un Struct local para Param_sel igual que lo hace MATLAB implícitamente
    Param_sel = Struct()
    Param_sel.Pa = np.cumsum(P_fps)
    
    # Inicializamos los índices con el mismo valor para forzar la entrada al bucle while
    Parents.index1 = 0
    Parents.index2 = 0
    
    # Bucle para asegurar que no se seleccione al mismo padre dos veces
    while Parents.index1 == Parents.index2:
        # NOTA: Asegúrate de que la función 'ruleta' devuelva un índice basado en 0 (estilo Python)
        Parents.index1 = ruleta(Param_sel)
        Parents.index2 = ruleta(Param_sel)
        
    # Asignación de cromosomas. Se utiliza .copy() para evitar que 
    # la modificación de los hijos afecte a los padres en la memoria.
    Parents.crom1 = Pop.cromo[Parents.index1, :].copy()
    Parents.crom2 = Pop.cromo[Parents.index2, :].copy()
    
    # Asignación de los valores de Aptitud (J) y Restricción (R)
    Parents.J1 = Pop.J[Parents.index1]
    Parents.J2 = Pop.J[Parents.index2]
    
    Parents.R1 = Pop.R[Parents.index1]
    Parents.R2 = Pop.R[Parents.index2]
    
    return Parents