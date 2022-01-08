# 상하좌우
#https://fierycoding.tistory.com/59
N = 5
map_arr = []
way = ['R', 'R', 'R', 'U', 'D', 'D']
way_dict = {
    'R' : (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}

for i in range(N):
    for j in range(N):
        map_arr.append((i, j))

curr_way = map_arr[0] # 스타트 
for each_way in way:
    is_valid_x = way_dict[each_way][0] + curr_way[0]
    is_valid_y = way_dict[each_way][1] + curr_way[1]
    if is_valid_x < N and is_valid_x >= 0 and is_valid_y < N and is_valid_y >=0:
        curr_way = (is_valid_x, is_valid_y) 
curr_way = (curr_way[0] + 1, curr_way[1] + 1)
print("답: ", curr_way)
#답:  (3, 4)
