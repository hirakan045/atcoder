def main() -> None:

    S = "wbwbwwbwbwbw" * 20
    N = len(S)

    W, B = map(int, input().split())
    L = []
    for i in range(N):
        for j in range(i, N):
            s = S[i:j]
            L.append((s.count("w"), s.count("b")))

    flag = False
    for l in L:
        if W == l[0] and B == l[1]:
            flag = True

    if flag:
        print("Yes")
    else:
        print("No")




if __name__ == "__main__":
    main()