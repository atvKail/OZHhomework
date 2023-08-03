t = int(input("Количество взвешиваний >> "))
n = int(input("Количество монет >> "))
moneys = [i for i in range(1, n + 1)]
f = True
arr = []

for i in range(t):
    c = input("Итог взвешивания >> ")
    sp1 = list(map(int, input("Первый список >> ").split()))
    sp2 = list(map(int, input("Второй список >> ").split())) 
    arr.append([c, sp1, sp2])
    print((23 + 2 * max(len(arr[i][1]), len(arr[i][2]))) * "=")
    if arr[i][0] == "=":
        tmp = arr[i][1] + arr[i][2]
        moneys = list(set(moneys) - set(tmp))
for i in range(t):
    sl, sr = [], []
    for j in range(len(arr[i][1])):
        if arr[i][1][j] in moneys:
            sl.append(arr[i][1][j])
    for j in range(len(arr[i][2])):
        if arr[i][2][j] in moneys:
            sl.append(arr[i][2][j])
    if (len(sl) == 1 and len(sr) == 0) or (len(sl) == 1 and len(sr) == 0):
        print(*(sl + sr))
        f = False
        break
if f:
    print("Недостаточно данных")

# 3
# 5
# <
# 1 5
# 2 3
# =
# 2 
# 3
# =
# 2 5
# 3 4