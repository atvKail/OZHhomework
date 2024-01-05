n = int(input())
s, x = (1 + n) * n // 2, int('1' * n)
print(s * x * (n - 1) if n > 1 else 0)
