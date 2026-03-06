#soal nomor 4(a)
panjang = 19
tinggi = 4
for i in range(tinggi):
    if i == 0 or i == tinggi - 1:
        print('*'*panjang)
    else:
        print('*'+' '*(panjang-2)+'*')
#soal nomor 4(b)
n = 4
for i in range(n + 1):
    print(' '*(n-i)+'*'*(2*i-1))
for i in range(n-1,0,-1):
    print (' '*(n-i) +'*'*(2*i-1))