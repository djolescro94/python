age = int(input("Quel âge as-tu ? "))
if age < 18 and age > 0:
    print("Tu as ",age, " ans, donc tu ne peux pas rentrer")
elif age >= 18:
    print("Tu as ",age, " ans, donc tu peux rentrer")
else:
    print("tu as saisis un nombre incorrect ! FDP", age)
