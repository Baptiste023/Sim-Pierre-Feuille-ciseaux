import pygame.draw


# Terrain

Hauteur_zone=1680

def rectangle(largeur_rect, hauteur_rect, screen,x,y):
 pygame.draw.rect(screen,(0,0,0),(x, y, largeur_rect,hauteur_rect),1)


# Zone stat

Hauteur_stat =240

# Fentre

Hauteur= Hauteur_zone +  Hauteur_stat
Largeur= 1080
Marge = 10

# Taille d'affichage à modifier avant de lancer la simulation.
# La scène ci-dessus sert de référence pour garder les mêmes proportions.
Largeur_fenetre = 1080
Hauteur_fenetre = 1920

FPS=24

# Couleur

Gris = (240, 230, 215)
test1=(210, 225, 235)
test2=(180, 165, 145)

Blanc = (255,255,255)
Bleu=(0,0,255)
Rouge=(255,0,0)
Vert=(0,255,0)
Noir=(0,0,0)

# Entité

rayon=10

rayon_apparition=500
espace_min_spwan=10


dico_couleur_entite={"Pierre": Rouge,"Feuille":Bleu,"Ciseau":Vert}

dico_relation_entite={"Pierre":"Ciseau","Ciseau":"Feuille","Feuille":"Pierre"}

taille_crown=50

# Texte

Taille_texte= 15




