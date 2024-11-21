print(2)
asal_sayilar = []
for i in range(3,1000000000,2):
    for sayi in asal_sayilar:
        if sayi > i // 2 + 1:
            print(i)
            asal_sayilar.append(i)
            break
        if i % sayi == 0:
            break
    else:
        print(i)
        asal_sayilar.append(i)
#not : pro daha iyi bir surum bunda o hatayi farketmesem biraz sallayarak digerini 10 a katliyodu maalesef
#not 2: suan pro_mega_3.1 yazilacak o bundan daha iyi bir surum olur gibi
