def main() -> None:
    N = int(input())

    d = {
        0: "0",
        1: "2",
        2: "4",
        3: "6",
        4: "8"
    }

    L = []
    if N == 1:
        print(0)
    else:
        N -= 1
        while N > 0:
            L.append(N % 5)
            N //= 5

        ans = ""
        for l in L:
            ans = d[l] + ans

        print(ans)
if __name__ == "__main__":
    main()