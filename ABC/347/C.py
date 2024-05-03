def main() -> None:
    N, A, B = map(int, input().split())
    D = list(map(int, input().split()))

    L = A + B
    lower = L
    upper = 0
    defa = 0
    defb = 0

    for d in D:
        k = d % L
        lower = min(lower, k)
        upper = max(upper, k)
        if k < L // 2:
            defa = max(defa, k)
        else:
            defb = max(defb, L-k)

    if (upper - lower < A) or (defa + defb + 1 <= A):
        print('Yes')
    else:
        print('No')

if __name__ == "__main__":
    main()