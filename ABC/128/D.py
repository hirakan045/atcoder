def main() -> None:
    N, K = map(int, input().split())
    V = list(map(int, input().split()))

    ans = 0
    # i: 取り出す操作の数
    for i in range(K + 1):
        # l: 左から取り出す操作の数
        for l in range(i + 1):
            r = i - l
            # Nを超える組み合わせはスキップ
            if l + r > N:
                continue
            if r > 0:
                v = V[:l] + V[-r:]
            else:
                v = V[:l]
            v.sort()
            minus = list(filter(lambda x: x < 0, v))
            del_count = min(len(minus), K - i)

            value = sum(v) - sum(minus[:del_count])
            ans = max(ans, value)

    print(ans)

if __name__ == "__main__":
    main()
