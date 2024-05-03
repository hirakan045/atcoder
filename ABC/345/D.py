def main() -> None:
    N, H, W = map(int, input().split())

    S = H * W

    tile = []
    area = []
    for _ in range(N):
        A, B = map(int, input().split())
        tile.append(tuple([A, B]))
        area.append(A*B)

    # 面積が等しい組み合わせを求める
    comb = []
    for i in range(2**N):
        s = 0
        l = []
        for j in range(N):
            if ((i >> j) & 1):
                s += area[j]
                l.append(j)
        if S == s:
            comb.append(tuple(l))

    for c in comb:
        print(c)



if __name__ == "__main__":
    main()