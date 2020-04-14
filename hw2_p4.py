a=0                      #第0項
b=1                      #第1項
n=eval(input('Input an integer number: '))
if n == 0:
     r=a                 #用變數r來儲存result
elif n == 1:
     r=b
f=1                      #變數f計算目前r是第幾項
while f<n:               #While迴圈計算費氏數列
     r=a+b
     a=b
     b=r
     f+=1

if n%10==1 and n!=11:    #判斷回傳結果時要使用的序數單位(st/nd/rd/th)
     o='-st '
elif n%10==2 and n!=12:
     o='-nd '
elif n%10==3 and n!=13:
     o='-rd '
else:
     o='-th '

print('The ',n,o,'Fibonacci sequence number is: ',r,sep='',end='') #回傳結果


