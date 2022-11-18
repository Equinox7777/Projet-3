#DEBUT
#On importe la librarie random pour pouvoir utiliser l'aléatoire dans le programme

    #On demande au joueur si il veut jouer au jeu avec un input (oui/non) et on l'inseret dasn une boucle while

        #Création d’une liste d’options "choices" jouable 

        #L’ordi joue aléatoirement  dans la liste "choice", compris entre 0 et 2
        #le joueur rentre une des trois données possible : Pierre, Feuille, Ciseaux
        #tant que le joueur ne perd pas

            #Si le choix du joueur est égale à celui de l'ordi
                #Afficher "Égalité"

            #Sinon le joueur est égale à Pierre
                #Si l'ordi est égale à Papier
                    #Afficher "Vous avez perdu…"  l'ordi "à recouvert" le joueur
                #Sinon
                    #Afficher "Vous avez gagné !" le joueur "à écrasé" l'ordi

            #Sinon le joueur est égale à Papier
                #Si l'ordi est égale à Ciseaux
                    #Afficher "Vous avez perdu…"  l'ordi "à coupé" le joueur
                #Sinon
                    #Afficher "Vous avez gagné !" le joueur "à recouvert" l'ordi

            #Sinon le joueur est égale à Ciseaux
                #Si l'ordi est égale à Pierre
                    #Afficher "Vous avez perdu…"  l'ordi "à écrasé" le joueur
                #Sinon
                    #Afficher "Vous avez gagné !" le joueur "à coupé" l'ordi

                #Joueur égale faux
                #L’ordi joue aléatoirement dans la liste "choice", compris entre 0 et 2

    #Sinon
        #Afficher "A la prochaine !"
#FIN
