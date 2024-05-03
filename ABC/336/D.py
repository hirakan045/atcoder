def main() -> None:
    # 入力を受け取る
    N = int(input())
    A = [0] + list(map(int, input().split())) + [0]

    # m1, m2を初期化
    m1 = [0] * N
    m2 = [0] * N

    # m1を計算
    m1[0] = min(A[0], A[1] - 1)
    for i in range(1, N):
        m1[i] = min(m1[i - 1], A[i + 1] - i - 1)

    # m2を計算
    m2[N - 1] = A[N + 1] + N + 1
    for i in range(N - 2, -1, -1):
        m2[i] = min(m2[i + 1], A[i + 2] + i + 2)

    # 答えを求める
    ans = 0
    for i in range(N):
        ans = max(ans, min(m1[i] + i + 1, m2[i] - i - 1))

    # 答えを出力
    print(ans)


if __name__ == "__main__":
    main()
