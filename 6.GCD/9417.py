from math import gcd
from sys import stdin

total_n = int(input())

total = []

for _ in range(total_n):
    total.append(list(map(int, stdin.readline().strip().split())))

gcd_array = []
for i in range(total_n):
    array = []
    for j in range(len(total[i])):
        for k in range(1, len(total[i]) - j):
            array.append(gcd(total[i][j], total[i][j + k]))
    gcd_array.append(array)

for i in range(total_n):
    print(max(gcd_array[i]))




