#DEBUT
#On admet que la fonction "random" existe et qu'elle permet de récupérer un chiffre aléatoirement

#Liste des objets disponnible jouable nomé "jeu" qui contient ('pierre, papier, ciseaux, puit')
#Affiche "Bienvenue dans le jeu Pierre Feuille Ciseaux !"

#On crée la fonction "play"

    #on crée une variable "bot" qui choisie ici un objet aléatoirement dans la liste "jeu"
    
    #on crée une variable "choix" utilisant la fonction input pour récupérer ce que joue le joueur
    #si la variable "choix" est égale à celle du "bot"
        #afficher ('Egalité ! Le robot a choisit', bot, 'comme vous !')
    #sinon
        #si la variable "choix" est égale à 'pierre' et la variable "bot" est égale à 'feuille'
            #afficher ('Vous avez gagner ! La pierre écrase la', bot, '!')
        
        #sinon si la variable "choix" est égale à 'feuille' et la variable "bot" est égale à 'pierre'
            #afficher ('Vous avez perdu ! La feuille se fait écraser par la', bot)        
        
        #sinon si la variable "choix" est égale à 'ciseaux' et la variable "bot" est égale à 'pierre'
            #afficher ('Vous avez perdu ! La pierre écrase le ciseaux !')       
        
        #sinon si la variable "choix" est égale à 'pierre' et la variable "bot" est égale à 'ciseaux'
            #afficher ('Vous avez gagner ! La pierre écrase le ciseaux !')        
        
        #sinon si la variable "choix" est égale à 'ciseaux' et la variable "bot" est égale à 'feuille'
            #afficher ('Vous avez gagner ! Le ciseaux coupe la feuille !')        
        
        #sinon si la variable "choix" est égale à 'feuille' et la variable "bot" est égale à 'ciseaux'
            #afficher ('Vous avez perdu ! Le ciseaux coupe la feuille !')      
        
        #sinon si la variable "choix" est égale à 'pierre' et la variable "bot" est égale à 'puit'
            #afficher ('Vous avez perdu ! La pierre tombe dans le puit !')       
        
        #sinon si la variable "choix" est égale à 'puit' et la variable "bot" est égale à 'pierre'
            #afficher ('Vous avez gagner ! La pierre tombe dans le puit !')       
        
        #sinon si la variable "choix" est égale à 'feuille' et la variable "bot" est égale à 'puit'
            #afficher ('Vous avez gagner ! La feuille bouche le puit !')       
        
        #sinon si la variable "choix" est égale à 'puit' et la variable "bot" est égale à 'feuille'
            #afficher ('Vous avez perdu ! Le puit se fait boucher par la feuille !')       
        
        #sinon si la variable "choix" est égale à 'ciseaux' et la variable "bot" est égale à 'puit'
            #afficher ('Vous avez perdu ! Le puit écrase le ciseaux !')       
        
        #sinon si la variable "choix" est égale à 'puit' et la variable "bot" est égale à 'ciseaux'
            #afficher ('Vous avez gagner ! Le puit écrase le ciseaux !')
            
        #autre
            #afficher ('Une erreur est survenue !')
            
#éxécuter "rejouer"

#On crée la fonction "rejouer", on crée une variable "choix2" utilisant la fonction input pour récupérer ce que choisi le joueur
    #si le "choix2" est égale à 'Y'
        #éxécuter "play"
    #si le "choix2" est égale à 'y'
        #éxécuter "play"
    #si le "choix2" est égale à 'yes'
        #éxécuter "play"
    #sinon
        #"exit"

#éxécuter "play"        
#FIN
