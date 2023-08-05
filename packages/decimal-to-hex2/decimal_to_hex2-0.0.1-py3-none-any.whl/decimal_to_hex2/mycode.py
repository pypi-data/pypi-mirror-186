def func(n):
    nbits = 16
    hexa = '{:04x}'.format(n & (( 1 << nbits)-1))
    print(hexa)