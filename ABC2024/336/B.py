def main() -> None:
    N = int(input())

    ans = 0
    flag = True

    while flag:
        if N % 2 == 0 and N != 0:
            ans += 1
            N = N >> 1
        else:
            flag = False

    print(ans)
if __name__ == "__main__":
    main()