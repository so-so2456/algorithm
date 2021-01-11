n, k = map(int, input().split())

cnt = 0
while True:
    cnt += n % k
    n //= k
    cnt += 1
    if (n <= 1):
        break
print(cnt)