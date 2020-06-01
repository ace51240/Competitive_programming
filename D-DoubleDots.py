import numpy as np
N, M = map(int, input().split())
A = np.empty(M)
B = np.empty(M)
for i in range(M):
    A[i], B[i] = map(int, input().split())
# 制限時間以内に解けてない