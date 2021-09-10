def m(b):
    c = [0, 0, 0]
    c[0] = b[0]; c[1] = b[1]; c[2] = b[2]
    if c[0] > c[2]:
        c[0], c[2] = c[2], c[0]
    if c[0] > c[1]:
        c[0], c[1] = c[1], c[0]
    elif c[1] > c[2]:
        c[1], c[2] = c[2], c[1]
    
    print(c)
    
    return c[1] 

def check(b, M):
    for k in range(3):
        if b[k] == M:
            m_index[k] = True
            
a = [int(x) for x in input().split()]
b = [0, 0, 0]
m_index = [False, False, False]

check(a, m(a))

for i in range(3):
    for j in range(3):
        b[0] = a[0]
        b[1] = a[1]
        b[2] = a[2]
        if i != j:
            b[i] = b[i] - b[j]
            check(b, m(b))
                    
for i in range(3):
    if m_index[i]:
        print('YES')
    else:
        print('NO')
            
            