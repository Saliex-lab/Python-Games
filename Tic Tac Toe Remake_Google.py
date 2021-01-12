import sys,random
import pygame
#Initialise pyagame

pygame.init()

#Initialise les differentes variable

height = 800
width = 800
couleur_ecran_cyan=(20, 189, 172)
couleur_raw_cyan=(25, 145, 135)
ecran = pygame.display.set_mode((height,width))
pygame.display.set_caption("Tic Tac Toe #Remake_Google")
ecran.fill(couleur_ecran_cyan)

jeu_en_cours = True

#Initialisation des fonctions

def grille ():
    for raw in range(1,3):
        for column in range (1,3):
            pygame.draw.line(ecran,couleur_raw_cyan,(180+raw*150,column*100),(180+raw*150,column*700),10)
            pygame.draw.line(ecran,couleur_raw_cyan,(raw*100,180+column*150),(raw*700,180+column*150),10)



grille()

while jeu_en_cours:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()








pygame.quit()