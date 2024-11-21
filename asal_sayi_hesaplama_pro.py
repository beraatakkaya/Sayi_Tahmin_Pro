print(2)
asal_sayilar = []
for i in range(3,1000000000000,2):
    for sayi in asal_sayilar:
        if i % sayi == 0:
            break
    else:
        print(i)
        asal_sayilar.append(i)
