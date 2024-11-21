denklem = input('Denklemi giriniz: ')
denklemdeki_degerler = []
for deger in denklem:
    if deger != ' ':
        denklemdeki_degerler.append(deger)
print(denklemdeki_degerler)
'''
print(denklem)
for deger in denklem:
    try:
        deger = int(deger)
    except ValueError:
        print('oyle')
    finally:
        print(type(deger))
        print(denklem)
        if 'x' in deger:
            print('evet')
            '''
