total_n = int(input())

total = []

for _ in range(total_n):
    total.append(int(input()))

for _ in range(total_n):
    dp = []

    for i in range(total[_]):
        dp.append(False)
    for i in range(1, total[_]+1):
        for j in range(1, (total[_]//i)+1):
            dp[i*j-1] = not dp[i*j-1]
    print(dp.count(True))