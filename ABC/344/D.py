def main() -> None:
    # 入力の文字
    T = input()
    # 文字列が入った袋の数
    N = int(input())

    # 入力文字の長さ
    L = len(T)
    # 入力文字を何個の文字列で作れるかを格納するリスト
    dp = [10 ** 9] * (L+1)
    # 0文字目は0個の文字が必要
    dp[0] = 0
    # N個の袋の文字列を受け取る
    for _ in range(N):
        A, *S = input().split()
        # i文字目までが何個の袋で作れるかを更新する
        for i in range(L, -1, -1):
            # 袋に入っている文字列でdpを更新できるか確認する
            for s in S:
                # 袋に入っている文字列の長さ
                m = len(s)
                if i+m <= L and s == T[i:i+m]:
                    dp[i+m] = min(dp[i+m], dp[i] + 1)

    ans = dp[L] if dp[L] < 10**9 else -1
    print(ans)

if __name__ == "__main__":
    main()