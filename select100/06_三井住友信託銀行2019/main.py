N = int(input())
S = input()

# 000から999までの全てのパスワードを生成
possible_passwords = [f"{i:03}" for i in range(1000)]

# Sの中で見つかったパスワードを格納するセット
found_passwords = set()

# 全ての可能なパスワードについて、それがSに含まれているかチェック
for password in possible_passwords:
    # パスワードの各桁がSに順に現れるかチェック
    index = -1
    is_found = True
    for digit in password:
        index = S.find(digit, index+1)  # 現在の桁の位置の次から探す
        if index == -1:  # パスワードのこの桁がSに見つからない場合
            is_found = False
            break
    if is_found:
        found_passwords.add(password)

# 見つかったユニークなパスワードの数を出力
print(len(found_passwords))
