def main() -> None:
    # N: スイッチの数、M: 電球の数
    N, M = map(int, input().split())
    # k: スイッチの番号、s: 電球の番号
    # p: スイッチが点灯する条件
    KS = []
    for _ in range(M):
        KS.append(list(map(int, input().split())))
    P = list(map(int, input().split()))

    ans = 0
    for i in range(2**N):
        flag = True
        for j in range(M):
            S = KS[j][1:]
            p = 0
            for s in S:
                if (i >> (s-1)) & 1:
                    p += 1
            if P[j] != p % 2:
                flag = False

        if flag:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()