vowels=['а' ,'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я', 'ы']
def vinni(list):
    slogi=[]
    for word in list:
        count=0
        for letter in word:
            if len(set(letter).intersection(set(vowels)))==1:
                count+=1
        slogi.append(count)
    return 'Парам пам-пам!' if len(set(slogi))==1 else 'Пам парам'

print('Винни, напиши свой стих :')
stih=list(input().split())
print(vinni(stih))