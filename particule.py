import math
from constante import*


class Entite :
    def __init__(self, espece, x, y, vitesse, angle ):
        self.x = x
        self.y = y
        self.espece = espece
        self.vitesse = vitesse
        self.angle= angle
        self.vitesse_x=vitesse*math.cos(angle)
        self.vitesse_y=vitesse*math.sin(angle)

    def dessiner(self,screen,assets):
        screen.blit(assets[self.espece],(self.x-rayon, self.y-rayon))

    def nouvelle_position(self):

        self.rebond()
        self.x += self.vitesse_x
        self.y += self.vitesse_y

    def rebond(self):
        if self.x-rayon<=Marge:
            self.vitesse_x = - self.vitesse_x
            self.x = Marge + rayon
        if self.x + rayon >= Largeur - Marge:
            self.vitesse_x = - self.vitesse_x
            self.x = (Largeur - Marge) - rayon

        if self.y+rayon>=Hauteur-Marge:
            self.vitesse_y = - self.vitesse_y
            self.y = (Hauteur - Marge) - rayon

        if self.y - rayon <=Hauteur_stat + Marge:
            self.vitesse_y = - self.vitesse_y
            self.y = (Hauteur_stat + Marge) + rayon


    def collision(self,autre):

        distance = math.sqrt((self.x - autre.x)**2 + (self.y - autre.y)**2)

        if distance <= 2*rayon:
            dx, dy = self.x - autre.x, self.y - autre.y
            norme = (dx/distance, dy/distance)
            chevauchement = 2*rayon - distance
            self.x+= (norme[0]*chevauchement)/2
            self.y+=(norme[1]*chevauchement)/2
            autre.x-= (norme[0]*chevauchement)/2
            autre.y-=(norme[1]*chevauchement)/2

            if dico_relation_entite[self.espece] == autre.espece :
               autre.espece = self.espece
            elif dico_relation_entite[autre.espece] == self.espece :
                self.espece = autre.espece

            if self.espece == autre.espece :
                self.vitesse_x =-self.vitesse_x
                self.vitesse_y =-self.vitesse_y
                autre.vitesse_x =- autre.vitesse_x
                autre.vitesse_y =- autre.vitesse_y


            return True
        else:
            return False
