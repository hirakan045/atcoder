def main() -> None:
    import sys
    input = sys.stdin.readline

    A = []
    flag = True

    while flag:
        a = int(input())
        A.append(a)
        if a == 0:
            flag = False

    A = A[::-1]

    for a in A:
        print(a)



if __name__ == "__main__":
    main()