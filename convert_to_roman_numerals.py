import sys

x = 'IVXLCDM '
with open(sys.argv[1], 'r') as f:
    for l in f:
        r = ''
        a = int(l)
        i = 0
        while a > 0:
            d = a % 10
            r = (x[i] + x[i+2] if d == 9 else x[i] + x[i+1] if d == 4 else x[i+1] * (d // 5) + x[i] * (d % 5)) + r
            a //= 10
            i += 2
        print(r)
