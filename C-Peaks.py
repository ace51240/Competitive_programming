N, M = map(int, input().split())
H = list(map(int, input().split()))
r_list = [set() for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    r_list[A-1].add(B)
    r_list[B-1].add(A)
# print(r_list)
count = 0
for i in range(N):
    flag = True
    for j in range(len(r_list[i])):
        next_index = r_list[i].pop()
        # print('now {} next {}'.format(i+1, next_index))
        if H[i] <= H[next_index-1]:
            flag = False
    if flag:
        count += 1
print(count)