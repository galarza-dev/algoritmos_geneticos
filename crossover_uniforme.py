import numpy as np

def crossover_uniforme(Offspring, Parents):
    """
    Cruzamiento Uniforme (Uniform Crossover)
    """
    longitud = len(Parents.crom1)
    
    # Generar máscaras aleatorias de 0s y 1s del tamaño del cromosoma.
    # np.random.randint(2, size=X) genera un arreglo con valores 0 y 1.
    mascara1 = np.random.randint(2, size=longitud)
    mascara2 = np.random.randint(2, size=longitud)
    
    # np.where(condicion, valor_si_verdadero, valor_si_falso)
    # Esto reemplaza por completo el bucle 'for' de MATLAB.
    # Si mascara == 1, toma el gen de Parents.crom1, si no, toma de Parents.crom2.
    Offspring.crom1 = np.where(mascara1 == 1, Parents.crom1, Parents.crom2)
    Offspring.crom2 = np.where(mascara2 == 1, Parents.crom1, Parents.crom2)
    
    return Offspring