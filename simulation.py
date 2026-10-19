import random
from particule import *
from constante import *


def gerer_colision (Liste_entite):
    for i in range(len(Liste_entite)):
        for j in range(len(Liste_entite)):
            if i <= j:
                continue

            else:
                Entite.collision(Liste_entite[i], Liste_entite[j])

def gerer_position (Liste_entite):
    for entite in Liste_entite:
        entite.nouvelle_position()

def gerer_stat(Liste_entite,Histo_pierre,Histo_ciseau,Histo_feuille):
    nb_pierre = 0
    nb_feuille = 0
    nb_ciseau = 0

    for entite in Liste_entite:
        if entite.espece == "Ciseau":
            nb_ciseau += 1

        if entite.espece == "Feuille":
            nb_feuille += 1
        if entite.espece == "Pierre":
            nb_pierre += 1

    Histo_pierre.append(nb_pierre)
    Histo_ciseau.append(nb_ciseau)
    Histo_feuille.append(nb_feuille)

    return nb_ciseau, nb_feuille, nb_pierre

def gerer_apparition():
    rayon_position_apparition=170
    y_centre = Hauteur_stat + Hauteur_zone / 2
    x_centre = Largeur / 2

    positions = []

    for indice in range(3):
        angle = -math.pi / 2 + indice * (2 * math.pi / 3)

        x_zone = x_centre + rayon_position_apparition * math.cos(angle)
        y_zone = y_centre + rayon_position_apparition * math.sin(angle)

        # Descendre les deux zones du bas
        if indice != 0:
            y_zone += 50

        positions.append((x_zone, y_zone))

    random.shuffle(positions)

    zones = {}

    for espece, position in zip(
        ["Ciseau", "Feuille", "Pierre"],
        positions
    ):
        zones[espece] = position

    return zones

def position_dans_zones(x_zone, y_zone,Liste_position):

    while True:
        angle = random.uniform(0, 2 * math.pi)
        distance = rayon_apparition * math.sqrt(random.uniform(0, 1))
        x = x_zone + distance * math.cos(angle)
        y = y_zone + distance * math.sin(angle)
        trop_proche = False
        for position in Liste_position:
            px, py = position
            dist = math.sqrt((px - x) ** 2 + (py - y) ** 2)
            if dist < 2* rayon + espace_min_spwan :
                trop_proche = True

        if not trop_proche:
            Liste_position.append((x, y))
            break
    return (x,y)

def condition_victoire(nb_ciseau, nb_feuille, nb_pierre):
    if nb_pierre == 0 and nb_feuille == 0 :
        return "Ciseau"
    elif nb_pierre == 0 and nb_ciseau == 0 :
        return "Feuille"
    elif nb_feuille == 0 and nb_ciseau == 0 :
        return "Pierre"
