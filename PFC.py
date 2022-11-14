from random import choices
from random import randint
 
while input("On lance une partie ? (oui/non): ").lower() != "non":
 
    #Création d’une liste d’options jouable
    choices = ["Pierre", "Papier", "Ciseaux"]
 
    #L’ordi joue aléatoirement
    computer = choices[randint(0,2)]
 
    while player == False:
        #le joueur rentre une des trois données possible : Pierre, Feuille, Ciseau
        player = input("Que voulez vous jouer?\n")
        if player == computer:
            print("Égalité !")
        elif player == "Pierre":
            if computer == "Papier":
                print("Vous avez perdu…", computer,  "à recouvert", player)
            else:
                print("Vous avez gagné !", player,  "à écrasé", computer)
        elif player == "Papier":
            if computer == "Ciseaux":
                print("Vous avez perdu…", computer, "à coupé", player)
            else:
                print("Vous avez gagné !", player,  "à recouvert", computer)
 
        elif player == "Ciseaux":
            if computer == "Pierre":
                print("Vous avez perdu…", computer, "à écrasé", player)
            else:
                print("Vous avez gagné !", player, "à coupé", computer)
        else:
            print("Votre orthographe est incorrecte, vérifiez et réessayez !")
 
        player = False
 
        computer = choices[randint(0,2)]
 
else:
    print("A la prochaine !")
