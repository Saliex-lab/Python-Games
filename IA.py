from random import *

caratère = ['1','2','3','4','5','6','7','8','9','0',
             'a','z','e','r','t','y','u','i','o','p','q','s','d','f','g','h','j','k','l','m','w','x','c','v','b','n',
             'A','Z','E','R','T','Y','U','I','O','P','Q','S','D','F','G','H','J','K','L','M','W','X','C','V','B','N',
             '+','-','*','/','.','$','^','ù','*','!',':',')','=',',','?',';','§','µ','%','£','¨','&','é','"','{','[',
             '-','è','_','ç','à']

longueur = int(input('Entrer la longueur du mot de passe'))
nb_mdp = int(input('Combien de mdp ?'))

def mdp (longeur):
    mdp=str()
    shuffle(caratère)
    for x in range (longueur):
        mdp+=caratère[x]

    print (mdp)

for x in range (nb_mdp):
    mdp (longueur)
input()