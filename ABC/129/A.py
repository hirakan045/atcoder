def main() -> None:
    t = list(map(int, input().split()))
    t.sort()
    print(sum(t[:2]))

if __name__ == "__main__":
    main()