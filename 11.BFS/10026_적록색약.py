from sys import stdin

def bfs(rows, columns, total):
    """

    :type rows: int
    :type columns: int
    :type total: list
    :type al_total: list
    """
    #   0 1 2 3 y열
    # 0 1 0 1 1
    # 1 1 1 1 1
    # x행
    # 탐색 순서 : 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    al_total = []
    que = []
    count = 0

    for _ in range(rows):
        al_total.append([0 for _ in range(rows)])
    for r in range(rows):
        row = r
        for c in range(columns):
            col = c
            if 0 <= row < rows and 0 <= col < columns and not al_total[row][col]:
                count += 1
                que.append([row, col])
                al_total[row][col] = 1
                while que:
                    tmp = que.pop(0)
                    a, b = tmp[0], tmp[1]
                    ch = total[a][b]
                    for i in range(4):
                        x = a + dx[i]
                        y = b + dy[i]
                        if 0 <= x < rows and 0 <= y < columns and not al_total[x][y] and ch == total[x][y]:
                            que.append([x, y])
                            al_total[x][y] = 1
    return count


if __name__ == '__main__':

    rows = int(stdin.readline().strip())

    total = []

    for i in range(rows):
        total.append([k for k in stdin.readline().strip()])

    print(bfs(rows, rows, total), end=' ')

    for r in range(rows):
        row = r
        for c in range(rows):
            col = c
            if total[r][c] == 'R':
                total[r][c] = 'G'

    print(bfs(rows, rows, total))



