x = int(input("Masukkan integer: "))
if x < 0:
    x = 0
    print('Negatif berubah menjadi nol')
elif x == 0:
    print('Nol')
elif x == 1:
    print('Single')
else:
    print('More')