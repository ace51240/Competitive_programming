
def otoshidama():
    N, Y = map(int,input().split())
    for i in range(N+1):
        for j in range(N + 1 - i):
            k = N - i - j
            if 10000 * i + 5000 * j + 1000 * k == Y:
                print("{} {} {}".format(i, j, k))
                return 0
    print("-1 -1 -1")

if __name__ == "__main__":
    otoshidama()