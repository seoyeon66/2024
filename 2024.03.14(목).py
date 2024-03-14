#7
a = '시은 우진'
a = a + ' 화이팅!!'
print(a)
print()
print(a)

#8
name = input('이름이 무엇인가요? ')
age = int(input('몇 살인가요? '))
print(name ,'님은 내년에는', age+1 ,'살이 됩니다.')

#9
a = int(input())
b = float(input())
print('a와 b의 합은', a+b)
print('a와 b의 평균값은', (a+b)/2)

#10
makit= 'SieunWoojin!'
result = makit[0]
print(result)
result = makit[5]
print(result)
result = makit[-1]
print(result)

#11
makit = 'Sieun Woojin!'
result = makit[2:9]
print(result)
result = makit[0:5]
print(result)
result = makit [6:13]
print(result)

#12
makit = '동서남북동서남북동서남북'
result = makit [0::4]
print(result)

#13
makit = '동서남북'
result = makit [::-1]
print(result)

#14
phone = '010-1234-5678'
new_phone = phone.replace('-' , '.')
print(new_phone)

#15
a = 10
b = 20
print(a < b)
print(a > b)
print(7 > 8)
print(7 < 8)
print(1 <= 1)
print(1 >= 2)
print(1 == 1)
print(1 == 2)
print(1 != 1)
print(1 != 2)

#16
a = 20
b = 30
print(a > 40 and b > 40)
print(a > 20 and b > 20)
print(a < 30 and b > 30)
print(a > 10 and b > 10)
print(20 > 40 or 30 > 40)
print(20 > 20 or 30 > 20)
print(20 < 30 or 30 > 30)
print(20 > 10 or 20 > 10)
print(a != b)
print(not(a != b))

#17
s = int(input('초를 입력하세요:'))
print(s, '초(sec)는', s//60  , '분(min)', s%60 ,  '초(sec)입니다.')

#18
s = int(input('분을 입력하세요:'))
print(s, '분은', s//1440 , '일', s%1440//60  , '시간', s%60 ,  '분입니다.')
