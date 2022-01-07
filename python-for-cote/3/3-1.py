n = 1260
count = 0
# 큰 단위인 화폐부터 차례대로 확인
list = [500, 100, 50, 10]

for coin in list:
    print("coin : ", coin)
    print("n // coin: ", n // coin)
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 화폐 세기
    n %= coin # n = n % count 
    print("n : ", n)

print(count)