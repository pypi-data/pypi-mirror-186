import numpy as np

def somme(n):
    """
    Calcule la somme des entiers de 1 à n.
    """
    T = np.linspace(1, n, num=n, dtype="int")
    return T.sum()
