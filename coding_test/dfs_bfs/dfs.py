# DFS (Depth-First Search)
# 깊이 우선 탐색, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘

# 그래프(Graph)
# 노드(Node)와 간선(Edge)으로 표현되며 이때 노드를 정점(Vertex)이라고도 함
# 그래프 탐색이란 하나의 노드를 시작으로 다수의 노드를 방문하는 것을 말한다
# 두 노드가 간선으로 연결되어 있다면 '두 노드는 인접하다(adjacent)라고 한다'

# 그래프의 표현 방식
# 1. 인접 행렬(Adjacency Matrix) 방식 >> 파이썬은 리스트로 구현
# 2. 인접 리스트(Adjacency List) 방식

# 1. 인접 행렬 방식

INF = 99999999  # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [[0, 7, 5], [7, 0, INF], [5, INF, 0]]

print("Adjacent Matrix:", graph)

# 2. 인접 리스트 방식

# 행이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((1, 5))

print("Adjacent List:", graph)

# 메모리: 행렬 > 리스트
# 속도: 행렬 < 리스트
# DFS: 스택 자료구조
# 시간복잡도: O(N)

print()


# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8],
         [1, 7]]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

dfs(graph, 1, visited)