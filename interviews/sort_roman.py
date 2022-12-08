
def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
 
    return -1
 
def romanToDecimal(st):
    res = 0
    i = 0
    while i < len(st):
        s1 = value(st[i])
        if (i + 1 < len(st)):
            s2 = value(st[i + 1])
            if (s1 >= s2):
                res = res + s1
            else :
                res = res + s2 - s1
                i += 1
        else :
            res = res + s1
        i += 1
     
    return res
 
def sortRoman(names):

    n = len(names)
 
    vp = []
 
    for i in range(n):
        p = romanToDecimal(names[i].split()[1])
        vp.append((p, names[i]))
    
    indexes = sorted(vp, key=lambda x: (x[1].split()[0], x[0]))
    return [index[1] for index in indexes]

print(sortRoman(['Phi II', 'Phil II']))
