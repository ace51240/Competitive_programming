A = int(input()) # 500
B = int(input()) # 100
C = int(input()) # 50
X = int(input())
count = 0
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if i * 500 + j * 100 + k * 50 == X:
                count += 1
print(count)
