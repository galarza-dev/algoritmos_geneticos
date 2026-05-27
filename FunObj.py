import numpy as np

def FunObj(cromo_i):
    """
    # VERSIÓN COMENTADA (Problema de Presupuesto)
    # presupuesto = 3200
    # C = np.array([100, 120, 90, 80, 110, 130, 140, 150, 100, 120])
    # O = np.array([500, 600, 400, 450, 550, 700, 650, 750, 600, 800])
    # P = np.array([150, 200, 125, 175, 180, 250, 200, 275, 175, 300])
    # Jfun = np.sum((P * C - O) * cromo_i)
    # Rfun = np.sum(O * cromo_i)
    # if Rfun > presupuesto:
    #     Jfun = 0.1
    # return Jfun, Rfun
    """
    
    # VERSIÓN ACTIVA (Problema de Energía)
    Emax = 950
    q = np.array([50, 60, 45, 40, 55, 70, 80, 65, 50, 75])
    e = np.array([120, 150, 90, 100, 130, 160, 200, 140, 110, 180])
    m = np.array([20, 18, 22, 19, 17, 16, 15, 21, 23, 14])
    
    # Cálculo de la función de aptitud (Fitness) y la restricción
    Jfun = np.sum((m * q) * cromo_i)
    Rfun = np.sum(e * cromo_i)
    
    # Castigo duro si viola la restricción de energía máxima
    if Rfun > Emax:
        Jfun = 0.1     
        
    return Jfun, Rfun