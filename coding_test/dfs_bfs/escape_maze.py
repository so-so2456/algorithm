# N x M의 미로에서 벽은 0, 길은 1로 표시된다
# 현위치는 (1, 1)이고 출구는 (N, M)이다
# 미로를 탈출하기 위해 움직여야 하는 최소 칸의 개수를 출력
# >> BFS를 사용하는 것이 매우 효과적
# >> 시작 지점에서 가까운 노드부터 탐색하기 때문
"""
5 6
101010
111111
000001
111111
111111

>> 10
"""
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


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
    return graph[n - 1][m - 1]


print(bfs(0, 0))