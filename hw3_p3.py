'''setting'''
R0 = [' ',' ',' ',' ',' ',' ',' ']
R1 = [' ',' ',' ',' ',' ',' ',' ']
R2 = [' ',' ',' ',' ',' ',' ',' ']
R3 = [' ',' ',' ',' ',' ',' ',' ']
R4 = [' ',' ',' ',' ',' ',' ',' ']
R5 = [' ',' ',' ',' ',' ',' ',' ']
R = [R0,R1,R2,R3,R4,R5]

sep = '+---+---+---+---+---+---+---+'
row = '| %s | %s | %s | %s | %s | %s | %s |'


'''print game board'''
for i in range(0,6):
     print(sep+'\n'+row % tuple(R[i]))
print(sep)
print('  0   1   2   3   4   5   6  ')


'''start game'''
XO = ['O','X']           
valid = ['0','1','2','3','4','5','6','7','8','9']
play = 1  #局數(單數回合X,雙數回合O)
while play :
     print()
     print('Player',XO[play%2],'>> ',end = '')
     inp = input()
     #若未輸入則跳出訊息並重新開始這個迴圈
     if inp == '':
          print()
          print('Invalid input, try again [0-6].')
          continue
     #若非整數(浮點數也不行!)則跳出訊息並重新開始這個迴圈
     for j in range(0,len(inp)):
          if not inp[j] in valid:
               print()
               print('Invalid input, try again [0-6].')
               judgeValid = 0
               break
          else:
               judgeValid = 1
     if judgeValid == 0:
          continue
     #是數字但超出範圍則跳出訊息並重新開始這個迴圈
     elif eval(inp) < 0 or eval(inp) > 6:
          print()
          print('Out of range, try again [0-6].')
          continue
     #輸入正確，將X或O填入
     else:
          column = eval(inp)
          for k in range(5,-1,-1):
               if R[k][column] == ' ':
                    R[k][column] = XO[play%2]
                    judgeFilled = 1
                    break
               else:
                    judgeFilled = 0
          #若沒有可填入的空格則跳出訊息並重新開始這個迴圈
          if judgeFilled == 0:
               print()
               print('This column is full. Try another column.')
               continue
     
     '''print game board'''
     print()
     for i in range(0,6):
          print(sep+'\n'+row % tuple(R[i]))
     print(sep)
     print('  0   1   2   3   4   5   6  ')

     '''判斷是否有連線，若有則將線上的符號轉為小寫(該回合填入位置除外)'''
     #R[k][column]     =    XO[play%2]
     #^當回合填入的位置     ^當回合是X/O
     judgeWin = 0
     
     #垂直線
     #判斷填入位置下面是否已有三個相同符號
     v = k + 1
     vCount = 0
     while k <= 2 and v <= 5:
          if R[v][column] == XO[play%2]:
               vCount += 1
          else:
               break
          v += 1
     if vCount == 3:
          judgeWin = 1
          for v in range(1,4):
               R[k+v][column] = R[k+v][column].lower()

     #水平線
     #判斷同列左及右同符號連續相加是否>=3(加上填入的位置就會>=4)
     l = column - 1
     lCount = 0
     while l >= 0:
          if R[k][l] == XO[play%2]:
               R[k][l] = R[k][l].lower()
               lCount += 1
          else:
               break
          l -= 1
     r = column + 1
     rCount = 0
     while r <= 6:
          if R[k][r] == XO[play%2]:
               R[k][r] = R[k][r].lower()
               rCount += 1
          else:
               break
          r += 1
     if lCount + rCount >= 3:
          judgeWin = 1
     else:
          for t in range(0,7):
               R[k][t] = R[k][t].upper()

     #斜率1斜線
     #左下連續+右上連續>=3
     l = 1
     lCount = 0
     while k+l < 6 and column-l >=0:
          if R[k+l][column-l] == XO[play%2]:
               lCount += 1
          else:
               break
          l += 1
          
     r = 1
     rCount = 0
     while k-r >= 0 and column+r < 7:
          if R[k-r][column+r] == XO[play%2]:
               rCount += 1
          else:
               break
          r += 1

     if lCount + rCount >= 3:
          judgeWin = 1
          l = 1
          while k+l < 6 and column-l >=0:
               if R[k+l][column-l] == XO[play%2]:
                    R[k+l][column-l] = R[k+l][column-l].lower()
               else:
                    break
               l += 1
          
          r = 1
          while k-r >= 0 and column+r < 7:
               if R[k-r][column+r] == XO[play%2]:
                    R[k-r][column+r] = R[k-r][column+r].lower()
               else:
                    break
               r += 1

     #斜率-1斜線
     #左上連續+右下連續>=3
     l = 1
     lCount = 0
     while k-l >= 0 and column-l >=0:
          if R[k-l][column-l] == XO[play%2]:
               lCount += 1
          else:
               break
          l += 1
          
     r = 1
     rCount = 0
     while k+r < 6 and column+r < 7:
          if R[k+r][column+r] == XO[play%2]:
               rCount += 1
          else:
               break
          r += 1

     if lCount + rCount >= 3:
          judgeWin = 1
          l = 1
          while k-l >= 0 and column-l >=0:
               if R[k-l][column-l] == XO[play%2]:
                    R[k-l][column-l] = R[k-l][column-l].lower()
               else:
                    break
               l += 1
          
          r = 1
          while k+r < 6 and column+r < 7:
               if R[k+r][column+r] == XO[play%2]:
                    R[k+r][column+r] = R[k+r][column+r].lower()
               else:
                    break
               r += 1          

     #全部判斷完，
     #若有連線則將該回合input的X或O也轉為小寫，並print出結果
     if judgeWin == 1:
          R[k][column] = R[k][column].lower()
          '''print game board'''
          print()
          for i in range(0,6):
               print(sep+'\n'+row % tuple(R[i]))
          print(sep)
          print('  0   1   2   3   4   5   6  ')

          print()
          print('Winner:',XO[play%2])
          break
     #若無且已填滿則平手
     elif judgeWin == 0 and play == 42:
          print()
          print('Draw')
          break
     play += 1

