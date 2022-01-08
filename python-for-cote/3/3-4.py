def sol(N: int, K: int, ans: int) -> int:
    if N % K != 0:
        ans += (N % K)
        N = N - (N % K)
    while N > 1:
        N //= K
        ans += 1

sol(25, 5, 0)
sol(17, 4, ans=0)

