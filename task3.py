n, m = input().split()
n, m = int(n), int(m)

layers = [int(x) for x in input().split()]
warriors = [int(x) for x in input().split()]

max_l = max(layers)
for i in range(n-1):#Вычисление всех солнечных участков
    if layers[i] == max_l:
        max_l = max(layers[i+1:])
    layers[i] -= max_l

layers.sort(reverse=True)
warriors.sort(reverse=True)
answer = 0
#print(layers)
#print(warriors)

l = 0
mw_i = 0
while (l < n) and (layers[l] > 0) and (mw_i < m):
    mw = warriors[mw_i]
        
    if mw <= layers[l]:
        answer += 1
        l += 1
    mw_i += 1
print(answer)