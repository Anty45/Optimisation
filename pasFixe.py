import numpy as np

#  Calcul du gradient

def gradient(x1,x2) :
    composante1 = -2*((1-x1)+200*x1*(x2-(x1*x1)))
    composante2 = 200*(x2-(x1*x1))
    return(np.array([composante1,composante2]))

#Calcul de la direction
def direction(gradient):
    return(gradient/gradient.T.dot(gradient))

def norme(gradient):
    return(gradient.T.dot(gradient))


def optimum(x0, teta, d, grad):
    k=0
    val_norme = norme(grad)
    if val_norme < 0.01:
        return (print(x0))
    xk_plus_un = x0
    while (norme(grad) > 0.001):
        xk_plus_un = xk_plus_un + teta * d
        grad = gradient(xk_plus_un[0], xk_plus_un[1])
        d = direction(grad)
        n = norme(grad)

    print("Valeur optimal : ")
    return (print(xk_plus_un))

x0 = np.array([-1,1])
grad = gradient(-1,1)
d=direction(grad)
optimum(x0,-0.700,d,grad)

"""
1-

Progamation par la méthode PFP 
Pour la fonciton Rosebrock avec x0=(-1,1)
avec pas fixe
Quel pas teta conseilleriez vous?

2- Idem avec minimisation unidirectionelle

a- Méthode de Newton
    a l'itération de l'algorithme PFP 
        xk,dk
        teta_zero = 0 
        teta_k+1 = teta_k - g'(teta_k)/g''(teta_k)
    Pour le critere d'arret sur le teta on peut utiliser :
        |teta_k - teta_k+1 | < 0.1.teta_k
b- Méthode de dichotomie (par la méthdoe de la fonction dorée ) 



"""