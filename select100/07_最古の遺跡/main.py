def main() -> None:
    import sys
    import itertools

    input = sys.stdin.readline

    n = int(input())
    coords = set()
    for _ in range(n):
        x, y = map(int, input().split())
        coords.add((x, y))

    ans = 0
    # 2組選んでループさせる
    for c1, c2 in itertools.combinations(coords, 2):
        x1, y1 = c1
        x2, y2 = c2

        # 2点間のベクトル
        x2_0, y2_0 = x2 - x1, y2 - y1
        x3_1, y3_1 = y2_0 + x1, -x2_0 + y1
        x4_1, y4_1 = y2_0 + x2, -x2_0 + y2

        x3_2, y3_2 = -y2_0 + x1, x2_0 + y1
        x4_2, y4_2 = -y2_0 + x2, x2_0 + y2

        if (x3_1, y3_1) in coords and (x4_1, y4_1) in coords:
            ans = max(ans, x2_0 * x2_0 + y2_0 * y2_0)

        if (x3_2, y3_2) in coords and (x4_2, y4_2) in coords:
            ans = max(ans, x2_0 * x2_0 + y2_0 * y2_0)
    print(ans)


if __name__ == "__main__":
    main()
