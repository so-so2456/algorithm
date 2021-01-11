# N x M 의 직사각형 맵에서 캐릭터가 움직이려한다
# 캐릭터의 움직임은 아래의 메뉴얼과 같다
# 1. 현재 위치, 현재 방향을 기준으로 왼쪽 방향(시계 반대 방향)부터 차례로 갈 곳을 정한다
# 2. 캐릭터가 바라본 방향으로 가보지 않은 칸이 존재하면 한 칸 전진한다
# 3. 모든 방향이 가본 칸이거나 바다로 되어 있는 경우 바라보는 방향을 유지한 채 뒤로 돌아간다
# 단, 뒤쪽 방향이 바다이면 움직임을 멈춘다

# 케릭터가 방문한 칸 수를 출력
#시뮬레이션
"""
 - 방향 d
 >> 0: 북
 >> 1: 동
 >> 2: 남
 >> 3: 서

 - 맵
 >> 0: 육지
 >> 1: 바다
 맵 외각은 항상 바다이다


4 4         # 4 x 4 맵
1 1 0       # (1, 1)에 북쪽(0)을 보고 있음
1 1 1 1     # 맵
1 0 0 1
1 1 0 1
1 1 1 1

>> 3


4 5
1 1 0
1 1 1 1 1
1 0 0 0 1
1 0 1 1 1
1 1 1 1 1

>> 4
"""
n, m = map(int, input().split())
x, y, direction = map(int, input().split())

coordinate = []
for i in range(n):
    coordinate.append(list(map(int, input().split())))
print()

# 북, 동, 남, 서 방향 정의
steps = [(0, -1), (1, 0), (0, 1), (-1, 0)]


# 왼쪽으로 회전
def turn_left():
    global direction
    if direction == 0:
        direction = 3
    else:
        direction -= 1


# 시뮬레이션 시작
cnt = 1
coordinate[y][x] = 2
while True:

    turn_left()
    dx = x + steps[direction][0]
    dy = y + steps[direction][1]

    # 가보지 않은 칸이 있으면 전진
    if coordinate[dy][dx] == 0:
        x = dx
        y = dy
        # 간 곳은 2로 표시
        coordinate[y][x] = 2
        cnt += 1

    # 전 방향이 막힌 경우 >> 교재에서는 turn_time이 4번이면 뒤로 이동함
    if (coordinate[y - 1][x] != 0 and coordinate[y + 1][x] != 0
            and coordinate[y][x - 1] != 0 and coordinate[y][x + 1] != 0):
        dx = x - steps[direction][0]
        dy = y - steps[direction][1]
        # 뒤가 바다인 경우 종료
        if (coordinate[dy][dx] == 1):
            break
        else:
            x = dx
            y = dy

for i in range(n):
    for j in range(m):
        print(coordinate[i][j], end=' ')
    print()
print(cnt)