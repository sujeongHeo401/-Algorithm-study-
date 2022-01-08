N = 3
M = 3
# arr = [[3, 1, 2], [4, 1, 4], [2, 2, 2]]
arr = [[7, 3, 1, 8], [3, 3, 3, 4]]
ans_arr = []
for row in arr:
    ans_arr.append(min(row))
print("답", max(ans_arr))
