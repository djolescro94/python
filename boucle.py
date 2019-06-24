nombre = int(input("Saisissez votre nombre de tour actuel : "))

while nombre < 0 or nombre > 100:
    print("Saisie incorrecte")
    nombre = int(input("Saisissez votre nombre de tour actuel : "))
    
while nombre <= 100 and nombre >= 0:
    if nombre == 1:
        print("j'ai fait ", nombre ,"tour !")
        nombre = nombre + 1
    else:
        print("j'ai fait ", nombre ,"tours !")
        nombre = nombre + 1
