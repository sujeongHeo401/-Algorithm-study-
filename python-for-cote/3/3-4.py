def sol(N: int, K: int, ans: int) -> int:
    result = 0
    target = (N // K) * K
    result += N - target
    N = target
    if N < K:
        break
    result += N -1
    # if N % K != 0:
    #     ans += (N % K)
    #     N = N - (N % K)
    # while N > 1:
    #     N //= K
    #     ans += 1
    # print("ans:", ans)
    # return ans

# sol(25, 5, 0)
# sol(17, 4, ans=0)

# print(sol(25, 5, 0))
# print(sol(17, 4, ans=0))
print(sol(20, 3, ans=0))

