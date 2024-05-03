def main() -> None:
    N = int(input())
    P = [int(i) for i in input().split()]
    Q = int(input())

    d = {}
    for i in range(N):
        d[P[i]] = i
    for i in range(Q):
        A, B = map(int, input().split())
        if d[A] > d[B]:
            print(B)
        else:
            print(A)

if __name__ == "__main__":
    main()