# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 16:06:57 2017
@author: Loïc Masure
Importation et génération du graphe abstrait.
"""
import pandas as pd
import numpy as np


def distance(A, B, l_rayon):
    """
    Calcule la distance (non-euclidienne) entre deux produits dans le magasin.
    A, B :  Produits dont on calcule la distance (x_A, y_A), (x_B, y_B).
    l :     Longueur des rayons pour calculer une distance réaliste.
    """
    xA, yA = A
    xB, yB = B

    if xA == xB:
        # Les deux articles sont dans le même rayon.
        return np.abs(yA - yB)
    else:
        # Les deux articles ne sont pas dans le même rayon.
        # Deux chemins sont possibles pour changer de rayon: passer par chaque
        # extrémité.
        chemin = min(yA + yB, 2*l_rayon - yA - yB)
        return np.abs(xA - xB) + chemin


table = pd.read_excel("PlanMagasin.xlsx", index_col=0)
l_rayon = table["Ordonnée"].max()
d = {}
for produit in table.index:
    d[produit] = (table["Abscisse"][produit], table["Ordonnée"][produit])

mat = np.zeros((len(d), len(d)))
for i, ind in enumerate(d.keys()):
    mat[i] = [distance(d[ind], d[j], l_rayon) for j in d.keys()]
