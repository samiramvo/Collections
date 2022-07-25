from collections import Counter

print("Entrez une chaine de caractère:")

chaine=str(input())

chaine=list(chaine)
print(Counter(chaine).most_common())