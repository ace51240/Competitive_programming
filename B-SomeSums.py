N, A, B = map(int,input().split())
sum1 = 0
for i in range(1,N+1):
    a = i // 10000
    b = i % 10000 // 1000
    c = i % 1000 // 100
    d = i % 100 // 10
    e = i % 10
    s = a + b + c + d + e
    if s >= A and s <= B:
        # print(i)
        sum1 += i
print(sum1)
# print("{} {} {} {} {}".format(a, b, c, d, e))


# 5400 / 1000 = 5
# 5400 % 1000 = 400
# 400 // 100 = 4 