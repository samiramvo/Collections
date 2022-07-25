
from collections import Counter
liste=[2,7,9,6,4,2,9,5,2,3,2,2,2]
liste1=Counter(liste)
print(liste1)
liste1=reversed(liste1.items())
print(tuple( max(liste1.items())))