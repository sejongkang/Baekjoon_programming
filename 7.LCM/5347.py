from sys import stdin

total_n = int(input())

total = []

for _ in range(total_n):
    total.append(list(map(int, stdin.readline().strip().split())))

lcm_array  = []
for i in range(total_n):
    for j in range(1, total[i][1] + 1):
        tmp = total[i][0] * j
        if tmp % total[i][1] == 0:
            lcm_array.append(tmp)
            break
for i in range(total_n):
    print(lcm_array[i])
