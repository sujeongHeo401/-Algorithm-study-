n, k = map(int, input().split())
result = 0

#n이 k 이상이라면 k 로 계속 나누기
while True:
    # (N == K로 나누어 떨어지는 수가 될 때 까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    if result == 4:
        print("target :", target)
        print("222 n :", n)

    print("1 result : ", result)
    n = target
    # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    #k로 나누기 
    result += 1
    print("result : ", result)
    n //= k

#마지막으로 남은 수에 대하여 1씩 빼기
print("(n - 1): ",(n - 1))
result += (n - 1)
print(result)