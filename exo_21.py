from collections import Counter
from webbrowser import get

print("Entrez une chaine:")
chaine=str(input())
chaine_ct=Counter(chaine)
print("Le caractere le plus courant est:",max(Counter(chaine),chaine_ct.get))
print("Le caractère le moins courant est:",min(Counter(chaine),chaine_ct.get))