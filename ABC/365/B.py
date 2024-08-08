def main() -> None:
    N = int(input())
    A = list(map(int, input().split()))

    d = {i: value for i, value in enumerate(A)}
    d = dict(sorted(d.items(), key=lambda item: item[1]))
    print(list(d)[-2] + 1)

if __name__ == "__main__":
    main()