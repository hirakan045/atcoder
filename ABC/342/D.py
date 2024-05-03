def main() -> None:
    import math
    from collections import defaultdict

    N = int(input())
    A = list(map(int, input().split()))

    X = 2*10**5
    s = [0] * (X + 1)  # X+1 の長さでリストを初期化。0から始まるインデックスに対応。

    # s[i]をiで初期化
    for i in range(1, X + 1):
        s[i] = i

    # d は sqrt(X) から 2 まで減少
    for d in range(int(math.sqrt(X)), 1, -1):
        # k のループ。ここでの除算は小数点以下を切り捨てるために // 演算子を使用
        for k in range(1, X // (d * d) + 1):
            if s[k * d * d] % (d * d) == 0:
                s[k * d * d] //= d * d  # s[k*d*d]をd*dで割る

    d = defaultdict(int)
    for a in A:
        d[s[a]] += 1

    ans = 0
    for k, v in d.items():
        if k == 0:
            ans += math.comb(len(A), 2) - math.comb(len(A)-v, 2)
        elif v > 1:
            ans += math.comb(v, 2)

    print(ans)

if __name__ == "__main__":
    main()