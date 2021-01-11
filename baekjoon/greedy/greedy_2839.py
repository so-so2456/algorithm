# https://www.acmicpc.net/problem/2839
"""
설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.
"""

n = int(input())
cnt = 0
flag = False

while True:
    if n % 5 != 0:
        if n < 3:
            flag = True
            break
        n -= 3
        cnt += 1
    else:
        cnt += n // 5
        break

if flag:
    print(-1)
else:
    print(cnt)
