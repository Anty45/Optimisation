import numpy as np
import math
import pandas as pd
from matplotlib import pyplot as plt


#  Calcul du gradient

def gradient(x1, x2):
    composante1 = -2 * ((1 - x1) + 200 * x1 * (x2 - (x1 * x1)))
    composante2 = 200 * (x2 - (x1 * x1))
    return (np.array([composante1, composante2]))


# Calcul de la direction
def direction(gradient):
    return (-gradient / gradient.T.dot(gradient))


def norme(gradient):
    return (math.sqrt(gradient.T.dot(gradient)))


def optimum(x0, teta, grad0):
    val_norme = norme(grad0)
    if norme(grad0) < 0.01:  # On s'assure que le point d'initialisation n'est pas un point de convergeance
        print("Valeur optimale :")
        return (print(x0))

    score = []  # Liste qui contiendra le nombre d'itérations pour chaque descente avec un teta donné, fixe
    p = teta
    k = 0
    list_teta = [teta]
    for j in range(30):  # On choisit 30 valeurs en vue de teta en vue de réaliser nos tests
        p = p + 0.0001
        list_teta.append(p)

    grad = grad0  # Phase d'initialisation
    xk_plus_un = x0
    for val in list_teta:
        while (norme(grad) > 0.000001):  # Notre critère d'arret est un gradient presque nul
            xk_plus_un = xk_plus_un - val * grad0
            grad = gradient(xk_plus_un[0], xk_plus_un[1])
            if (k == 80000):
                break  # Cette condition est un seuil permettant de définir une divergeance de l'algorithme.
            k += 1
        score.append(k)  # On stocke le nombre d'itération réalisé pour le teta correspondant
        xk_plus_un = x0  # On réinitilise toutes nos variables pour la prochaine descente, avec un autre teta de la liste.
        grad = grad0
        k = 0
    best_teta = list_teta[score.index(min(score))]
    nbre_iteration = min(score)
    print("nombre d'itérations pour le teta optimal dans le cas d'une méthdoe à pas fixe : " + str(nbre_iteration))
    print("Valeur optimale  : " + str(best_teta))
    return xk_plus_un, list_teta, score


x0 = np.array([-1, 1])
grad = gradient(x0[0], x0[1])
score_list = []
list_teta = []
teta = 0
# teta,list_teta,score_list = optimum(x0,0.0001,grad)


# df = pd.DataFrame(list(zip(list_teta,score_list)),columns=['Valeurs teta tester','Nombres Iterations'])
# print(df)
"""
1-

Progamation par la méthode PFP 
Pour la fonciton Rosebrock avec x0=(-1,1)
avec pas fixe
Quel pas teta conseilleriez vous? 10^-3 , a 10^-2 le problème n'est plus localisé 
et dépasse le minimum. Les valeurs ne font que croitre jusqu'à exploser


2- Idem avec minimisation unidirectionelle

a- Méthode de Newton
    a l'itération de l'algorithme PFP 
        xk,dk
        teta_zero = 0 
        teta_k+1 = teta_k - g'(teta_k)/g''(teta_k)
    Pour le critere d'arret sur le teta on peut utiliser :
        |teta_k - teta_k+1 | < 0.1.teta_kc

"""


def optimum_Newton(grad):
    teta = 0
    while (norme(grad) > 0.000001):
        teta = teta
    return (0)


"""

b- Méthode de dichotomie (par la méthdode de la fonction dorée ) 

"""


def fonction_score(x1, x2):
    premier_terme = (1 - x1) * (1 - x1)
    second_terme = 100 * (x2 - x1) * (x2 - x1)

    return (premier_terme + second_terme)


def g(teta, x1, x2):
    d = gradient(x1, x2)
    return (fonction_score(x1 + (teta * d[0]), x2 + (teta * d[1])))


def section_doree(x):
    #  Initialisation

    alpha = (math.sqrt(5) / 2) - 1
    a = 0
    b = 0.0025
    c = alpha * a + (1 - alpha) * b
    d = a + b - c
    k = 0

    #  Iteration

    while (g(b, x[0], x[1]) - g(a, x[0], x[1]) > 0.00001):

        if g(c, x[0], x[1]) < g(d, x[0], x[1]):
            b = d
            d = c
            c = a + b - d
        else:
            a = c
            c = d
            d = a + b - c

    return ((a + b) / 2)


def optimum_section_doree(x0, teta, grad):
    if norme(grad) < 0.01:
        print("Valeur optimale :")
        return (print(x0))
    xk_plus_un = x0
    k = 0
    evol_norme = []
    iteration = []
    while (norme(grad) > 0.00001):
        xk_plus_un = xk_plus_un - teta * grad
        grad = gradient(xk_plus_un[0], xk_plus_un[1])
        teta = section_doree(xk_plus_un)
        k += 1
        evol_norme.append(norme(grad))
        if ((k % 10000) == 0):
            print(k)
            print(teta)
    return xk_plus_un, evol_norme


r, evol_norme = optimum_section_doree(x0, teta, grad)
print(r)

plt.plot(evol_norme)
plt.show()
