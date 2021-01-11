# 8 x 8 체스판에서 현 나이트의 위치를 입력받고
# 움직일 수 있는 수를 출력
# 시뮬레이션
"""
a1

>> 2

c2

>> 6
"""
position = input()
x = ord(position[0]) - ord('a') + 1
y = int(position[1])

step_types = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2),
              (1, 2)]
cnt = 0

for step in step_types:
    dy = y + step[0]
    dx = x + step[1]
    if 1 <= dy and dy <= 8 and 1 <= dx and dx <= 8:
        cnt += 1

print(cnt)