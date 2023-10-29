n = int(input())
a = set(map(int, input().split()))
a0 = min(list(a))
an = max(list(a))
ds = []
for d in range(1, an):
    t = set([a0 + d * i for i in range(an)])
    if a.issubset(t):
        ds.append((len(list(t)[:list(t).index(an) + 1]) - n, list(t)[:list(t).index(an) + 1]))
ans = min(ds, key=lambda x: x[0])
print(ans[0])
print(*ans[1])