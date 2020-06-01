N = int(input())
H = list(map(int,input().split()))

max_num = 0
posi = 0
while posi < N-1:
    count = 0
    for i in range(posi, N-1):
        if H[i] >= H[i+1]:
            count += 1
        else:
            break
    posi += count+1
    if max_num < count:
        max_num = count
print(max_num)
