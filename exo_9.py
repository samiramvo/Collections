from collections import deque

print("Nombres pairs:")
pairs=[2,4,8,10]
print(pairs)
pairs=deque(pairs)
print("Plus de nombres pairs:")
plus_pairs=[12,14,16,18,20]
plus_pairs=deque(plus_pairs)
pairs.extend(plus_pairs)
print(pairs)