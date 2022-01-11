# 큰 수의 법칙 
def sol()-> int:
    N, M, K = map(int, input().split())
    # N 개의 수를 공백으로 입력 받기 
    arr = list(map(int, input().split()))
    arr.sort()
    first = arr[N - 1] # 가장 큰 수 
    second = arr[N - 2] # 두 번째 가장 큰 수 
    # 가장 큰 수가 더해지는 횟수 계산
    count = K*(M//(K + 1))
    count += M%(K + 1) # 나눠 떨어지지 않는 경우

    result = 0
    result += (count) * first # 가장 큰 수 더하기
    result += (M - count) * second # 두 번째로 큰 수 더하기

    print(result) # 최종 답안 입력

sol()