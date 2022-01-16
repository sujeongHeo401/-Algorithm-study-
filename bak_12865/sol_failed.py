# N 개를 받고 무게는 K 만큼 ㅋㅋ
# A = 1 부터 ~ N 개까지 순열 
# A 의 무게 합이 K 이하여야 하고
import sys
from itertools import permutations
si = sys.stdin.readline
N, K = map(int, si().split())
input_arr = []
candi_arr = []
ans_arr = []
for i in range(N):
    input_arr.append(list(map(int,si().split())))

def perm(lst, n, K):
    ret = []
    if n > len(lst):
        return ret
    if n == 1:
        for i in lst:
            if i[0] <= K:
                ret.append([i])
    elif n > 1:
        for i in range(len(lst)):
            temp = [i for i in lst]
            temp.remove(lst[i])
            for p in perm(temp, n - 1, K):
                ret.append([lst[i]] + p)
    return ret

for i in range(1, N + 1):
    a = perm(input_arr, i, K)
    # for element in a:
    #     check_sum = 0
    #     for deep in element:
    #         check_sum += deep[0]
    #     if check_sum <= K:
    #         # print("element : " ,element)
    #         # print("여기 왔을 때 값이 뭔데 ?? K : ", K , "check_sum : ", check_sum)
    #         # print("a", a)
    candi_arr += a
            


max_answer = 0
for element in candi_arr:
    sum_1 = 0
    for each in element:
       sum_1 += each[0]
    print("K: ", K)
    if sum_1 >K:
        print("element: ", element)
        print("candi_arr", candi_arr)
        candi_arr.remove(element)
        print("111 candi_arr", candi_arr)



sum_1 = 0
max_kk = 0
for ele2 in candi_arr:
    sum_max = 0
    for ele3 in ele2:
        sum_max += ele3[1]
    max_kk = max(sum_max, max_kk)
    # print("ele2 : ", ele2)
    # print("ele2[1] : " , ele2[1])
    # sum_1 += ele2[1]
    # max_answer = max(sum_1, max_answer)

print("max_kk:", max_kk)
print("답: ", max_kk)