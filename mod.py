import string


def modIfFull(productID):
    w = productID[0]
    r_s = productID[1]
    r = int(r_s)
    s_s = productID[2:4]
    s = int(s_s)
    as_w = ord(w)
    row = (as_w + r) % 7
    slot = s % 25
    wID = 4
    return wID, row, slot


x=["A","B","C","I","J","K","Q","R","S"]
for i in x:
    for j in range(1,6):
        for k in range(10):
            for l in range(10):
                f=str(i)+str(j)+str(k)+str(l)
                print(f)
                print(modIfFull(f))
