# 현재 나이트의 위치 입력 받기
input_data = input().split()
col = int(ord(input_data[0]) - ord('a'))
row = int(input_data[1])

def is_valid(x, y):
    if x < 0 or x > 7 or y < 0 or y > 7:
        return False
    return True

steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (1, 2), (1, -2), (-1, 2), (-1, -2)]




result = 0
for i in steps:
    row, col = row + i[0], row + i[1]
    if is_valid(row, col):
        result += 1

print("답 : ",result)