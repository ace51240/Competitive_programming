N = int(input())
A = list(map(int,input().split()))
count = 0
flag = True
while flag:
    for i in range(N):
        if A[i] % 2 == 1:
            print(count)
            flag = False
            break
        else:
            A[i] = A[i] // 2
    count += 1