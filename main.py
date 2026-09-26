from interface import*
from simulation import*


pygame.init()
screen = pygame.display.set_mode((Largeur,Hauteur))
pygame.display.set_caption('SIM Guerre PFC')
assets= charger_assets()



clock = pygame.time.Clock()
police=pygame.font.SysFont("Arial", Taille_texte)
police2=pygame.font.SysFont("Arial", taille_crown)

zones = gerer_apparition()
Liste_entite = []
Liste_position = []
Histo_pierre=[]
Histo_ciseau=[]
Histo_feuille=[]

for espece in zones:
    x_zone, y_zone = zones[espece]
    for _ in range(15):
        x, y = position_dans_zones(x_zone, y_zone,Liste_position)
        Liste_entite.append(Entite(espece,x,y,7,random.uniform(0, 2*math.pi)))
        Liste_position.append((x,y))

running = True
win = False
creer_graph=False
surface_graph=None

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)
    pygame.display.flip()

    if win:
       screen.fill(Blanc)
       afficher_victoire(screen,win,assets,police2)

       if not creer_graph:
           buffer_graph=creer_graphique(Histo_feuille, Histo_pierre, Histo_ciseau)
           surface = pygame.image.load(buffer_graph)
           creer_graph=True

       screen.blit(surface,(25,300))


    else:

        screen.fill(Blanc)

        afficher_terrain(screen)

        gerer_colision(Liste_entite)

        nb_ciseau, nb_feuille, nb_pierre=gerer_stat(Liste_entite,Histo_pierre,Histo_ciseau,Histo_feuille)


        win=condition_victoire(nb_ciseau, nb_feuille, nb_pierre)


        afficher_stat(screen,police2,nb_pierre,nb_feuille,nb_ciseau,assets)

        gerer_position(Liste_entite)

        afficher_entites(screen,Liste_entite,assets)





pygame.quit()



