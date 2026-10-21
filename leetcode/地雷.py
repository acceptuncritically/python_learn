import sys
def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    rows = int(data[0])
    cols = int(data[1])
    two_list = []
    index = 2
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(data[index]))
            index += 1
        two_list.append(row)
    directions = [
        (-1, 0),  (1, 0),  (0, -1),  (0, 1),
        (-1, -1), (-1, 1), (1, -1),  (1, 1)
    ]
    result_list = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if two_list[i][j] == 1:
                result_list[i][j] = 9
            else:
                count = 0
                for dx, dy in directions:
                    next_x = i + dx
                    next_y = j + dy
                    if 0 <= next_x < rows and 0 <= next_y < cols:
                        if two_list[next_x][next_y] == 1:
                            count += 1
                result_list[i][j] = count
    for row in result_list:
        print(" ".join(map(str, row)))
if __name__ == '__main__':
    solve()