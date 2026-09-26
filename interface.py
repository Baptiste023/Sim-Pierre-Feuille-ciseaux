import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
from constante import *

def afficher_entites(screen,Liste_entite,assets):
    for entite in Liste_entite:
        entite.dessiner(screen,assets)

def afficher_terrain(screen):
    rectangle(Largeur - 2 * Marge, Hauteur_zone - 2 * Marge, screen, Marge, Hauteur_stat + Marge)

def afficher_stat(screen,police,nb_pierre,nb_feuille,nb_ciseau,assets):

    text_pierre=police.render(": "+ str(nb_pierre), True, Noir)
    text_feuille = police.render(": "+ str(nb_feuille), True, Noir)
    text_ciseau = police.render(": "+ str(nb_ciseau), True, Noir)

    nouvelle_dimention1 = pygame.transform.scale(assets["Pierre"], (taille_crown, taille_crown))
    nouvelle_dimention2 = pygame.transform.scale(assets["Ciseau"], (taille_crown, taille_crown))
    nouvelle_dimention3 = pygame.transform.scale(assets["Feuille"], (taille_crown, taille_crown))


    screen.blit(text_ciseau,(100,30))
    screen.blit(nouvelle_dimention2,(100-taille_crown,30))
    screen.blit(text_pierre,(230,30))
    screen.blit(nouvelle_dimention1,(230-taille_crown,30))
    screen.blit(text_feuille,(380,30))
    screen.blit(nouvelle_dimention3,(380-taille_crown,30))

def charger_assets():
    curent_dir = os.path.dirname(os.path.abspath(__file__))
    asset_dir = os.path.join(curent_dir,"assets")

    assets = {}

    image_Papier= pygame.image.load(os.path.join(asset_dir, "001-paper-scroll.png"))
    assets["Feuille"]= pygame.transform.scale(image_Papier,(2*rayon,2*rayon))

    image_Ciseaux= pygame.image.load(os.path.join(asset_dir, "008-scissors-1.png"))
    assets["Ciseau"]= pygame.transform.scale(image_Ciseaux,(2*rayon,2*rayon))

    image_Pierre= pygame.image.load(os.path.join(asset_dir, "001-stone.png"))
    assets["Pierre"] = pygame.transform.scale(image_Pierre,(2*rayon,2*rayon))

    image_victoire= pygame.image.load(os.path.join(asset_dir, "002-crown-1.png"))
    assets["Crown"] = pygame.transform.scale(image_victoire,(taille_crown,taille_crown))

    return assets

def afficher_victoire(screen,espece_gagnante, assets,police):

    x = (Largeur- taille_crown)/2
    y = 75
    x_2_point= x+ taille_crown+ 15

    nouvelle_dimention=pygame.transform.scale(assets[espece_gagnante],(taille_crown,taille_crown))

    screen.blit(assets["Crown"], (x, y))
    separateur=police.render(":", True, Noir)
    screen.blit(separateur, (x_2_point, y))
    screen.blit(nouvelle_dimention, (x+taille_crown+20, y))

def creer_graphique(Histo_feuille,Histo_ciseau,Histo_pierre):

    plt.figure(figsize = (5,4))
    plt.plot(Histo_feuille,color="red")
    plt.plot(Histo_ciseau,color="blue")
    plt.plot(Histo_pierre,color="green")
    buffer=io.BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    plt.clf()
    return buffer

