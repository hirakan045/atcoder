def main() -> None:
    S = input()

    L = len(S)

    ans = set()
    for i in range(L):
        for j in range(i, L+1):
            if S[i:j] != "":
                ans.add(S[i:j])

    print(len(ans))



if __name__ == "__main__":
    main()