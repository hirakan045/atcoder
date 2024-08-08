def main() -> None:
    Y = int(input())
    if Y % 4 != 0:
        ans = 365
    elif Y % 100 != 0:
        ans = 366
    elif Y % 400 != 0:
        ans = 365
    else:
        ans = 366
    print(ans)

if __name__ == "__main__":
    main()