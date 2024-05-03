def main() -> None:
    N, M  = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    BC = [tuple(map(int, input().split())) for _ in range(M)]
    BC = sorted(BC, key=lambda x: x[1], reverse=True)

    i = 0
    for bc in BC:
        b = bc[0]
        c = bc[1]
        for _ in range(b):
            if i >= N:
                break
            if A[i] < c:
                A[i] = c
                i += 1
            else:
                break

    print(sum(A))


if __name__ == "__main__":
    main()