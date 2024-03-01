def main() -> None:
    S = input()
    T = input()

    d = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4
    }

    S = min(abs(d[S[0]] - d[S[1]]), abs(d[S[1]] - d[S[0]]))
    T = min(abs(d[T[0]] - d[T[1]]), abs(d[T[1]] - d[T[0]]))

    S = min(S, 5-S)
    T = min(T, 5-T)

    if S==T:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()