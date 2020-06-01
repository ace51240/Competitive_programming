K = int(input())
S = str(input())
if len(S) <= K:
    print(S)
else:
    print('{}...'.format(S[0:K]))