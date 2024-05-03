import sys

input = lambda: sys.stdin.readline().rstrip()

def main() -> None:
    H, W, N = map(int, input().split())
    T = input()
    S = tuple(input() for _ in range(H))

    d = {
        "L": (0, -1),
        "R": (0, 1),
        "U": (-1, 0),
        "D": (1, 0)
    }
    D = tuple(d[t] for t in T)

    def f(y, x):
        for di in D:
            dy, dx = di
            y += dy
            x += dx
            if S[y][x] == "#":
                return False
        return True

    ans = 0
    for i in range(H):
        for j in range(W):
            if S[i][j] == "." and f(i, j):
                ans += 1

    print(ans)



if __name__ == "__main__":
    main()