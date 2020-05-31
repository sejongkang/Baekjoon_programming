def Hanoi(n, f, b, t):
    global count
    global moves
    count += 1
    if n == 1:
        # 맨 위 원반이면 바로 from에서 to로 이동
        moves.append('{} {}'.format(f, t))
    else:
        # n번 위에 원반들 from에서 by로 옮겨놓기
        Hanoi(n-1, f, t, b)
        # n번 원반 from에서 to로 옮기기
        moves.append('{} {}'.format(f, t))
        # n번 위에 원반들 by에서 to로 옮기기
        Hanoi(n-1, b, f, t)

if __name__ == '__main__':
    num = int(input())
    count = 0
    moves = []
    Hanoi(num, 1, 2, 3)
    print(count)
    for move in moves:
        print(move)
