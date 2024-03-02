def main() -> None:
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    l = [0] * 3*10**5

    count = 0
    ans = 0
    for a in A:
        l[a] += 1
        if count == l[a]:
            ans = min(ans, a)
        elif count < l[a]:
            ans = a
        count = l[ans]
        print(ans)

if __name__ == "__main__":
    main()