alphavit = ' abcdefghijklmnopqrstuvwxyz'
n = int(input())
s = input().strip()
result = ''
for c in s:
    result += alphavit[(alphavit.index(c) + n) % len(alphavit)]
print('Result: "' + result + '"')
