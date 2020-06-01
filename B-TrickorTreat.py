import numpy as np
N, K = map(int, input().split())
member = np.ones(N, dtype=int)
for i in range(K):
    d = int(input())
    A = list(map(int, input().split()))
    for j in range(len(A)):
        member[A[j]-1] = 0
print(sum(member))
