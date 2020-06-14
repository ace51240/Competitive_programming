X, N = map(int, input().split())
p = list(map(int, input().split()))

def is_in_p(j):
    flag = True
    for p_i in p:
        if p_i == j:
            flag = False
    return flag

abs_min = 101 
min_num = 0

for j in range(102):
    if abs(X - j) < abs_min and is_in_p(j):
        abs_min = abs(X - j)
        min_num = j
print(min_num)