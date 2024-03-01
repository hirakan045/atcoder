from collections import defaultdict

def main() -> None:
    ans = 0

    n = int(input())
    D = {n: 1}

    while D:
        d = defaultdict(int)  # d を defaultdict として初期化
        for x, k in D.items():
            ans += x * k
            x1 = x >> 1
            if x1 > 1:
                d[x1] += k
            x2 = (x + 1) >> 1
            if x2 > 1:
                d[x2] += k

        D = dict(d)  # D を d の現在の状態で更新

    print(ans)  # 結果を出力

if __name__ == "__main__":
    main()
