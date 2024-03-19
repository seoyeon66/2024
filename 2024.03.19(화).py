s = int(input('분을 입력하세요:'))
print(s, '분은', s//10080 , '주' , s%10080//1440 , '일', s%1440//60  , '시간', s%60 ,  '분입니다.')

d = int(input('출발시간 [시]'))
dm = int(input('출발시간 [분]'))
a = int(input('도착시간 [시]'))
am = int(input('도착시간 [분]'))
travel_hours = ((a*60+am)-(d*60+dm))//60
travel_minutes = ((a*60+am)-(d*60+dm))%60
print('총 여행시간은', (travel_hours), '시간', (travel_minutes), '분입니다.')
