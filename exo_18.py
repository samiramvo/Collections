from itertools import chain
A={"x":30,"y":45}
B={"w":78,"z":89}
dict2={key:value for d in (A,B) for key,value in d.items()}
print(dict2)