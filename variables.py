# une variable est une "boite" qui contient une valeur
# celle ci peut changer au cours du programme

maVariable1 = 15 #nombre entier (int)
maVariable2 = "bonjour" #lettres (str)
maVariable3 = 0.5 # nombre decimal (float)

maListe = ["Bonsoir","salut", 42] # une liste contenannt 3 valeurs

# un dictionnaire contenat 3 valeur 
# sa particularite c'est que les index sont choisi par nous meme 

monDico =  {"a" : "rate", 
            "b" : 42 
            "c" : 0.1}
# Ici on affiche dans le terminal les valeurs et les types 
# de chaque variable (attention aux listes et dictionnaires)            
print(maVariable1, type(maVariable1))
print(maVariable2, type(maVariable2))
print(maVariable3, type(maVariable3))
print(maListe[0]), type(maListe))
print(monDico["a"]), type(monDico))

print("----------------------------")
#operateurs arithmetique
# + : addition
# - : soustraction
# / : division
# * : multiplication
# ** : eposant
# // : division entiere
# % : modulo 
print(maVariable1**2)
print(maVariable1//2)
print(maVariable1%2)


print(---------------------)
# operatuers de comparaison
# > : plus grand que
# < : plus petit que
# >= : plus grand ou egal a
# <= : plus petit ou egal a
# == : est egale a 
# != : est different que

if (5<10):
    print("vrai")
if(maVariable1==15):
    print("vrai")
if(15 != maVariable1): #celui ci sera ignore car ils sont egeaux
    print("vrai")    