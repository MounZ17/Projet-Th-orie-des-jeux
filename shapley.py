from itertools import combinations
import math
import bisect


def P_set(List):    #fonction qui nous permet de creer une liste avec toutes les combinaisons possibles en utilisant "combinations" de "itertools"
    PS = [list(j) for i in range(len(List)) for j in combinations(List, i+1)]
    return PS

def main():
    #Defintion du nombre de joueurs et le tableau des characteristiques 
    n = 3
    characteristic_function = [6,12,42,12,42,42,42]      #Definition des characteristiques des joueurs et les coalitions
    List = list([i for i in range(n)])
    N = P_set(List)                 
 
    shapley_values = []
    for i in range(n):
        shapley = 0
        for j in N:
            if i not in j:
                Z = len(j)              #Nombre de joueurs dans une coalition
                Cui = j[:]                  
                bisect.insort_left(Cui,i)     
                l = N.index(j)
                k = N.index(Cui)
                temp = float(float(characteristic_function[k]) - float(characteristic_function[l])) *\
                           float(math.factorial(Z) * math.factorial(n - Z - 1)) / float(math.factorial(n))
                shapley += temp


        Z = 0
        Cui = [i]
        k = N.index(Cui)
        temp = float(characteristic_function[k]) * float(math.factorial(Z) * math.factorial(n - Z - 1)) / float(math.factorial(n))
        shapley += temp
        shapley_values.append(shapley)

    print (shapley_values)

if __name__ == '__main__':
    main()