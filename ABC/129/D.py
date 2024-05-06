def main() -> None:
    H, W = map(int, input().split())

    area = [input() for _ in range(H)]

    X = [[0] * W for _ in range(H)]
    Y = [[0] * H for _ in range(W)]

    # 横方向のマスの数を求める
    for h in range(H):
        start = 0
        end = 0
        for w in range(W):
            # 最終マスの時
            if w == W-1:
                # 障害物の時
                if area[h][w] == '#':
                    X[h][start:end] = [end-start] * (end-start)
                # 障害物ではない時
                else:
                    end = w + 1
                    X[h][start:end] = [end-start] * (end-start)
            # 最終マスではない時
            else:
                # 障害物の時
                if area[h][w] == '#':
                    X[h][start:end] = [end-start] * (end-start)
                    start = w + 1
                # 障害物ではない時
                else:
                    end = w + 1

    # 縦方向のマスの数を求める
    for w in range(W):
        start = 0
        end = 0
        for h in range(H):
            # 最終マスの時
            if h == H-1:
                # 障害物の時
                if area[h][w] == '#':
                    Y[w][start:end] = [end-start] * (end-start)
                # 障害物ではない時
                else:
                    end = h + 1
                    Y[w][start:end] = [end-start] * (end-start)
            # 最終マスではない時
            else:
                # 障害物の時
                if area[h][w] == '#':
                    Y[w][start:end] = [end-start] * (end-start)
                    start = h + 1
                # 障害物ではない時
                else:
                    end = h + 1

    ans = 0
    for h in range(H):
        for w in range(W):
            ans = max(ans, X[h][w] + Y[w][h] - 1)

    print(ans)
if __name__ == "__main__":
    main()