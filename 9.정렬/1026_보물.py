from sys import stdin

count = int(input())

list_a = list(map(int, stdin.readline().strip().split()))
list_b = list(map(int, stdin.readline().strip().split()))

total = 0
for _ in range(count):
    total += list_a.pop(list_a.index(min(list_a))) * list_b.pop(list_b.index(max(list_b)))

print(total)