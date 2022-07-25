from collections import deque

print("Voici un tuple:")
tuple1=(1,2,3)
print(tuple1)
tuple1=deque(tuple1)
print(type(tuple1))
liste=[1,8,0,5]
print(liste)
print(type(deque(liste)))