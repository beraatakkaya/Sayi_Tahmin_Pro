import random

tahmin = ''
tahmin_sayisi = 0
while True:
    sifre = input("Sifrenizi giriniz: ")
    if len(sifre) != 4:
        print('Lutfen 4 haneli bir sifre giriniz')
        continue
    elif sifre[0] == '0':
        print('Sifre 0 ile baslayamaz')
        continue
    
    for sifre_karakteri in sifre:
        if sifre_karakteri not in '0,1,2,3,4,5,6,7,8,9':
            print("Sifreniz tamamen sayilardan olusmalidir")
            break
        karakter_tekrari = sifre.count(sifre_karakteri)
        if karakter_tekrari > 1:
            print('Bir sayi en fazla 1 kez kullanilmalidir')
            break
    else:
        break
sayi_listesi = [str(i) for i in range(1000,10000) if len(set(str(i))) == 4]
print(sayi_listesi)
while True:
    tahmin_sayisi += 1
    artilar = 0
    eksiler = 0
    tahmin = random.choice(sayi_listesi)
    if tahmin == sifre:
        print(f'Su kadar tahminde buldum: {tahmin_sayisi}')
        print(f'Sifreni buldum: {tahmin}')
        break
    for i in range(4):
        if tahmin[i] in sifre:
            if tahmin[i] == sifre[i]:
                print('+') 
                artilar += 1
            else:
                print('-')
                eksiler += 1
    fake_sayi_listesi = []
    for sayi in sayi_listesi:
        arti_sayisi = 0
        eksi_sayisi = 0
        for i in range(4):
            if tahmin[i] in sayi:
                if tahmin[i] in sayi[i]:
                    arti_sayisi += 1
                else:
                    eksi_sayisi += 1
        if arti_sayisi == artilar and eksi_sayisi == eksiler:
            fake_sayi_listesi.append(sayi)
    sayi_listesi = fake_sayi_listesi
    print(sayi_listesi)
    print(f'Sifren: {sifre}')
    print(f'Bilgisayar tahmini: {tahmin}')
    print(f'Arti sayisi: {artilar} eksi sayisi: {eksiler}')
    print(f'Bu kadar sayi kaldi: {len(sayi_listesi)}')
    devam_et = input('Devam etmek icin enter basinz: ')
    if devam_et != '':        
        break
