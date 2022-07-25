from collections import Counter
import re
print("Entrez un paragraphe:")
para=str(input())
word=re.findall('\w+',para)

print(list(Counter(word).most_common(10)))