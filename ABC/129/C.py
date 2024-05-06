def main() -> None:
    N, M = map(int, input().split())
    A = [int(input()) for _ in range(M)]
    # DPの初期化
    dp = [0] * (N + 1)
    dp[0] = 1

    # Mによる条件分岐
    i = 0
    flag = M > 0

    if N == 0:
        ans = 0
    else:
        # 最初の床で条件分岐
        if flag and A[i] == 1:
            dp[1] = 0
            if i + 1 == M:
                flag = False
            else:
                i += 1
        else:
            dp[1] = 1
        # 2段目以降
        for j in range(2, N+1):
            if flag and j == A[i]:
                dp[j] = 0
                if i + 1 == M:
                    flag = False
                else:
                    i += 1
            else:
                dp[j] = dp[j-1] + dp[j-2]
        ans = dp[N] % 1000000007

    print(ans)

if __name__ == "__main__":
    main()