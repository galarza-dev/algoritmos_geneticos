import numpy as np

def mut_uniforme(Offspring):
    """
    Mutación Uniforme (Uniform Mutation)
    """
    longitud = len(Offspring.crom1)
    
    # Generamos las máscaras aleatorias de 0s y 1s del tamaño del cromosoma
    mascara1 = np.random.randint(2, size=longitud)
    mascara2 = np.random.randint(2, size=longitud)
    
    # Indexación booleana: 
    # Seleccionamos solo las posiciones donde la máscara es igual a 1
    # y aplicamos la inversión (1 - valor_actual) a esos genes específicos.
    # Esto reemplaza por completo los bucles 'for' y los 'if' de MATLAB.
    Offspring.crom1[mascara1 == 1] = 1 - Offspring.crom1[mascara1 == 1]
    Offspring.crom2[mascara2 == 1] = 1 - Offspring.crom2[mascara2 == 1]
    
    return Offspring