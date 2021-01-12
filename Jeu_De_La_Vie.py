import sys,random
import pygame
import numpy as np

class Grille :
    def __init__(self):
        self.Tableau = []



    def Afficher (self):
        self.Tableau.append(3)
        print(self.Tableau)



class Jeu :
    def __init__(self):
#On creer la fenetre pygame
        self.ecran = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Jeu de la Vie")
        self.jeu_en_marche = True
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.grille = Grille()



    def fonction_principale(self):
    #Boucle qui permet d'afficher la fenetre indéfiniment jusqu'a fermer la fenetre
        while self.jeu_en_marche:

            for evenement in pygame.event.get():

                if evenement.type == pygame.QUIT:
                    sys.exit()

            self.ecran.fill(self.white)
            self.grille.Afficher()

            pygame.display.flip()





if __name__ == '__main__':
    pygame.init()
    Jeu().fonction_principale()
    pygame.quit()