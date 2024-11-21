import math
print(2)
asal_sayilar = []
for i in range(3,1000000000,2):
    for sayi in asal_sayilar:
        if sayi > math.sqrt(i):
            print(i)
            asal_sayilar.append(i)
            break
        if i % sayi == 0:
            break
    else:
        print(i)
        asal_sayilar.append(i)
#not : bu karekokden buyuk olamama fikrini kendim bulmadim ama acayip hizli
#not 2 : 91 karekoke uymuyo ama yazmiyo bana farketmez
#egri egri dogru dogru 
#egri bugru ama yine de dogru
