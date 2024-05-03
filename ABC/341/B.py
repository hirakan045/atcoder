def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    s = [list(map(int, input().split())) for i in range(n-1)]

    for i in range(n-1):
        if s[i][0] > a[i]:
            continue
        else:
            x = a[i] // s[i][0]
            a[i] = a[i] - s[i][0] * x
            a[i+1] = a[i+1] + s[i][1] * x

    print(a[n-1])

if __name__ == "__main__":
    main()