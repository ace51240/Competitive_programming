N, K = map(int, input().split())
A = list(map(int,input().split()))
MOD = 1000000007
count = 0
for i in range(N-1):
    for j in range(i+1, N):
        if A[i] > A[j]:
            count += 1
first = (count * K) % 1000000007

count2 = 0
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            count2 += 1

#ans = ((count * K) + (count2 * K * (K-1) // 2)) % MOD
second = (count2 * (K*(K-1)//2)%MOD) % MOD

print(int((first+second)%MOD))
#print(ans)

