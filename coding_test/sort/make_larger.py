# (1 <= N <= 100,000 & 0 <= K <= N)
# 모든 원소는 10,000,000보다 작은 자연수다

n, k = map(int, input().split(' '))

array_a = list(map(int, input().split(' ')))
array_b = list(map(int, input().split(' ')))

array_a = sorted(array_a)
array_b = sorted(array_b, reverse=True)

for i in range(k):
    if array_a[i] >= array_b[i]:
        break
    else:
        array_a[i], array_b[i] = array_b[i], array_a[i]

result = sum(array_a)
print(result)
