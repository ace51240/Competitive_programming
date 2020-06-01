import numpy as np

N = int(input())
a = np.array(list(map(int,input().split())))
A = 0
B = 0
for i in range(1,N+1):
    if i % 2 == 1: 
        A += np.max(a)
        a[np.argmax(a)] = 0
    else:
        B += np.max(a)
        a[np.argmax(a)] = 0
print(np.abs(A-B))
        