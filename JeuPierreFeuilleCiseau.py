#DEBUT
#Tant que 
    #On apporte la bibliothèque "random"  pour utiliser des choix aléatoires 
    #Création d’une liste d’options "choices" jouable 
    #L’ordi joue aléatoirement  dans la liste "choice", compris entre 0 et 2
    #le joueur rentre une des trois données possible : Pierre, Feuille, Ciseau
    #tant que le joueur ne perd pas
        #Si le choix du joueur est égale à celui de l'ordi
            #Afficher "Égalité"
        #Sinon le joueur est égale à Pierre
            #Si l'ordi est égale à Papier
                #Afficher "Vous avez perdu…"  l'ordi "à recouvert" le joueur
            #Sinon
                #Afficher "Vous avez gagné !" le joueur "à écrasé" l'ordi
        #Sinon le joueur est égale à Papier
            #Si l'ordi est égale à Ciseau
                #Afficher "Vous avez perdu…"  l'ordi "à coupé" le joueur
            #Sinon
                #Afficher "Vous avez gagné !" le joueur "à recouvert" l'ordi
        #Sinon le joueur est égale à Ciseau
            #Si l'ordi est égale à Pierre
                #Afficher "Vous avez perdu…"  l'ordi "à écrasé" le joueur
            #Sinon
                #Afficher "Vous avez gagné !" le joueur "à coupé" l'ordi
            #Joueur égale faux
            #L’ordi joue aléatoirement dans la liste "choice", compris entre 0 et 2
#Sinon
    #Afficher "A la prochaine !"
#FIN


import random

while input("On lance une partie ? (oui/non): ").lower() != "n":

    #Création d’une liste d’options jouable
    choices = ["Pierre", "Papier", "Ciseau"]

    #L’ordi joue aléatoirement
    computer = choices[random(0,2)]
    #le joueur rentre une des trois données possible : Pierre, Feuille, Ciseau
    player = input("Pierre, Papier, Ciseau?")

    while player == False:

        if player == computer:
            print("Égalité !")
        elif player == "Pierre":
            if computer == "Papier":
                print("Vous avez perdu…", computer,  "à recouvert", player)
            else:
                print("Vous avez gagné !", player,  "à écrasé", computer)
        elif player == "Papier":
            if computer == "Ciseau":
                print("Vous avez perdu…", computer, "à coupé", player)
            else:
                print("Vous avez gagné !", player,  "à recouvert", computer)

        elif player == "Ciseau":
            if computer == "Pierre":
                print("Vous avez perdu…", computer, "à écrasé", player)
            else:
                print("Vous avez gagné !", player, "à coupé", computer)
        else:
            print("Votre orthographe est incorrecte, vérifiez et réessayez !")

        player = False

        computer = choices[random(0,2)]
else:
    print("A la prochaine !")


#Definir une fonction...