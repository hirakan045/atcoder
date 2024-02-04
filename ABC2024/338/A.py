S = input()

if len(S) == 1:
    result = "Yes" if S[0].isupper() else "No"
else:
    result = "Yes" if S[0].isupper() and S[1:].islower() else "No"

print(result)