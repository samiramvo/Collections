from collections import deque
print("Faire des rotations sur un deque avec des nombres positifs")
print("Deque avant rotation:")
liste=[2,3,4,7]
dq=deque(liste)
print(dq)
print("Deque après une rotation:")
dq.rotate()
print(dq)
print("Deque après une deuxième rotation:")
dq.rotate(2)
print(dq)