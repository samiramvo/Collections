from collections import deque

dq=deque(['Red','Green','White'])
print(dq)
print("Ajout à gauche:")
dq.appendleft('Pink')
print(dq)
print("Ajout à droite:")
dq.append('Orange')
print(dq)
print("Retrait de la dorite:")
dq.pop()
print(dq)
print("Enlever de la gauche:")
dq.popleft()
print(dq)
print("Inverser le deque:")
print(list(reversed(dq)))