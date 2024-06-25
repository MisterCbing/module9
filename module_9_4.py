def all_variants(s):
    for i in range(1, len(s)):
        for j in range(len(s) - i + 1):
            yield s[j : j + i]
    yield s

a = all_variants("abcd")
for i in a:
    print(i)