import pygame.draw


# Terrain

Hauteur_zone=540

def rectangle(largeur_rect, hauteur_rect, screen,x,y):
 pygame.draw.rect(screen,(0,0,0),(x, y, largeur_rect,hauteur_rect),1)


# Zone stat

Hauteur_stat =120

# Fentre

Hauteur= Hauteur_zone +  Hauteur_stat
Largeur= 500
Marge = 10

FPS=60

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

rayon_apparition=80
espace_min_spwan=10


dico_couleur_entite={"Pierre": Rouge,"Feuille":Bleu,"Ciseau":Vert}

dico_relation_entite={"Pierre":"Ciseau","Ciseau":"Feuille","Feuille":"Pierre"}

taille_crown=50

# Texte

Taille_texte= 15




