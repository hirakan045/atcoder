def main() -> None:
    N = int(input())

    ans = []
    for i in range(N):
        row = input().split()
        l = []
        for j in range(N):
            if row[j] == "1":
                l.append(str(j + 1))
        ans.append(l)

    for a in ans:
        if " ".join(a) != "":
            print(" ".join(a))



if __name__ == "__main__":
    main()