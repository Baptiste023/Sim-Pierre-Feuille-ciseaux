import os
import matplotlib
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


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
    y = 25
    x_2_point= x+ taille_crown+ 15

    nouvelle_dimention=pygame.transform.scale(assets[espece_gagnante],(taille_crown*echelle,taille_crown*echelle))

    screen.blit(assets["Crown"], (x, y))
    separateur=police.render(":", True, Noir)
    screen.blit(separateur, (x_2_point, y))
    screen.blit(nouvelle_dimention, (x+taille_crown+20, y))

def creer_graphique(Histo_feuille,Histo_ciseau,Histo_pierre):

    couleur_feuille =  conversion(dico_couleur_entite["Feuille"])
    couleur_pierre = conversion(dico_couleur_entite["Pierre"])
    couleur_ciseau = conversion(dico_couleur_entite["Ciseau"])

    curent_dir = os.path.dirname(os.path.abspath(__file__))
    asset_dir = os.path.join(curent_dir, "assets")

    plt.figure(figsize = (5,4))



    image_pierre= plt.imread(os.path.join((asset_dir),"001-stone.png"))
    icone_pierre=OffsetImage(image_pierre,zoom=0.05)
    affichage_pierre=AnnotationBbox(icone_pierre,(0.52,0.90),xycoords='axes fraction')
    plt.gca().add_artist(affichage_pierre)
    image_ciseau = plt.imread(os.path.join((asset_dir), "008-scissors-1.png"))
    icone_ciseau = OffsetImage(image_ciseau, zoom=0.05)
    affichage_ciseau = AnnotationBbox(icone_ciseau,(0.32,0.90),xycoords='axes fraction')
    plt.gca().add_artist(affichage_ciseau)

    image_feuille = plt.imread(os.path.join((asset_dir), "001-paper-scroll.png"))
    icone_feuille = OffsetImage(image_feuille, zoom=0.05)
    affichage_feuille = AnnotationBbox(icone_feuille, (0.1,0.90),xycoords='axes fraction')
    plt.gca().add_artist(affichage_feuille)

    plt.plot(Histo_feuille, color=couleur_feuille,label="Feuille")
    plt.plot(Histo_ciseau,color=couleur_ciseau,label="Ciseau")
    plt.plot(Histo_pierre,color=couleur_pierre,label="Pierre")

    ax = plt.gca()
    ax.plot([0.2,0.25],[0.88,0.88],color=couleur_feuille,transform=ax.transAxes)
    ax.plot([0.40, 0.45], [0.88, 0.88], color=couleur_ciseau, transform=ax.transAxes)
    ax.plot([0.60, 0.65], [0.88, 0.88], color=couleur_pierre, transform=ax.transAxes)

    buffer=io.BytesIO()
    plt.savefig(buffer,format="png")
    buffer.seek(0)
    plt.close()

    return buffer

def conversion(couleur):
    nouvelle_couleur=[]
    for i in couleur:
        nouvelle_couleur.append(i/255)

    return tuple(nouvelle_couleur)
