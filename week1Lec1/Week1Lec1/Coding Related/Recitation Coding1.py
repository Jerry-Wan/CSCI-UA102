def reverseNumber(s):
    if s>=0:
        a = str(s)
        b = list(a)
       
        b.reverse()
        d=""
        for c in b:
            d +=c
        return int(d)
    else:
        s = s*-1
        a = str(s)
        b = list(a)
       
        b.reverse()
        d=""
        for c in b:
            d +=c
        e = int(d)
        e = e*-1
        return e
