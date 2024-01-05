s = input()

results = []
i = 0
while i < len(s):
    if s[i] not in ["A", "C", "G", "T"]:
        i += 1
        continue
    j = i + 1
    while j < len(s) and s[j] in ["A", "C", "G", "T"]:
        j += 1
    results.append(j-i)
    i = j + 1

if len(results) == 0:
    print(0)
else:
    print(max(results))

