def main() -> None:
    n = int(input())

    ans = 0
    l = [n]

    for v in l:
        ans += sum(l)
        l = []
        if v % 2 == 0:
            l.append(v // 2)
            l.append(v // 2)
        else:
            l.append(v // 2)
            l.append(v // 2 + 1)
        while 1 in l:
            l.remove(1)
    print(ans)


if __name__ == "__main__":
    main()