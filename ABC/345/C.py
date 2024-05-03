def main() -> None:
    from collections import defaultdict
    import math

    S = input()

    d = defaultdict(int)

    for s in S:
        d[s] += 1

    ans = math.comb(len(S), 2)
    flag = True
    for k, v in d.items():
        comb = math.comb(v, 2)
        ans -= comb
        if flag and comb > 0:
            flag = False

    if flag:
        print(ans)
    else:
        print(ans + 1)



if __name__ == "__main__":
    main()