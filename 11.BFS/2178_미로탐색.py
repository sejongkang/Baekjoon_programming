from sys import stdin

def bfs(rows, columns, total, al_total):
    count = []
    count.append(1)
    que = [[0, 0]]
    al_total[0][0] = 1
    while que:
        tmp = que.pop(0)
        a, b = tmp[0], tmp[1]
        cc = count.pop(0)

        if a == (rows - 1) and b == (columns - 1):
            print(cc)
            break

        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < rows and 0 <= y < columns and not al_total[x][y] and bool(total[x][y]):
                que.append([x, y])
                al_total[x][y] = 1
                count.append(cc + 1)

if __name__ == '__main__':

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    s_in = list(map(int, stdin.readline().strip().split()))

    rows = s_in[0]
    columns = s_in[1]

    total = []
    al_total = []
    for i in range(rows):
        total.append([int(k) for k in stdin.readline().strip()])
        al_tmp = []
        for j in range(columns):
            al_tmp.append(0)
        al_total.append(al_tmp)

    bfs(rows, columns, total, al_total)




