s = input()

if s == "".join(sorted(s)):
    print("Yes")
else:
    print("No")