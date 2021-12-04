numbers = open("input.txt").readline().strip()


tokens = [
    ("femti", 50),
    ("førti", 40),
    ("tretti", 30),
    ("tjue", 20),
    ("nitten", 19),
    ("atten", 18),
    ("sytten", 17),
    ("seksten", 16),
    ("femten", 15),
    ("fjorten", 14),
    ("tretten", 13),
    ("tolv", 12),
    ("elleve", 11),
    ("ti", 10),
    ("ni", 9),
    ("åtte", 8),
    ("sju", 7),
    ("seks", 6),
    ("fem", 5),
    ("fire", 4),
    ("tre", 3),
    ("to", 2),
    ("en", 1),
]


sum = 0
i = 0
while i < len(numbers):
    prev_i = i
    for token, value in tokens:
        token_len = len(token)
        candidate = numbers[i : i + token_len]
        if candidate == token:
            sum += value
            i += token_len
            break
    if prev_i == i:
        raise ValueError(
            f"Unable to parse token at position {i}. Preview: {numbers[i:i + 10]}"
        )

print(sum)
