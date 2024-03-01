def main() -> None:
    import sys

    input = sys.stdin.readline
    a, b, d = map(int, input().split())

    for i in range(a, b+1, d):
        print(i)


if __name__ == "__main__":
    main()