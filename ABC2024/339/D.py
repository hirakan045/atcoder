from collections import deque
import sys

def bfs_optimized(grid, start1, start2):
    n = len(grid)
    # 訪問済み状態を (x1, y1, x2, y2) の形で記録
    visited = set((start1[0], start1[1], start2[0], start2[1]))
    queue = deque([(start1, start2, 0)])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while queue:
        (x1, y1), (x2, y2), steps = queue.popleft()
        if (x1, y1) == (x2, y2):
            return steps

        for dx, dy in directions:
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy

            # 移動先がグリッド内かつ空きマスかを確認
            if not (0 <= nx1 < n and 0 <= ny1 < n and grid[nx1][ny1] != '#'):
                nx1, ny1 = x1, y1
            if not (0 <= nx2 < n and 0 <= ny2 < n and grid[nx2][ny2] != '#'):
                nx2, ny2 = x2, y2

            if (nx1, ny1, nx2, ny2) not in visited:
                visited.add((nx1, ny1, nx2, ny2))
                queue.append(((nx1, ny1), (nx2, ny2), steps + 1))

    return -1


# 入力とプレイヤーの位置を探す部分は以前と同じ
N = int(input())
grid = tuple(sys.stdin.readline().rstrip() for _ in range(N))


def find_players(grid):
    positions = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == 'P':
                positions.append((i, j))
    return positions


player1, player2 = find_players(grid)
min_steps = bfs_optimized(grid, player1, player2)
print(min_steps)
