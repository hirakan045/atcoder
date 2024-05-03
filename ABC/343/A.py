def main() -> None:
    A, B = map(int, input().split())

    L = [0,1,2,3,4,5,6,7,8,9]

    for l in L:
        if l != A + B:
            print(l)
            break


if __name__ == "__main__":
    main()