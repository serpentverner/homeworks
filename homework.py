str1 = 'asdfghoyr'
str2 = 'asdfgkiure'
q = input('Вы ввели строку s1 и s2')
print(q)
print('Их длина соответственно',  len(str1), 'и', len(str2))
print('Первый символ первой строки', str1[:1],)
print('Последний символ второй строки', str2[-1])
print(bool(str1==str2))
print(str1 in str2)
print(str2 in str1)