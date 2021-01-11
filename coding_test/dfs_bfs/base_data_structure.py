from collections import deque  # double-ended queue의 약자
from time import time


# 스택(stack)
def make_stack():  # 선입후출(first in last out)
    stack = []
    list_ = [5, 2, 3, 7, 1, 4]

    for i in list_:
        stack.append(i)
        print(stack)
        if i == 7 or i == 4:
            stack.pop()
    print(stack)
    print(stack[::-1])


# 큐(queue)
def make_queue():  # 선입선출(first in first out)
    queue = deque()
    list_ = [5, 2, 3, 7, 1, 4]

    for i in list_:
        queue.append(i)
        print(list(queue))
        if i == 7 or i == 4:
            queue.popleft()
    print(list(queue))
    queue.reverse()
    print(list(queue))


make_stack()
print()
make_queue()
print()

# 재귀함수의 수행은 스택 자료구조를 이용함
# 따라서 스택 자료구조를 사용하는 알고리즘은 대부분 재귀함수를 이용해서 구현된다
# >> 대표적인 예: DFS


# 재귀함수
def iterative_factorial(n):
    start_time = time()
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def recursive_factorial(n):
    if n <= 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)


start_time = time()
iterative_factorial(10)
end_time = time()
i = end_time - start_time

start_time = time()
recursive_factorial(10)
end_time = time()
j = end_time - start_time

print(i >= j)