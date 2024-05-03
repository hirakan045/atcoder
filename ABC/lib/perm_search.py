from itertools import permutations

def search_permutations(n):
    # 0からn-1までの数の全順列を生成し、それぞれの順列を出力する
    for perm in permutations(range(n)):
        print(perm)

# 例: 0から2までの数の全順列を出力
search_permutations(3)

# (0, 1, 2)
# (0, 2, 1)
# (1, 0, 2)
# (1, 2, 0)
# (2, 0, 1)
# (2, 1, 0)
