from sys import stdin

room = []
node = {}

def dfs(num, edge):
    for y in edge:
        if al_room[y - 1]:
            continue
        al_room[y - 1] = True
        if (room[y - 1] == 0) or (dfs(room[y - 1], node[room[y - 1]])):
            room[y - 1] = num
            return True
    return False

s_in = list(map(int, stdin.readline().strip().split()))

cow_n = s_in[0]
room_n = s_in[1]

for i in range(1, cow_n + 1):
    edge = []
    tmp = list(map(int, stdin.readline().strip().split()))
    for j in range(1, tmp[0] + 1):
        edge.append(tmp[j])
    node[i] = edge

for _ in range(room_n):
    room.append(0)

count = 0

for i in range(1, cow_n + 1):
    al_room = []
    for _ in range(room_n):
        al_room.append(False)
    if dfs(i, node[i]):
        count += 1

print(count)