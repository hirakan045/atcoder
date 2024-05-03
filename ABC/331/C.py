def main() -> None:
    from collections import defaultdict
    N = int(input())
    A = list(map(int, input().split()))

    d = defaultdict(list)
    for i, a in enumerate(A):
        d[a].append(i)

    ans = [0] * N
    s = 0
    for v, i_list in sorted(d.items())[::-1]:
        for i in i_list:
            ans[i] = s
        s += v * len(i_list)

    print(*ans)

if __name__ == "__main__":
    main()