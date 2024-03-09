# 文字列
A = input()

# 数値
B = int(input())

# 数値の分割代入
A, B, C = map(int, input().split())

# 数値をリストに代入
L = list(map(int, input().split()))

# 組み合わせをリストに代入
N = int(input())
L = [tuple(map(int, input().split())) for i in range(N)]

# 複数行の読み込み（整数
import sys
input = sys.stdin.readline
n = input()
for _ in range(n):
    x, y, z = map(int, input())

# 複数行の読み込み（文字列）
import sys
input = sys.stdin.readline
n = input()
for _ in range(n):
    s = input()[:-1]

# 反転
s = input()[::-1]

