def main() -> None:

    S = input()
    s1, s2 = int(S[:2]), int(S[2:])

    yymm = False
    mmyy = False

    if s2 >= 1 and s2 <= 12:
        yymm = True
    if s1 >= 1 and s1 <= 12:
        mmyy = True

    if yymm and mmyy:
        print('AMBIGUOUS')
    elif yymm and not mmyy:
        print('YYMM')
    elif not yymm and mmyy:
        print('MMYY')
    else:
        print('NA')

if __name__ == "__main__":
    main()