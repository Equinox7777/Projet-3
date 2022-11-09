#DEBUT
def salaireNet(brut, coeff):
    return brut - brut* coeff

def salaireParSeconde(salaireHoraire, heurParJourOuvre, jourOuvreParAn):
    #Calculer mon salaire annuel
    salaireAnnuel = salaireHoraire * heurParJourOuvre * jourOuvreParAn
    #Calculer le nb de secondes dans une année
    nbSecondeParAn = 365*24*60*60
    #Je pose et retourne la division
    return salaireAnnuel / nbSecondeParAn
#FIN

#Definir une fonction withdrawFees qui retir un pourcentage a un total en fonction d'un total et d'un pourcentage
def withdrawFees(total, percent):
    #Definir fees en fonction d'un total et d'un pourcentage
    fees= total * (percent/100)
    #soustraire fees au total
    result = total - fees
    #retourner la valeur obtenue
    return result

#Définir une fonction qui retourne le salaire net en fonction du salaire brut (float) et du secteur d'activité (isPublic > booleen)
def calculBrutEnNet(salaireBrut, isPublic):
    #Si je suis un travailleur du secteur publique 
    if isPublic:
        #Alors je soustrais 15% de mon salaire Brut
        salaireNet = salaireBrut - (salaireBrut * (15/100))
    #Sinon : je suis un travailleur du secteur privé
    else :
        #Alors je soustrais 23%
        salaireNet = salaireBrut - (salaireBrut / (23/100))
    #Retourner salaireNet  
    return salaireNet

#Definir un fonction qui divise x par y et retourne le resultat
def divide(x, y):
    #Si y est égale à zéro
    if y == 0 :
        #Alors écrire un message d'erreur
        print("divisé par 0 ?! boloss")
    #Sinon
    else:
        #Alors retourner x / y    
        return x / y


def input():
    #Renvoie un caractere de type string au hasard




#Eercices:
    #Faire un mini jeu qui affiche un message lorque input renvoie le bon caractere
    # le caractere doit etre parametrable

#Definir une fonction avec un caractere gagnat
#On choisis un cartactere
    #tant que le caractere n'est pas le gagant
        #alors on en choisi un autre
#Si le caractere est identique au gagnant
    #Alors on gagne
