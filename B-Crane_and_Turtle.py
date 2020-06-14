
def count_legs():
    X, Y = map(int, input().split())
    for i in range(X):
        if i * 2 + (X-i) * 4 == Y or (X-i) * 2 + i * 4 == Y:
            print('Yes')
            return True
    print('No')

if __name__ == "__main__":
    count_legs()
