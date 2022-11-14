from tkinter import *


#Définition des Variables globales

drapeau = True

#Définition des Fonctions
def afficher(event) :
    global drapeau
    abscisse = event.x
    ordonnee = event.y
    l = (ordonnee-2)//100                    # Ligne du clic
    c = (abscisse-2)//100                    # Colonne du clic
    if drapeau:                              # drapeau == True
        dessin.create_line(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, fill = 'blue')
        dessin.create_line(100*c+8, 100*l+96, 100*c+96, 100*l+8, width = 5, fill = 'blue')
        message.configure(text='Aux ronds de jouer')
    else:
        dessin.create_oval(100*c+8, 100*l+8, 100*c+96, 100*l+96, width = 5, outline = 'red')
        message.configure(text='Aux croix de jouer')
    drapeau = not(drapeau)

#Création de la fenêtre
fen = Tk()
fen.title('Morpion')


#Création des zones de texte
message=Label(fen, text='Aux croix de jouer')
message.grid(row = 0, column = 0, columnspan=2, padx=3, pady=3, sticky = W+E)


#Création des boutons
bouton_quitter = Button(fen, text='Quitter', command=fen.destroy)
bouton_quitter.grid(row = 2, column = 1, padx=3, pady=3, sticky = S+W+E)
bouton_reload = Button(fen, text='Recommencer', command=fen.event_generate)
bouton_reload.grid(row = 2, column = 0, padx=3, pady=3, sticky = S+W+E)



#Création du canevas
dessin=Canvas(fen, bg="white", width=301, height=301)
dessin.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)


#La grille
lignes = []
for i in range(4):
    lignes.append(dessin.create_line(0, 100*i+2, 303, 100*i+2, width=3))
    lignes.append(dessin.create_line(100*i+2, 0, 100*i+2, 303, width=3))


#Evenements
dessin.bind('<Button-1>', afficher)


#Programme principal
fen.mainloop()