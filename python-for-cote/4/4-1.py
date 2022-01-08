# 상하좌우
#https://fierycoding.tistory.com/59
N = 5
way = ['R', 'R', 'R', 'U', 'D', 'D']
way_json = {
    'R' : (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}
arr = []
for i in range(N):
    for j in range(N):
        arr.append((i, j))
print("arr: ", arr)