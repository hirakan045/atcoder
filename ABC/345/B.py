def main() -> None:
    X = int(input())

    if X % 10 == 0:
        X //= 10
    else:
        X = X // 10 + 1
    print(X)
if __name__ == "__main__":
    main()