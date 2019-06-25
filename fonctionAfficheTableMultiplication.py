def afficherTableDeMultiplication(nombreSaisie, max=10):
    
    i = 1 #Variable d'incrémentation
    
    while i <= max:
        print(i,"*",nombreSaisie,"=", i * nombreSaisie)
        i = i + 1
########################################################################################################
nombreSaisie = int(input("Choisis un nombre pour voir sa table de multiplication (entre 1 et 100) : "))

while nombreSaisie < 1 or nombreSaisie > 100: #On s'assure que le nombre se trouve entre 1 et 100
    nombreSaisie = int(input("Tu n'as pas choisis un nombre entre 1 et 100, recommence : "))

max = int(input("Jusqu'à combien le multiplier : "))

while max < 1 or max > 100:
    max = int(input("Tu n'as pas choisis un nombre entre 1 et 100, recommence : "))


afficherTableDeMultiplication(nombreSaisie,max)

