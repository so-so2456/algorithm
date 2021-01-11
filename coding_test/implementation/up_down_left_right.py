# N x N 공간에서 L, R, U, D를 입력받아 최종 위치를 출력
# 단, 정사각형을 벗어나는 움직임은 무시함
# 시뮬레이션
"""
5
R R R U D D

>> 3 4
"""
x, y = 1, 1
n = int(input())
move = list(input().split())
moving_types = ['L', 'R', 'U', 'D']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for step in move:
    for i in range(len(moving_types)):
        if step == moving_types[i]:
            tmp_x = x + dx[i]
            tmp_y = y + dy[i]
    if tmp_x < 1 and tmp_x > n and tmp_y < 1 and tmp_y > n:
        continue
    else:
        x = tmp_x
        y = tmp_y

print(x, y)