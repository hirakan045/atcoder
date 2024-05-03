def main() -> None:
    N = int(input())
    A = map(int, input().split())
    Q = int(input())

    for i in range(Q):
        q, *xy = map(int, input().split())
        if q == 1:
            x, y = xy
        else:
            x = xy[0]



if __name__ == "__main__":
    main()