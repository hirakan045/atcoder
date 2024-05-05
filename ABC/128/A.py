def main() -> None:
    A, P = map(int, input().split())

    N = 3 * A + P

    ans = N // 2

    print(ans)

if __name__ == "__main__":
    main()