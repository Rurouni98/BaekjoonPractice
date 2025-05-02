def modinv(b, mod):
    return pow(b, mod - 2, mod)

def modfrac(numer, denom, mod):
    return (numer * modinv(denom, mod)) % mod

M = int(input()) # M은 주사위의 갯수
total = 0
for i in range(M):
    N, S = map(int, input().split()) # N은 몇 면체인지, S는 모든 면에 적힌 수를 더한 값
    total += modfrac(S, N, 1000000007)

print(total % 1000000007)
