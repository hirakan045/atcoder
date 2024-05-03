def main() -> None:
    N = int(input())

    l = [int("1"*i) for i in range(1, 13)]

    L = []

    for i in range(12):
        for j in range(12):
            for k in range(12):
                L.append(l[i] + l[j] + l[k])

    L = sorted(set(L))

    print(L[N-1])



if __name__ == "__main__":
    main()