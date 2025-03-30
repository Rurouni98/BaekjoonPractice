n = int(input())
filenames = [input() for _ in range(n)]

pattern = []

# zip으로 각 문자열의 같은 인덱스 문자들을 묶어서 비교
for chars in zip(*filenames):
    if all(char == chars[0] for char in chars):
        pattern.append(chars[0])  # 모두 같으면 그대로
    else:
        pattern.append('?')  # 하나라도 다르면 '?'

print(''.join(pattern))