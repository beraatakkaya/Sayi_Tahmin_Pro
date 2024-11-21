print(2)
for i in range(3,1000000000,2):
    for a in range(3,i//2+1,2):
        if i % a == 0:
            break
    else:
        print(i)
