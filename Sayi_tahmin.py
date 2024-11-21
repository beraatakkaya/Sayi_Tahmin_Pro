def sayitahmin(isim,sifre,tahmin):
    for i in range(4):
        if tahmin[i]==sifre[i]:
            arti+=1
        elif tahmin[i] in sifre:
            eksi+=1
    kullaniciya_gosterilen_sey+=arti*'+'
    kullaniciya_gosterilen_sey+=eksi*'-'
    arti=0
    eksi=0
kullanici_1=input('Birinci kullanici adini giriniz: ')
kullanici_2=input('Ikinci kullanici adini giriniz: ')
kullaniciya_gosterilen_sey=''
b=1
arti=0
eksi=0
kullanici_1_sifesi=input(f'{kullanici_1} 4 haneli sifreni gir: ')
kullanici_2_sifesi=input(f'{kullanici_2} 4 haneli sifreni gir: ')
while kullaniciya_gosterilen_sey!='++++':
    print(kullaniciya_gosterilen_sey)
    kullaniciya_gosterilen_sey=''
    if b==1:
        tahmin=input(f'{kullanici_1} tahmini gir: ')
        sifre=kullanici_2_sifesi
        b=2
        isim=kullanici_1
        diger_sifre=kullanici_1_sifesi
    else:
        tahmin=input(f'{kullanici_2} tahmini gir: ')
        isim=kullanici_2
        sifre=kullanici_1_sifesi
        diger_sifre=kullanici_2_sifesi
        b=1
    sayitahmin(isim,sifre,tahmin)
print(f'{isim} Kazandi!',end='')
print(f'{isim} sifresi: {diger_sifre}')
