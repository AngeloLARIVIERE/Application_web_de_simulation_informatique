from __future__ import annotations

import math
import sys

# On initialise une variable pour savoir si une chaîne de caractères est un nombre ou pas
ISSTRING = False
# Initialisation de la borne inférieure l'intégrale
A = -math.inf
# On essaie d'obtenir les deux arguments M et sigma à partir des arguments de la ligne de commande
# sys.argv est une liste qui contient les arguments de la ligne de commande

try:
    M = int(sys.argv[1]) #On récupère le premier argument (indice 0) qui est M
    sigma = int(sys.argv[2]) # On récupère le deuxième argument (indice 1) qui est sigma
except:
    M=0
    sigma=1
    pass
# Fonction de la loi normale
# x: le point pour lequel on veut calculer la probabilité P(X<=x) de la variable aléatoire X suivant cette loi normale
# M: moyenne de la loi normale (par défaut 0)
# sigma: écart-type de la loi normale (par défaut 1)
def f(x,M,sigma):
    """La déclaration de la fonction qui calcule l'intégrale de la densité de probabilité de la loi normale pour une variable x donnée"""
    # math est une bibliothèque Python qui fournit des fonctions mathématiques
    return (1.0 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - M) / sigma) ** 2)

#Fonction pour l'intégration par rectangles gauches
# t: borne supérieure de l'intégrale, à partir de laquelle on va calculer l'intégrale
# n: nombre de rectangles utilisés pour calculer l'aire sous la courbe (plus n est grand, plus l'approximation est précise)
# M: moyenne de la loi normale (par défaut 0)
# sigma: écart-type de la loi normale (par défaut 1)
def rectangles_gauches(t: int, n: int, m=M,sigma=sigma) -> float | str:
    """La fonction pour calculer l'intégrale par la méthode des rectangles gauches et qui vérifie les erreurs possibles"""
    # On vérifie que sigma n'est pas inférieur à 0 
    if sigma <= 0:
        return "ERREUR: sigma doit etre strictement plus grand que 0"
    # On vérifie que n est positif pour que la méthode fonctionne
    if n <= 0:
        return "ERREUR : n doit etre strictement plus grand que 0"
    # On vérifie que t n'est pas inférieur à 0
    if t <= 0:
        return "ERREUR: t doit etre strictement plus grand que 0"

    integrale = 0   # Pour stocker la somme des aires des rectangles
    largeur = t/n   # Largeur de chaque rectangle
    hauteur = 0     # Pour stocker la somme des hauteurs des rectangles
    for k in range(0, n): # Pour faire la somme des hauteurs de 0 à n-1
        hauteur += f(k*t/n,m,sigma) # Calcul de la hauteur de chaque rectangle en sommant les valeurs de la fonction aux points correspondants
    aire = largeur * hauteur # Calcul de l'aire de chaque rectangle
    integrale += aire        # Somme des aires des rectangles

    return round(integrale + 0.5, 5) # Arrondi de l'intégrale à 5 décimales

# Fonction pour l'intégration par rectangles droites
def rectangles_droites (t: int, n: int, m=M,sigma=sigma) -> float | str:
    """La fonction pour calculer l'intégrale par la méthode des rectangles droites et pour vérifier les erreurs possibles"""
    # On vérifie que sigma n'est pas inférieur à 0 
    if sigma <= 0:
        return "ERREUR: sigma doit etre strictement plus grand que 0"
    # On vérifie que n est positif pour que la méthode fonctionne
    if n <= 0:
        return "ERREUR: n doit etre strictement plus grand que 0"
    # On vérifie que t n'est pas inférieur à 0
    if t <= 0:
        return "ERREUR: t doit etre strictement plus grand que 0"

    integrale = 0  # Pour stocker la somme des aires des rectangles
    largeur = t/n  # Largeur de chaque rectangle
    hauteur = 0    # Pour stocker la somme des hauteurs des rectangles
    for k in range(1, n+1):  # Pour faire la somme des hauteurs de 1 à n
        hauteur += f(k*t/n,m,sigma)   # Calcul de la hauteur de chaque rectangle
    aire = largeur * hauteur  # Calcul de l'aire de chaque rectangle
    integrale += aire         # Somme des aires des rectangles

    return round(integrale + 0.5, 5)  # Arrondi de l'intégrale à 5 décimales

#Intégration par rectangles médians
def rectangles_medians(t: int, n: int, m=M,sigma=sigma) -> float | str:
    """La fonction pour calculer l'intégrale par la méthode des rectangles droites et pour vérifier les erreurs possibles: sigma, n, et t doivent être strictement supérieur à 0"""

    if sigma <= 0:
        return "ERREUR: sigma doit etre strictement plus grand que 0"
    if n <= 0:
        return "ERREUR: n doit etre strictement plus grand que 0"
    if t <= 0:
        return "ERREUR: t doit etre strictement plus grand que 0"

    integrale = 0 # Initialisation de l'intégrale à 0
    largeur = t/n # Calcul de la largeur de chaque rectangle
    hauteur = 0   # Initialisation de la hauteur à 0
    largeur2 = (1/2) * largeur  # Calcul de la moitié de la largeur
    # Boucle pour calculer la hauteur de chaque rectangle
    for k in range(0, n):
        hauteur += f(k*largeur + largeur2,m,sigma)
    aire = largeur * hauteur  # Calcul de l'aire de chaque rectangle
    integrale += aire # Ajout de l'aire à l'intégrale

    return round(integrale + 0.5, 5)  # Arrondi du résultat à 5 décimales

#Intégration par méthode de trapèze
def trapèze(t: int, n: int, m=M,sigma=sigma) -> float | str:
    """La fonction pour calculer l'intégrale par la méthode des trapèze et pour vérifier les erreurs possibles: sigma, n et t doivent être strictement supérieur à 0"""

    if sigma <= 0:
        return "ERREUR: sigma doit etre strictement plus grand que 0"
    if n <= 0:
        return "ERREUR: n doit etre strictement plus grand que 0"
    if t <= 0:
        return "ERREUR: t doit etre strictement plus grand que 0"

    integrale = 0 # Initialisation de l'intégrale à 0
    largeur = t/n # Calcul de la largeur de chaque trapèze
    largeur2 = (1/2) * largeur # Calcul de la moitié de la largeur
    hauteur=0  # Initialisation de la hauteur à 0
    # Boucle pour calculer la hauteur de chaque trapèze
    for k in range(1, n):
        hauteur += 2*f(k*largeur,m,sigma)
    aire = largeur2 * (hauteur + f(A,m,sigma) + f(t,m,sigma)) # Calcul de l'aire de chaque trapèze
    integrale += aire # Ajout de l'aire à l'intégrale

    return round(integrale + 0.5, 5) # Arrondi du résultat à 5 décimales

#Intégration par méthode de Simpson
def simpson(t: int, n: int, m=M,sigma=sigma) -> float | str:
    """La fonction pour calculer l'intégrale par la méthode de Simpson et pour vérifier les erreurs possibles: sigma, n et t doivent être strictement supérieur à 0"""
    if sigma <= 0:
        return "ERREUR: sigma doit etre strictement plus grand que 0"
    if n <= 0:
        return "ERREUR : n doit etre strictement plus grand que 0"
    if t <= 0:
        return "ERREUR: t doit etre strictement plus grand que 0"

    integrale = 0  # Initialiser de l'intégrale à 0
    largeur = (t)/n # Calculer la largeur de chaque rectangle
    largeur2 = (1/2) * largeur # Calculer la moitié de la largeur pour la somme2
    somme1 = 0 # Initialiser de la somme1 à 0
    somme2 = 0 # Initialiser de la somme2 à 0
    # Boucle pour alculer somme1 et somme2 en utilisant la méthode de Simpson
    for k in range(1, n):
        somme1 += f(k*largeur,m,sigma)
        somme2 += f((2*k+1)*largeur2,m,sigma)
        hauteur = f(A,m,sigma) + f(t,m,sigma) + 2*somme1 + 4*somme2 + f(largeur2,m,sigma)
    aire = (1/3) * largeur2 * hauteur # Calculer l'aire sous la courbe
    integrale += aire # Ajout de l'aire à l'intégrale
    
    return round(integrale + 0.5, 5) # Arrondi du résultat à 5 décimales

  

try:
    # Récupérer les arguments t et n depuis la ligne de commande
    n = int(sys.argv[3])
    t = int(sys.argv[4])
    # Récupérer le nom de la méthode d'intégration
    fct = sys.argv[5]
except:
    # Si aucun argument n'est fourni, utiliser des valeurs par défaut
    n = 10
    t = 1
    fct = 'Rectangles_gauches'

# Appeler la méthode d'intégration appropriée en fonction de la méthode sélectionnée
if fct == 'Rectangles_gauches':
    print(rectangles_gauches(t, n)) # arrondir le résultat à 5 décimales
elif fct == 'Rectangles_droites':
    print(rectangles_droites(t, n))
elif fct == 'Rectangles_médians':
    print(rectangles_medians(t, n))
elif fct == 'Simpson':
    print(simpson(t, n))
elif fct == "Trapèze":
    print(trapèze(t, n))

