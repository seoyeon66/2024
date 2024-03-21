a = ['메이킷','우진','시은']
print(a[0])
print(a[1][0])

a.append(1)
print(a)
a.remove(1)
print(a)
a.insert(2, '1')
a.extend(a)
print(a)

print(a[1:3:2])
print(a[1: ])
print(a[-1:-2])
print(len(a))

#문제 019: 기차처럼 만드는 리스트 자료 저장
a = ['메이킷','우진','시은']
print(a[0:])
print(a[0])
print(a[1])
print(a[-1])

#문제 020: 리스트 순서를 정하는 인덱스 알아보기
a = ['메이킷','우진','제임스','시은']
print(a[0:2])
print(a[1:4])
print(a[2:])
print(a[0:])

#문제 021: 리스트 추가, 삭제하기
a = ['우진','시은']
a.append('메이킷')
print(a)
a.remove('메이킷')
print(a)

a = ['우진','시은']
a.append('메이킷')
print(a)
a.pop()
print(a)

#문제 022: 리스트 원하는 위치에 삽입하기
a = ['우진','시은','메이킷']
a.insert(1, '하워드')
print(a)

#문제 023: 리스트 합치기
a = ['우진', '시은']
b = ['메이킷', '소피아', '하워드']
a.extend(b)
print(a)
print(b)

#문제 024: 공백 리스트와 합치기
a = ['우진','시은']
b = ['메이킷','소피아','하워드']
c = []
c.extend(a)
print(c)
c.extend(b)
print(c)

#문제 025: 리스트의 개수인 길이 구하기
a = [3, 7, 4, 5, 6, 8]
print('리스트 a의 개수 즉 길이는' ,len(a))
print('리스트 a의 숫자들의 평균은' , sum(a)/6)

#문제 026: 리스트 잘라내기(슬라이싱)
a = [1,2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']
b = a[0:5]
print('b :', b)
c=a[5:10]
print('c :', c)
d = a[4:6]
print('d :', d)
e = a[:-1:2]
print('e :', e)
f = a[1: : 2]
print('f :', f)

#문제 027: 리스트 거꾸로 잘라내기
a = ['형우', '윤진', '시은', '우진']
b = a[-1:-5:-1]
print(b)

#문제 028: 리스트 안에 리스트
a = [['메이킷', 95], ['우진', 100], ['시은', 98]]
print(a[0][0] ,'학생의 시험 점수는', a[0][1])
print(a[1][0] ,'학생의 시험 점수는',a[1][1] )
print(a[2][0] ,'학생의 시험 점수는',a[2][1])

#문제 029: 리스트 안에 있는 문자로 하나의 문자열 만들기(join)
a = ['시은', '우진', '지훈', '지연']
b =  ' '. join(a)
print(b)

#문제 030: 문자열 분리해 리스트 만들기(split)
a = '시은 우진 지훈 지연'
b = a.split(' ')
print(b)

#문제 031: 여러 개의 값 입력받기
a, b, c = map(int, input().split())
print(min(a, b, c))
