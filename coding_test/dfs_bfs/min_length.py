# 자작 문제
# N x M 미로, (0, 0)에서 출발
# 0 >> 벽
# 1 >> 길
# 출구는 (0, m - 1), (n - 1, 0), (n - 1, m - 1)
# 이 중 최단 거리를 출력
# (단, 한번 갈라진 길은 다시 이어지지 않음)
"""
9 11
11000001111
01100111000
00111100010
00001011110
11111110000
10000011100
11100010010
00100010010
11101111111

>> 15
  1   2   0   0   0   0   0  12  13  14  15 
  0   3   4   0   0   9  10  11   0   0   0 
  0   0   5   6   7   8   0   0   0  16   0 
  0   0   0   0   8   0  12  13  14  15   0 
 13  12  11  10   9  10  11   0   0   0   0 
 14   0   0   0   0   0  12  13  14   0   0 
 15  16  17   0   0   0  13   0   0  20   0 
  0   0  18   0   0   0  14   0   0  19   0 
 21  20  19   0  17  16  15  16  17  18  19 
"""
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = []
n, m = map(int, input().split())
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        elif graph[nx][ny] == 0:
            continue
        elif graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            dfs(nx, ny)
    return


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            elif graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return


dfs(0, 0)
graph[0][0] = 1

exits = [(0, m - 1), (n - 1, 0), (n - 1, m - 1)]

min = graph[0][m - 1]
for i, j in exits:
    if min > graph[i][j]:
        min = graph[i][j]
print(min)

for i in range(n):
    for j in range(m):
        print("%3d" % graph[i][j], end=' ')
    print()
