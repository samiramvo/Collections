from collections import Counter

liste=['PHP','PHP','PHP','Python','JS','Python','Python','PHP','Python']

print(Counter(liste).most_common(1)[0][0])