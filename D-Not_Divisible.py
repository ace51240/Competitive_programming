N = int(input())
A = list(map(int, input().split()))

eratus_list = [True] * (max(A) + 1)
A.sort()
last_a = 0
for A_num in A:
    # print(eratus_list)
    if last_a == A_num:
        continue
    for i in range(A_num+A_num, max(A)+1, A_num):
        eratus_list[i] = False
    last_a = A_num
cnt = 0

for i in range(len(A)):
    # 頭悪い書き方
    if i < len(A) - 1:
        if A[i] == A[i+1]:
            continue
    if i == len(A) - 1:
        if A[i] == A[i-1]:
            continue
    if eratus_list[A[i]]:
        cnt += 1
    last_a = A_num
print(cnt)


# for i in range(1, len(eratus_list)):
    # for 

# check_list = [0] * N
# flag = [0] * N
# def be_can_div(i):
#     if sum(check_list[0:i]) == 0:
#     for j in range(0, i):

#         if A[j] % A[i] == 0:
#             check_list[i] = 1
#         if A[i] % A[j] == 0:
#             return False

#     for j in range(i+1, N):
#         if A[j] % A[i] == 0:
#             check_list[i] = 1
#         if A[i] % A[j] == 0:
#             return False
#     return True

# count = 0
# for i in range(N):
#     print(check_list)
#     if check_list[i] == 1:
#         continue
#     if be_can_div(i):
#         count += 1
# print(count)

# 解けなかった

# 解説 :
# エラトステネスの篩を使う.調和級数を用いた解析によるとO(NlogN+A_maxlogA_max)になる
# 値の要素数のbool配列を用意しtrueに初期化．昇順に見ていく
# tureはその値より下に約数が存在しないことを意味する．
# 着目する値より大きい値で倍数となる要素をfalseにしていく
# 例) 24, 11, 8, 3, 16
# ソートすると，3, 8, 11, 16, 24
# bool配列は24要素, 値を合わせたいなら0を考慮して25要素
# [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# [T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T, T]
# 3の倍数の要素をFにする
# [T, T, T, T, T, F, T, T, F, T, T, F, T, T, F, T, T, F, T, T, F, T, T, F]
# 次に8の倍数の要素をFにする．
# [T, T, T, T, T, F, T, T, F, T, T, F, T, T, F, F, T, F, T, T, F, T, T, F]
# 次に11の倍数の要素をFにする．
# [T, T, T, T, T, F, T, T, F, T, T, F, T, T, F, F, T, F, T, T, F, F, T, F]
# 次に16の倍数の要素をFにする．(変更なし)
# [T, T, T, T, T, F, T, T, F, T, T, F, T, T, F, F, T, F, T, T, F, F, T, F]
# 次に24の倍数の要素をFにする．(変更なし)
# [T, T, T, T, T, F, T, T, F, T, T, F, T, T, F, F, T, F, T, T, F, F, T, F]
# Aのリストに含まれてる値のうち，Tとなっている数が解になる．
# 