N, M = map(int, input().split()) # N은 DNA의 수, M은 문자열의 길이
dnas = [input() for _ in range(N)]
max_dna = []
sum = 0
for chars in zip(*dnas):
    char_cnt = {}
    for char in chars:
        if char in char_cnt:
            char_cnt[char] += 1
        else:
            char_cnt[char] = 1

    max_count = 0
    max_char = ''

    for char in sorted(char_cnt.keys()):
        if char_cnt[char] > max_count:
            max_count = char_cnt[char]
            max_char = char
    max_dna.append(max_char)
    sum += N - max_count
print(''.join(max_dna))
print(sum)
