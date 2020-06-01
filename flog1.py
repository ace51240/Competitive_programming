import sys
sys.setrecursionlimit(10**6)
#import numpy as np
#N = map(int, input().split())
N = int(input())
h = list(map(int,input().split()))

# メモ化再帰
#memo = np.full(N, -1)
# memo = [-1]*N
# def func(i):
#     if memo[i] != -1:
#         return memo[i]
#     if i == 0:
#         return 0
#     elif i == 1:
#         return abs(h[1]-h[0])
#     a = func(i-1) + abs(h[i]-h[i-1])
#     b = func(i-2) + abs(h[i]-h[i-2])
#     memo[i] = min(a,b)
#     return min(a,b)
# print(func(N-1))

# pythonの問題はfuncの呼び出し回数
# 10^50に耐えられない
# sys.setrecursionlimit(10**6)で回避

# DP
#memo = np.full(N, -1)
memo = [-1]*N

memo[0] = 0
memo[1] = abs(h[1]-h[0])
for i in range(2,N):
    a = memo[i-1] + abs(h[i]-h[i-1])
    b = memo[i-2] + abs(h[i]-h[i-2])
    memo[i] = min(a,b)
print(memo[N-1])
# def func(i):
#     if memo[i] != -1:
#         return memo[i]
#     if i == 0:
#         return 0
#     elif i == 1:
#         return abs(h[1]-h[0])
#     a = func(i-1) + abs(h[i]-h[i-1])
#     b = func(i-2) + abs(h[i]-h[i-2])
#     memo[i] = min(a,b)
#     return min(a,b)
# print(func(N-1))
