from collections import deque

print("Entrez le nombre de sujets:")
suj=int(input())
list_suj=[]
for i in range(suj):
    print("Nom du sujet et notes:")
    nom=str(input())
    list_suj.append(nom)

for j in list_suj:
    print(j)