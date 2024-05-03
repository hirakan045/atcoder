def main() -> None:
    S = input()
    flag = True
    for i in range(len(S)):
        if i == 0:
            if S[i] != '<':
                flag = False
        elif i == len(S) - 1:
            if S[i] != '>':
                flag = False
        else:
            if S[i] != '=':
                flag = False

    if flag:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()