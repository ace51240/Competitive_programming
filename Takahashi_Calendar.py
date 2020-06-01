# https://atcoder.jp/contests/jsc2019-qual/tasks/jsc2019_qual_a
M, D = map(int, input().split())
count = 0
for month in range(1, M+1):
    for date in range(1, D+1):
        d1 = date%10
        if d1 < 2: continue
        d10 = int(date/10)
        if d10 < 2: continue
        if d1 * d10 == month:
            count += 1
print(count)