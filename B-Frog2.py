
import numpy as np

def frog():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    dp = np.zeros(N, dtype=int)
    dp[1] = abs(h[1] - h[0])
    for i in range(2, N):
        min_value = 99999
        for k in range(1, min(1 + K, 1 + i)):
            if min_value > abs(h[i] - h[i-k])+dp[i-k]:
                min_value = abs(h[i] - h[i-k])+dp[i-k]
        dp[i] = min_value
    print(dp[N-1])
# まだWA
if __name__ == "__main__":
    frog()

