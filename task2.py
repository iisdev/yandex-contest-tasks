n, m = input().split()
n, m = int(n), int(m)

img = [[symb for symb in input()] for i in range(n)]
BOTTLE = ('\\', '/', '|')
layer = n - 2

for i in range(int(input())):
    inp = input().split()
    
    
    for j in range(int(inp[1])):
        in_bottle = False
        
        for k in range(m):
            sym = img[layer][k]
            if not(in_bottle) and (sym in BOTTLE):
                in_bottle = True
                continue
                
            if in_bottle and (sym in BOTTLE):
                in_bottle = False
                continue
                
            if in_bottle:
                img[layer][k] = inp[2]
                
        layer -= 1


for i in range(n):
    for j in range(m):
        print(img[i][j], end = '')
    print()
