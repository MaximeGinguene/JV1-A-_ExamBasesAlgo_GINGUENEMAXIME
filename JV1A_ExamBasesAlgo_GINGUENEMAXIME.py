#Exercice 1: Tris à bulles
# question 1,2 et 3
MyTable=[45,35,28,75]
stock= 0
for n in range(len(MyTable)-1): 
    for i in range(len(MyTable)-1): 
        if(MyTable[i] > MyTable[i+1]): 
            stock = MyTable[i]
            MyTable[i] = MyTable[i+1]
            MyTable[i+1] = stock

print(MyTable)

#Quesion 4: Cela est tres lent car il doit vérifier un à un si le nombre est plus petit que le nombre précédent.





#Exercice 2
#1. Écrire la fonctionnalité permettant d’afficher la grille de jeu.
#2. Écrire la fonctionnalité permettant de jouer un O ou un X.
#3. Écrire la fonctionnalité vérifiant si oui ou non l’un des joueurs a réussi à aligner 3
#symboles sur une ligne verticale, horizontale, diagonale.
#4. Écrire la fonctionnalité vérifiant si la grille est complète.
#5. Écrire un programme permettant de jouer à deux au Tic tac toe.
#6. Qu’aura-t-on besoin de faire, si on souhaite désormais programmer un jeu de
#Puissance 4 ?
#Répondez en commentaire

# On devra faire plus de case, mais aussi faire attention à ce que le pion aille là ou il faut par exemple si aucun pion n'est encore mis forceément le pion tombera sur la dernière ligne.





#Question 1:

# je créer mon tableau en print utilisant la fonction print, utilisation du pavé numérique pour faire son morpion:



Joueur1=("O")
Joueur2=("X")
ligne1= [7],[8],[9]
ligne2= [4],[5],[6]
ligne3= [1],[2],[3]

if Joueur1:
    input(7)
    




print("!___!___!___!")
print("!___!___!___!")
print("!___!___!___!")

#Qus=estion 2:

print("joueur 1 (X) à vous de jouer")

input('X')









