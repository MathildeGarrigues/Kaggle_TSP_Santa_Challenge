#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random
import math
import pandas as pd

# Paramètres de génération.
RAYON = 100.0
path = 'cities.csv'

class Data:
    # TSP.
    tab_villes = []

    def import_cities(self, path):
        """Import cities of the problem"""
        labeled_cities = pd.read_csv(path)
        for i in range(100):
            x = labeled_cities.iloc[i,1]
            y = labeled_cities.iloc[i,2]
            self.tab_villes.append([x, y])

    def generer_villes_cercle(self, n):
        """Génération de n villes sur le cercle (TSP)."""
        for i in range(n):
            theta = random.uniform(0, 2 * math.pi)
            x = RAYON * math.cos(theta)
            y = RAYON * math.sin(theta)
            self.tab_villes.append([x, y])
            
    
    def afficher_villes(self):
        """Affichage des villes."""
        print("*** Villes ***")
        for i in range(len(self.tab_villes)):
            print("Ville ", i, " : " + repr(self.tab_villes[i]), sep="")
        

    def __init__(self, path):
        self.import_cities(path)
        self.afficher_villes()
        
