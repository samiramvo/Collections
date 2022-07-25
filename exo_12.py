
from collections import deque
def compter(dq,n):
    return dq.count(n)

dq1=deque([1,4,9,4,3,2,4])
print(compter(dq1,2))
print(compter(dq1,4))