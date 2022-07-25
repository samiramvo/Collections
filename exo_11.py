import collections

tuple1=(1,2,3)
tuple1=collections.deque(tuple1)
print("Tuple1:",tuple1)
print("Tuple1 id",id(tuple1))
print("Element1:",id(tuple1[0]))

tuple2=tuple1.copy()

print("Tuple2",tuple2)
print("Tuple2 id:",id(tuple2))
print("Element1:",id(tuple2[0]))