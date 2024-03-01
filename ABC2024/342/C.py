def main() -> None:
    from string import ascii_lowercase

    N = int(input())
    S = input()

    Q = int(input())

    mapping_from = ascii_lowercase
    mapping_to = ascii_lowercase

    for _ in range(Q):
        c, d = input().split()
        mapping_to = mapping_to.replace(c, d)  # c を d に置き換える

    # 文字を一括で置換する
    print(S.translate(str.maketrans(mapping_from, mapping_to)))

if __name__ == "__main__":
    main()