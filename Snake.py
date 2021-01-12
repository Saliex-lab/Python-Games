import sys,random
import pygame

# On creer la class snake
class Snake:

# initialise toutes les variables de la  class snake grace au __init__
    def __init__(self):

        self.ecran = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Snake')
        self.jeu_en_cours = True
        self.snake_position_x = 300
        self.snake_position_y = 300
        self.snake_direction_x = 0
        self.snake_direction_y = 0
        self.time=pygame.time.Clock()
        self.pomme_position_x = random.randrange(30,770,10)
        self.pomme_position_y = random.randrange(30, 570, 10)
        self.pomme_taille = 5
        self.snake_taille = []
        self.grandeur = 0
        self.score = 0
        self.temps = 8

# cette fonction permet de gerer les evenements et certains composants du jeu
    def fonction_principale (self):


# cette boucle permet d'afficher la fenetre tant qu'elle n'est pas fermé
        while self.jeu_en_cours:
            self.time.tick(self.temps)
            for evenement in pygame.event.get():
                #print(evenement)
                if evenement.type == pygame.QUIT:
                    sys.exit()

            # creer les evenements qui permetent de bouger le serpent
                if evenement.type == pygame.KEYDOWN:

                    if evenement.key == pygame.K_d:
                       self.snake_direction_x = 10
                       self.snake_direction_y = 0

                    if evenement.key == pygame.K_q:
                        self.snake_direction_x = -10
                        self.snake_direction_y = 0

                    if evenement.key == pygame.K_s:
                        self.snake_direction_x = 0
                        self.snake_direction_y = 10

                    if evenement.key == pygame.K_z:
                        self.snake_direction_x = 0
                        self.snake_direction_y = -10




            # bouger le serpent
            self.snake_position_x += self.snake_direction_x
            self.snake_position_y += self.snake_direction_y
            #print(self.snake_position_x,self.snake_position_y)


            # couleur de l'ecran
            self.ecran.fill((0,0,0))

            #score
            font = pygame.font.SysFont("arial",20)
            text = font.render("Score:",True,(255,255,255))
            text2 = font.render("{}".format(str(self.score)), True, (255, 255, 255))
            self.ecran.blit(text,(5,5))
            self.ecran.blit(text2,(65, 6))


            #creer le serpent
            Green = (0, 255, 0)
            P_snake=pygame.draw.rect(self.ecran, Green, (self.snake_position_x, self.snake_position_y, 5, 5))
            print(P_snake)

            #creer la limite

            self.limite()

            #creer la condition de la limite
            if self.snake_position_x < 0 or self.snake_position_x > 800 or self.snake_position_y < 0 or self.snake_position_y > 600:
                sys.exit()

            #creer la pomme

            yellow = (255, 255, 0)
            pygame.draw.rect(self.ecran, yellow, (self.pomme_position_x, self.pomme_position_y, self.pomme_taille,self.pomme_taille))

            #condition de la pomme
            if self.snake_position_x == self.pomme_position_x and self.snake_position_y == self.pomme_position_y :
                self.pomme_position_x = random.randrange(30, 770, 10)
                self.pomme_position_y = random.randrange(30, 570, 10)

                self.grandeur += 1
                self.score +=1
                self.temps += 1

            #creer un liste qui va recenser la tete du serpent

            tete_du_serpent=[]
            tete_du_serpent.append(self.snake_position_x)
            tete_du_serpent.append(self.snake_position_y)

            self.snake_taille.append(tete_du_serpent)

            for taille_serpent in self.snake_taille:
                pygame.draw.rect(self.ecran, Green, (taille_serpent[0],taille_serpent[1],self.pomme_taille,self.pomme_taille))
                print(taille_serpent)


            if len(self.snake_taille) > self.grandeur:
                self.snake_taille.pop(0)
                print(self.snake_taille)
            #si le serpent se mord la queue le jeu s'arrete

            for taille_serpent in self.snake_taille [:-1]:
                if tete_du_serpent == taille_serpent:
                    sys.exit()

            #mettre à jour en continue l'écran
            pygame.display.flip()


    def limite (self):

        pygame.draw.rect(self.ecran, (255,0,0), (0, 0, 800, 600),3)


# cette instance permert d'initialiser les fonctions de pygame, d'appeler la fonction principale de la class Snake , et enfin quitter pygame
if __name__ == '__main__':

    pygame.init()
    Snake().fonction_principale(),
    pygame.quit()