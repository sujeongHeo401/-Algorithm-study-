# 큰 수의 법칙 
def sol()-> int:
    N, M, K = 5, 8, 3 # 숫 횟수, 연속 횟수
    arr = [2, 4, 5, 4, 6]
    ans = 0

    arr.sort()
    print("arr[-1]:", arr[-1])
    print("arr[-2]:", arr[-2])
    max_val_list = [value for value in arr if value == arr[-1]]
    for i in max_val_list:
        arr.remove(i)
    second_max_val_list = [value for value in arr if value == arr[-1]]

    if 2 <= len(max_val_list):
        ans = max_val_list[-1] * K
        return ans

    if len(second_max_val_list) >= 1:
        if M - (K*(M//K)) > 0:
            # print("M // K: ", M // K)
            # print("M % K: ",M % K)
            # print("second_max_val_list[-1]: ",second_max_val_list[-1])
            # print("max_val_list[-1]*K: ",max_val_list[-1]*K)
            # print("second_max_val_list[-1]: ",max_val_list[-1]*K)
            ans = (M // K)*(max_val_list[-1]*K) + second_max_val_list[-1]*(M % K)
            return ans
    
print("ans : ", sol())
