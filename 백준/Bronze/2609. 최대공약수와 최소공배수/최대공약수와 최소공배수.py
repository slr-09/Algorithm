import sys
input = sys.stdin.readline

def gcd(a, b):
    if a % b == 0: return b
    else: return gcd(b, a % b)


a, b = map(int, input().split())
if a > b: gcd = gcd(a, b)
else: gcd = gcd(b, a)

print(gcd)
print(int(a * b / gcd))
