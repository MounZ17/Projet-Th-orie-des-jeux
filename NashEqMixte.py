import random
import numpy as np
from scipy.optimize import linprog


'''
    cette fonction va nous permettre de créer notre matrice de jeu, de voir s'il 
    éxiste un point de selle (en stratégies pures) et de trouver un équilibre de nash en stratégie mixtes
'''
def NashEquilibriumZSG(): 
    '''
        Définition des stratégies des deux jouerus tels que: 
            - strat[0] -> Stratégies du joueur 1
            - strat[1] -> Stratégies du joueur 2
        
        Définition de la matrice de jeu en utilisant random.randInt() pour les coefficients afin 
        d'éviter que le jeu ne soit statique, sinon l'IA choisira chaque fois la même stratégie 
    '''     

    startegies = [['Rock', 'Paper', 'Scissor', 'Lizard', 'Spock'],
                  ['Rock', 'Paper', 'Scissor', 'Lizard', 'Spock']]
    
    a = random.randint(1, 500)  
    b = random.randint(1, 500)
    c = random.randint(1, 500)
    d = random.randint(1, 500)
    e = random.randint(1, 500)

    GameMatrix=  [np.array(  [[ 0, -b,  c,  d, -e],
                            [ a,  0, -c, -d,  e],
                            [-a,  b,  0,  d, -e],
                            [-a,  b, -c,  0,  e],
                            [ a, -b,  c, -d,  0]])]

    print(GameMatrix)
    
    '''
        Recherche du point de selle en calculant: 
            - le minmax de la matrice
            - le maxmin de la matrice 
            - Vérification de l'égalité afin de trouver l'existence du point de selle ou non
                Si oui, on récupère la position et on l'affiche

    '''
    minimums = np.amin(GameMatrix[0], axis=1)
    maximums = np.amax(GameMatrix[0], axis=0)
 
    if np.max(minimums) != np.min(maximums) :
        print("Il n'existe pas de point de selle dans cette matrice, il faut trouver l'équilibre en stratégies mixtes")
    else :
        PointSelle = "{"
        indices = np.argwhere(GameMatrix[0] == np.min(maximums))
        for row in indices :
            PointSelle += "(" + str(row[0]+1) + "," +str(row[1]+1) + ")"
            PointSelle += "}"
            print("Les points de selle : ", PointSelle)

    '''
        Calcul de la distribution des probabilités (Énumération de support) pour J1 et J2,
        Nous retiendrons uniquement les résultats concernant le joueur 2 car la stratégie finale
        du joueur 1 sera fixée par le joueur ( Vous ).
    '''

    tab = np.ones(GameMatrix[0].shape[0]+1)
    tab[0] = 0
    c = -1*(1-tab)  

    """
        Définition des équations et résolution grâce au linprog de scipy qui nous permet de gérer
        ce qui concerne la programmation linéaire. 
        Il s'agit d'une alternative au module "eq" de la classe "Symbol"
    """
     
    A_ub = np.concatenate((np.ones((1, GameMatrix[0].shape[1])), -1*GameMatrix[0]), axis=0).T
    B_ub = np.zeros(GameMatrix[0].shape[1])
    A_eq = np.expand_dims(tab, axis=0)
    B_eq = np.ones(1)
    bounds = [(None, None)] + [(0,1)]* GameMatrix[0].shape[0]
    result = linprog(c, A_ub=A_ub, b_ub=B_ub, A_eq=A_eq, b_eq=B_eq, bounds=bounds)
    ValeurP1, sigma1 = result.x[0], result.x[1:]

    """
        Préparation des valeurs d'entrées pour la fonction linprog
        Elle nous donne en résultat la distribution des probabilités de chacune des stratégies
    """

    tab = np.ones(GameMatrix[0].shape[1]+1)
    tab[0] = 0
    c = (1-tab)
    A_ub = np.concatenate((-1*np.ones((GameMatrix[0].shape[0], 1)), GameMatrix[0]), axis=1)
    B_ub = np.zeros(GameMatrix[0].shape[0])
    A_eq = np.expand_dims(tab, axis=0)
    A_eq = np.concatenate((A_eq, 1-A_eq), axis=0)
    B_eq = np.array([1, ValeurP1]) 
    bounds = [(None, None)] + [(0,1)]*GameMatrix[0].shape[1]
    result = linprog(c, A_ub=A_ub, b_ub=B_ub, A_eq=A_eq, b_eq=B_eq, bounds=bounds)
    sigma2 = result.x[1:]
    print(sigma2[0])

    print("L'equilibre de nash  : {", tuple(sigma1), "," ,tuple(sigma2), "}")
    return sigma2,startegies

"""
    La fonction suivante va nous permettre de choisir en fonction de l'utilitié calculée pour 
    le  joueur 2, la meilleure de ses stratégies jouables en vérifiant quelle est la valeur maximale 
    dans le tableau de distributions.
"""
def ChoixStrat():
    max = -999
    index = 0
    sigma2,startegies = NashEquilibriumZSG()
    for i in range(len(sigma2)):
        if sigma2[i] >= max :
            max = sigma2[i]
            index = i
    print(sigma2)
    return startegies[1][index]

print(ChoixStrat())