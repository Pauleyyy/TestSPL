#Primzahlen uebung
zahl = input("Bitte eine Zahl eingeben: ")
zahl1 = int(zahl)
a = False
for i in range (1,zahl):
    if(zahl %i == 0):
        a=True
    else:
        a=False

if(a==True):
    print("Ist EINE Primzahl")
if(a==False):
    print("Ist KEINE Primzahl")




