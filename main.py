from time import sleep
import datetime
import os

from interface import*
from simulation import*

import sys
sys.path.append(r"") # Chemin de l'enregistreur
from Enregistreur import Enregistreur



os.environ["SDL_VIDEODRIVER"]="dummy"
pygame.init()
screen = pygame.display.set_mode((Largeur,Hauteur))
pygame.display.set_caption('SIM Guerre PFC')
assets= charger_assets()
clock = pygame.time.Clock()
police=pygame.font.SysFont("Arial", Taille_texte)
police2=pygame.font.SysFont("Arial", taille_crown)


def init():
    Liste_entite = []
    Liste_position = []
    Histo_pierre = []
    Histo_ciseau = []
    Histo_feuille = []
    date = datetime.datetime.now().strftime("%d_%m_%H_%M_%S")
    enregistreur = Enregistreur(Hauteur=Hauteur, Largeur=Largeur, FPS=FPS, chemin=f"PFC_{date}.mp4", duree_min=60)
    win = False
    creer_graph = False
    surface_graph = None
    ajout_enregistreur = False
    zones = gerer_apparition()
    for espece in zones:
        x_zone, y_zone = zones[espece]
        for _ in range(40):
            x, y = position_dans_zones(x_zone, y_zone, Liste_position)
            Liste_entite.append(Entite(espece, x, y, 12, random.uniform(0, 2 * math.pi)))
            Liste_position.append((x, y))

    return Liste_entite, enregistreur, creer_graph,surface_graph,ajout_enregistreur,Histo_pierre,Histo_ciseau,Histo_feuille, win



Liste_entite, enregistreur, creer_graph,surface_graph,ajout_enregistreur,Histo_pierre,Histo_ciseau,Histo_feuille,win =init()


running = True


while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)
    pygame.display.flip()



    if win:
       pygame.time.wait(1000)
       screen.fill(Blanc)
       afficher_victoire(screen,win,assets,police2)
       if not creer_graph:
           buffer_graph = creer_graphique(Histo_feuille, Histo_ciseau, Histo_pierre)
           surface = pygame.image.load(buffer_graph)
           creer_graph = True
       screen.blit(surface,((Largeur - surface.get_width())//2, 150))

       if not ajout_enregistreur:
           enregistreur.ajouter_image(screen)
           enregistreur.pause(10)
           assez_long=enregistreur.exporter()
           ajout_enregistreur = True
           if not assez_long :
               Liste_entite, enregistreur, creer_graph,surface_graph,ajout_enregistreur,Histo_pierre,Histo_ciseau,Histo_feuille,win =init()
           else:
               running = False


    else:

        screen.fill(Blanc)

        afficher_terrain(screen)

        gerer_colision(Liste_entite)

        nb_ciseau, nb_feuille, nb_pierre=gerer_stat(Liste_entite,Histo_pierre,Histo_ciseau,Histo_feuille)

        win=condition_victoire(nb_ciseau, nb_feuille, nb_pierre)

        afficher_stat(screen,police2,nb_pierre,nb_feuille,nb_ciseau,assets)

        gerer_position(Liste_entite)

        afficher_entites(screen,Liste_entite,assets)

        enregistreur.ajouter_image(screen)



if not  ajout_enregistreur:
    enregistreur.writer.close()
    os.remove(enregistreur.chemin)

pygame.quit()



