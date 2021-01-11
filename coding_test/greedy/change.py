# 가장 큰 화폐 단위 부터
change = int(input("input your change: "))
coin = [500, 100, 50, 10]
count = 0

for i in coin:
    tmp = change // i
    change = change % i
    print(i, ">>", tmp)
    count += tmp

print("Total =", count)