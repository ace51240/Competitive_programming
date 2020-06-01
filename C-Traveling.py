def travel():
    N = int(input())
    flag = True
    last_t = 0
    last_x = 0
    last_y = 0
    for i in range(N):
        t, x, y = map(int,input().split())
        updated_t = t - last_t
        updated_x = abs(x - last_x)
        updated_y = abs(y - last_y)
        if updated_x + updated_y > updated_t or (updated_t - updated_x - updated_y) % 2 != 0:
            flag = False
            # print('No')
        # else:
            # print('Yes')
        last_t = t
        last_x = x
        last_y = y
    if flag:
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    travel()