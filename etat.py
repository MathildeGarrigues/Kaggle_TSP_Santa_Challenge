#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random as rd
import data_tsp as dt
import math
import test
IS_MINIMISATION = True
path = 'cities.csv'
# Dimension du problème.
DIMENSION = 100
alpha = 0.2

class Etat:
    def __init__(self, dim_etat):
        self.vecteur = [i for i in range(dim_etat)]
        self.i = 0
        self.j = 0
        self.villes = dt.Data(path)
        self.x = [self.villes.tab_villes[i][0] for i in range(len(self.villes.tab_villes))]
        self.y = [self.villes.tab_villes[i][1] for i in range(len(self.villes.tab_villes))]
        
    def init_aleatoire(self):
        """Initialisation aléatoire de l'état."""
        pass
    
        
    def afficher(self):
        """Affichage."""
        return str(self.vecteur)
    
    def generer_voisin2(self):
        """Générer un état voisin."""
        self.i = rd.randint(0, DIMENSION-1)
        self.j = rd.randint(0, DIMENSION-1)
        while self.j == self.i:
            self.j = rd.randint(0, DIMENSION-1)
            
        self.vecteur[self.i], self.vecteur[self.j] = self.vecteur[self.j], self.vecteur[self.i]

    def generer_voisin(self):
        self.i = rd.randint(0, DIMENSION-2)
        self.j = rd.randint(self.i+1, DIMENSION-1)
        mean = int((self.j-self.i)/2)
        for k in range(mean):
            self.vecteur[self.i+k], self.vecteur[self.j-k] =  self.vecteur[self.j-k], self.vecteur[self.i+k]            
            
    def come_back(self):
        mean = int((self.j-self.i)/2)
        for k in range(mean):
            self.vecteur[self.i+k], self.vecteur[self.j-k] =  self.vecteur[self.j-k], self.vecteur[self.i+k]            
        
    def come_back2(self):
        """Retour à l'état précédent."""
        self.vecteur[self.i], self.vecteur[self.j] = self.vecteur[self.j], self.vecteur[self.i]
    
    def calcul_critere(self, temperature_initiale, temperature):
        """Évaluation des objectifs."""
        somme = float(0)
        k = 0
        for index in range(len(self.vecteur)-1):
            i = self.vecteur[index]
            ip1 = self.vecteur[index+1]
            somme = somme + math.sqrt((self.x[ip1] - self.x[i])**2 + (self.y[ip1] - self.y[i])**2)
            if [i%10 == j for j in range(len(self.vecteur)-1)] and test.is_prime(i) :
                somme = somme * 1.1
                k+=1
        somme += math.sqrt((self.x[self.vecteur[-1]] - self.x[self.vecteur[0]])**2 + (self.y[self.vecteur[-1]] - self.y[self.vecteur[0]])**2)

        return somme if k<1 else somme*(1+alpha*k)


