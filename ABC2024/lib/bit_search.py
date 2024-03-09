def bit_search(n):
    # 全探索
    for i in range(2 ** n):
        # 組み合わせを格納するためのリスト
        combination = []

        for j in range(n):
            # iのjビット目が1かどうかで、要素jが選択されているか判断
            if (i >> j) & 1:
                combination.append(j)

        # 選択された組み合わせの出力
        print(combination)


# 例：4要素からなる集合に対するビット全探索
bit_search(4)
