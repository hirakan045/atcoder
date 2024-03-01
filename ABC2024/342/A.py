def main() -> None:
    S = input()

    N = len(S)

    ans = 0
    f = S[0]

    if S[0] == S[1]:
        for i in range(N):
            if S[0] != S[i]:
                ans = i + 1
    else:
        if S[0] != S[2]:
            ans = 1
        else:
            ans = 2

    print(ans)




if __name__ == "__main__":
    main()