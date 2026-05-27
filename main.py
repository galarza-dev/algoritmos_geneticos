import numpy as np
import matplotlib.pyplot as plt
import random
from FunObj import FunObj
from random_sel import random_sel
from fps_sel import fps_sel
from rank_lineal import rank_lineal
from rank_exp import rank_exp
from sel_rank import sel_rank
from crossover_uno import crossover_uno
from crossover_dos import crossover_dos
from crossover_uniforme import crossover_uniforme
from mut_uno import mut_uno
from mut_dos import mut_dos
from mut_uniforme import mut_uniforme
from rem_al import rem_al
from rem_peor import rem_peor
from rem_ambos import rem_ambos

# Clase auxiliar para replicar las estructuras de MATLAB
class Struct:
    pass

# %% PARÁMETROS DEL ALGORITMO
Pop = Struct()
Pop.D = 10
Pop.N = 20
Pop.MaxGen = 1500

# %% INICIALIZACIÓN DE VARIABLES DE LA POBLACIÓN
Pop.J = np.zeros(Pop.N)          # inicializo J
Pop.R = np.zeros(Pop.N)          # inicializo R
Pop.cromo = np.zeros((Pop.N, Pop.D), dtype=int) # inicializo Población
Pop.J_graf = np.zeros(Pop.MaxGen) # inicializo Jgraf
Pop.exper = 50
Pop.rep = np.zeros(Pop.exper)

# %% INICIALIZACIÓN DE LA ESTRUCTURA PARENTS
Parents = Struct()
Parents.crom1 = np.zeros(Pop.D, dtype=int) # inicializo Padre 1
Parents.crom2 = np.zeros(Pop.D, dtype=int) # inicializo Padre 2
Parents.index1 = 0 # inicializo Índice Padre 1
Parents.index2 = 0 # inicializo Índice Padre 2
Parents.J1 = 0.0   # inicializo Aptitud Padre 1
Parents.J2 = 0.0   # inicializo Aptitud Padre 2
Parents.R1 = 0.0   # inicializo Restricción Padre 1
Parents.R2 = 0.0   # inicializo Restricción Padre 2

# %% INICIALIZACIÓN DE LA ESTRUCTURA OFFSPRING
Offspring = Struct()
Offspring.crom1 = np.zeros(Pop.D, dtype=int) # inicializo Hijo 1
Offspring.crom2 = np.zeros(Pop.D, dtype=int) # inicializo Hijo 2
Offspring.J1 = 0.0 # inicializo Aptitud Hijo 1
Offspring.J2 = 0.0 # inicializo Aptitud Hijo 2
Offspring.R1 = 0.0 # inicializo Restricción Hijo 1
Offspring.R2 = 0.0 # inicializo Restricción Hijo 2

# %% PARÁMETROS PARA SELECCIÓN
Param_sel = Struct()
Param_sel.Tipo = 2       # 1-random, 2-FPS, 3-LRS, 4-ERS
Param_sel.r = 0.99       # parámetro para ERS
Param_sel.cmax = 1.6     # parámetro para LRS
Param_sel.cmin = 2 - Param_sel.cmax # parámetro para LRS
Param_sel.Pa = np.zeros(Pop.N)      # inicializo Probabilidad acumulada

# %% PARÁMETROS PARA CRUZAMIENTO
Param_cros = Struct()
Param_cros.Tipo = 3      # 1-un punto, 2-dos puntos, 3-uniforme
Param_cros.PC = 0.6      # Probabilidad de cruzamiento

# %% PARÁMETROS PARA MUTACIÓN
Param_mut = Struct()
Param_mut.Tipo = 2       # 1-un gen, 2-dos genes, 3-máscara
Param_mut.PM = 0.8       # Probabilidad de mutación

# %% PARÁMETROS PARA REEMPLAZO
Param_rem = Struct()
Param_rem.Tipo = 2       # 1-aleatorio, 2-peor rendimiento, 3-ambos padres

# =====================================================================
# BUCLE DE EXPERIMENTOS
# =====================================================================
for k in range(Pop.exper):
    # %% INICIALIZACIÓN DE LA POBLACIÓN
    # Genera matriz de ceros y unos de tamaño (Pop.N, Pop.D)
    Pop.cromo = np.random.randint(2, size=(Pop.N, Pop.D))
    
    # %% EVALUACIÓN DE LA POBLACIÓN INICIAL
    for i in range(Pop.N):
        # NOTA: FunObj debe estar definida y retornar (Jfun, Rfun)
        Jfun, Rfun = FunObj(Pop.cromo[i, :]) 
        Pop.J[i] = Jfun
        Pop.R[i] = Rfun
    
    # %% FASE ITERATIVA
    for g in range(Pop.MaxGen):
        
        # MECANISMO DE SELECCIÓN
        if Param_sel.Tipo == 1:
            Parents = random_sel(Pop)
        elif Param_sel.Tipo == 2:
            Parents = fps_sel(Pop, Parents)
        elif Param_sel.Tipo == 3:
            Param_sel = rank_lineal(Pop, Param_sel)
            Pop, Parents = sel_rank(Pop, Parents, Param_sel)
        elif Param_sel.Tipo == 4:
            Param_sel = rank_exp(Pop, Param_sel)
            Pop, Parents = sel_rank(Pop, Parents, Param_sel)
        else:
            print('error de selección')
            
        # %% CRUZAMIENTO
        if random.random() <= Param_cros.PC:
            if Param_cros.Tipo == 1:
                Offspring = crossover_uno(Offspring, Parents)
            elif Param_cros.Tipo == 2:
                Offspring = crossover_dos(Offspring, Parents)
            elif Param_cros.Tipo == 3:
                Offspring = crossover_uniforme(Offspring, Parents)
            else:
                print('error de opción de cruzamiento')
        else:
            # En Python es importante usar .copy() para evitar referencias no deseadas en arreglos de numpy
            Offspring.crom1 = Parents.crom1.copy()
            Offspring.crom2 = Parents.crom2.copy()
            
        # %% MUTACIÓN
        if random.random() <= Param_mut.PM:
            if Param_mut.Tipo == 1:
                Offspring = mut_uno(Offspring)
            elif Param_mut.Tipo == 2:
                Offspring = mut_dos(Offspring)
            elif Param_mut.Tipo == 3:
                Offspring = mut_uniforme(Offspring)
            else:
                print('error de opción de mutación')
                
        # %% REEMPLAZO
        Jfun, Rfun = FunObj(Offspring.crom1)
        Offspring.J1 = Jfun
        Offspring.R1 = Rfun
        
        Jfun, Rfun = FunObj(Offspring.crom2)
        Offspring.J2 = Jfun
        Offspring.R2 = Rfun
        
        if Param_rem.Tipo == 1:
            Pop = rem_al(Offspring, Pop)
        elif Param_rem.Tipo == 2:
            Pop = rem_peor(Offspring, Pop, Parents)
        elif Param_rem.Tipo == 3:
            Pop = rem_ambos(Offspring, Pop, Parents)
        else:
            print('error de opción de reemplazo')
            
        # %% PRESENTACION DE RESULTADOS
        # np.argmax devuelve el índice del valor máximo
        IBest = np.argmax(Pop.J) 
        JBest = Pop.J[IBest]
        XBest = Pop.cromo[IBest, :]
        RBest = Pop.R[IBest]
        
        print('----------------------------------')
        print(f'g: {g + 1}') # g+1 para que coincida con la vista de MATLAB (1-based)
        print(f'JBest: {JBest}')
        print(f'RBest: {RBest}')
        print(f'[X]: {XBest}')
        
        Pop.J_graf[g] = JBest
        
    Pop.rep[k] = JBest 
    
    # Gráfica de convergencia (se sobreescribirá en la misma figura en cada iteración del experimento si no se limpia)
    gen = np.arange(1, Pop.MaxGen + 1)
    plt.plot(gen, Pop.J_graf, linewidth=2)
    plt.xlabel('g', fontsize=16)
    plt.ylabel('J($)', fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)

# Mostrar la primera figura con todas las curvas de convergencia
plt.show()

# %% Histograma final
plt.figure()
# bins ajustados simulando el BinWidth=5 de MATLAB
bins = np.arange(min(Pop.rep), max(Pop.rep) + 5, 5) 
plt.hist(Pop.rep, bins=bins, edgecolor='black')
plt.xlabel('JBest')
plt.ylabel('Frecuencia')
plt.title('Histograma de resultados')
plt.show()