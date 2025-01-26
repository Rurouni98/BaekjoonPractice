num = int(input())
dp = [0 for i in range(num + 1)]
dp[0] = 0
if num >= 1:
    dp[1] = 1
if num >= 2:
    dp[2] = 1
for i in range(3, num + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[num])