year = int(input('Please input Year: '))
m = int(input('Please input Month: '))

'''判斷所需參數C/M/Y'''
(C,y) = divmod(year,100)      #C = year // 100, y = year % 100

if m==1:                      #蔡勒公式中1、2月要當作前一年的13、14月計算
     M=13
     Y=y-1
elif m==2:
     M=14
     Y=y-1
else:
     M=m
     Y=y
     
W=(Y+(Y//4)+(C//4)-2*C+(26*(M+1)//10))%7 #蔡勒公式

'''判斷月份天數'''
if ((y%4==0 and y%100!=0 ) or (y%400 ==0)) and m==2:   #閏年二月29天
     D = 29
elif m==2:                                             #平年二月28天
     D = 28
elif m==4 or m==6 or m==9 or m==11:                    #小月30天
     D = 30
else:                                                  #大月31天
     D = 31

'''依照規定格式輸出'''
print('Sun Mon Tue Wed Thu Fri Sat')
print('    '*W,end='')             #W是要跳過(空白)的天數
for i in range(1,D+1):
     print('%02d' % (i),end='  ')
     if (W+i)%7==0:                #前面空白天數加上印出的天數到七天要換行
          print('\n',end='')
