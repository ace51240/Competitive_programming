A, B = map(int,input().split())
num = 1
count = 0
while num < B:
    num += (A - 1)
    count += 1
print(count)