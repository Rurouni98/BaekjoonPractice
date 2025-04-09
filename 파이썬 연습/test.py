people = int(input())
tips = [int(input()) for _ in range(people)]
tips.sort(reverse=True)
maxSum = 0
diff = 0
for tip in tips:
    maxSum += (tip - diff) if tip - diff >= 0 else 0
    diff += 1
print(maxSum)
