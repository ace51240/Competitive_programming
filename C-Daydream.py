# import sys

# def finder(s):
#     l = len(s)
#     if l == 0:
#         print("YES")
#         return
#     elif l < 5:
#         print("NO")
#         return
#     elif s[l-5:l] == "dream":
#         finder(s[0:l-5])
#     elif s[l-5:l] == "erase":
#         finder(s[0:l-5])
#     elif s[l-6:l] == "eraser":
#         finder(s[0:l-6])
#     elif s[l-7:l] == "dreamer":
#         finder(s[0:l-7])
#     else:
#         print("NO")
#         return

def finder2(s):
    while True:
        # print(s)
        l = len(s)
        if l == 0:
            print("YES")
            return
        elif l < 5:
            print("NO")
            return
        elif s[l-5:l] == "dream":
            s = s[0:l-5]
        elif s[l-5:l] == "erase":
            s = s[0:l-5]
        elif s[l-6:l] == "eraser":
            s = s[0:l-6]
        elif s[l-7:l] == "dreamer":
            s = s[0:l-7]
        else:
            print("NO")
            return

if __name__ == "__main__":
    s = str(input())
    finder2(s)

