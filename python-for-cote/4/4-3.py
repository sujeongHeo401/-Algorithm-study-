# 현재 나이트의 위치 입력 받기
input_data = input()
col = int(ord(input_data[0])) - int(ord('a'))
row = int(input_data[1])
def is_valid(row: int, col: int) -> bool:
    if col < 0 or col > 7:
        # sth
        return False
    if row < 0 or row > 7:
        return False
    return True

# [row][col]
steps = [(-2, -1),(-2, 1), (2, 1), (2, -1), (-1, -2), (-1, 2), (1, 2), (1, -2)]

result = 0
# 8가지 방향에 대해서 이동 가능한지 확인
for i in steps:
    row, col = i[0] + row, i[0] + col
    if is_valid(row, col) is True:
        result += 1

print("답) ", result)
    