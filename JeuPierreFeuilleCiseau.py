import random

COUP = ("Pierre", "Feuille", "Ciseaux")
#Demande au joueur si il veut jouer
while input("Voulez vous jouez ? (oui/non): ").lower() != "non":
 
    print("\n------------------------------------")
    print("Le jeu du: Pierre - Feuille - Ciseaux")
    print("------------------------------------\n")
 
    a = int(input("Choisissez un chiffre:\n0: Pierre\n1: Feuille\n2: Ciseaux\n-> "))
    b = choice(range(3))
 
    print("\n{} VS {}".format(COUP[a], COUP[b]))
    if a == b:
        print("ÉGALITÉ\n")
    elif (a>b and b+1==a) or (a<b and a+b==2):
        print("VOUS GAGNEZ\n")
    else:
        print("VOUS PERDEZ\n")
else:
    print("Bye Bye")
