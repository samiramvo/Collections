print("Entrez le nombre d'étudiants:")
etd=int(input())
liste=[]
for i in range(etd):
    print("Nom")
    nom=str(input())
    print("Notes:")
    notes=int(input())
    liste.append([nom,notes])
print(liste)