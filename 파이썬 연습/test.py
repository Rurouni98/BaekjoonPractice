board = input()
pattern1 = 'AAAA'
pattern2 = 'BB'
cnt = 0
new_board = []
for char in board:
    if char == 'X':
        cnt += 1
    elif char == '.':
        if cnt > 0:
            a = cnt // 4
            cnt %= 4
            b = cnt // 2
            if cnt % 2 != 0:
                new_board = ['-1']
                break
            new_board.append(pattern1 * a + pattern2 * b)
            cnt = 0
        new_board.append('.')

if cnt > 0:
    a = cnt // 4
    cnt %= 4
    b = cnt // 2
    if cnt % 2 != 0:
        new_board = ['-1']
    else:
        new_board.append(pattern1 * a + pattern2 * b)

print(''.join(new_board))
