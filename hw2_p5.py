###print table###
x = ('Rock','Paper','Scissors')
print('Player A\tPlayer B\tResult')
for i in range(0,3):
     for j in range(0,3):
          print('%-16s%-16s' % (x[i],x[j]),sep='',end='')
          if i==j:                                #這部分是利用i及j來判斷勝負
               print('Tie')
          elif (i>j and i-j!=2) or j-i==2:
               print('Player A')
          else:
               print('Player B')
print('-'*48)                                     #分隔線

###start game###
r='rock'                                          #為了簡化後面條件判斷的式子
p='paper'
s='scissors'
while 1:                                          #外層迴圈讓遊戲一直循環(直到bye結束)
     A = input('Player A? ')
     while not (A==r or A==p or A==s or A=='bye'):#內層迴圈重複直到input正確
          print('Invalid input. Please enter again.')
          A = input('Player A? ')
     if A=='bye':
               break
     B = input('Player B? ')
     while not (B==r or B==p or B==s or B=='bye'):
          print('Invalid input. Please enter again.')
          B = input('Player B? ')
     if B=='bye':
          break
     print(A,B)
#判斷結果#
     if A==B:                                          #出一樣平手
          print('Outcome: Tie\n')
     elif (A,B)==(r,s) or (A,B)==(p,r) or (A,B)==(s,p):#直接打出所有A勝的情形去判斷
          print('Outcome: Player A wins!\n')
     else:                                             #非上述兩種情形則B勝
          print('Outcome: Player B wins!\n')

