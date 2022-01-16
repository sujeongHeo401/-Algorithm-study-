# 2
# 4
# 40 30 30 50
# 15
# 1 21 3 4 5 35 5 4 3 5 98 21 14 17 32
import sys
si = sys.stdin.readline

def go(i, j):
    print("i : ", i , "j : ", j)
    if i == j:
        return 0
    if d[i][j] != -1:
        return d[i][j]
    ans = d[i][j]
    cost = sum(a[i:j+1])
    print("cost : ", cost)
    for k in range(i, j):
        temp = go(i, k) + go(k+1, j) + cost 
        if ans == -1 or ans > temp:
            ans = temp 
    d[i][j] = ans
    return ans 




t = int(input())
for _ in range(t):
    n = int(input())
    a = list (map(int, si().split()))
    d = [[-1] * n for _ in range(n)]  ##### 어떻게 생겼어???
    # -1 (0, 0)
    # -1-1 (1, 0) (1, 1)
    # -1-1-1 (2, 0), (2, 1), (2, 2)
    print("gggg", go(0, n-1)) # n 이 4 이면 n 이 3으로 나오겠네 ㅋㅋㅋㅋㅋ 











# import sys
# si = sys.stdin.readline


# def go(i, j):
#     if i == j:
#         return 0
#     if d[i][j] != -1:
#         return d[i][j]
#     ans = d[i][j]
#     cost = sum(a[i:j+1])
#     for k in range(i, j):
#         temp = go(i, k) + go(k+1, j) + cost
#         if ans == -1 or ans > temp:
#             ans = temp
#     d[i][j] = ans
#     return ans 

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, si().split()))
#     d = [[-1] * n  for _ in range(n)]
#     print(go(0, n-1))

    