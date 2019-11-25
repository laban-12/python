# operatuers de comparaison
# > : plus grand que
# < : plus petit que
# >= : plus grand ou egal a
# <= : plus petit ou egal a
# == : est egale a 
# != : est different que

#les conditions 
# if () : SI la condition est vrai 
# elif () : SINON SI cette condition est vrai 
# else : SINON, par defaut tu fais...

age = 16 

if (age < 12):
    print("enfant") 
elif(age <18):
    print("ado") 
else :
    print("adulte")


    print("---------------------")
    # les boucles
    # while () : tant que la condition est vrai...
    # for () : POUR CHAQUE element de ma liste ...

    compteur = 1 

    while (compteur <= 10):
        print(compteur)
        compteur = compteur +1

        maListe = ["c'est", "enfin", "fini"]
        for element in maListe:
            print(element)