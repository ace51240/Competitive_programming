
import numpy as np

def frog():
    N = int(input())
    h = list(map(int, input().split()))
    dp = np.zeros(N, dtype=int)
    dp[1] = abs(h[1] - h[0])
    for i in range(2, N):
        dp[i] = min([abs(h[i] - h[i-1])+dp[i-1], abs(h[i] - h[i-2])+dp[i-2]])
    print(dp[N-1])

if __name__ == "__main__":
    frog()

