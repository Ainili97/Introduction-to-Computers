'''p.s.一定要在所有地雷上正確放上旗子才算勝利'''
'''p.p.s.一局結束若輸入y以外則都當作n，結束遊戲'''
#### set up ####
import random
import time
parting = '   +---+---+---+---+---+---+---+---+---+'
column = ['a','b','c','d','e','f','g','h','i']
row = ['1','2','3','4','5','6','7','8','9']
instruction = 'Enter the column followed by the row (ex: a5). To add or remove a flag, \nadd \'f\' to the cell (ex: a5f).'

def show_table():
     '''印出當下遊戲'''
     print('     a   b   c   d   e   f   g   h   i')
     for i in range(9):
          print(parting)
          print('',i+1,end = ' ')
          for j in r[i]:
               print('|',j,end = ' ')
          print('|')
     print(parting)
     print()
     
def show_real():
     '''印出實際分布'''
     print('     a   b   c   d   e   f   g   h   i')
     for i in range(9):
          print(parting)
          print('',i+1,end = ' ')
          for j in R[i]:
               print('|',j,end = ' ')
          print('|')
     print(parting)
     print()
####### game #######
while 1:
     #設定R是實際地雷和數字的表; r是顯示出來的部分
     r1 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
     r2 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
     r3 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
     r4 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
     r5 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
     r6 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
     r7 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
     r8 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
     r9 = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
     r = [r1, r2, r3, r4, r5, r6, r7, r8, r9]
     R = r[:]
     for i in range(9):
          R[i] = r[i][:]
     for i in range(9):
          for j in range(9):
               R[i][j] = 0
     mine = 10 #剩下的地雷數
     countmine = 0 #已創造的地雷數
     show_table()
     print(instruction+'Type \'help\' to show this message again.')
     print()
     while 1:
          inp = input('Enter the cell (%s mines left): '%(mine))
          #input的第一種可能:help
          if inp == 'help':
               show_table()
               print(instruction)
               print()
          #input的第二種可能:正確的選擇一個位置(如:a5)
          elif len(inp) == 2 and inp[0] in column and inp[1] in row:
               a = int(inp[1])-1
               b = column.index(inp[0])
               #第一次踩下
               if countmine == 0 and r[a][b] == ' ':
                    #開始計時
                    timestart = time.time()
                    #隨機產生地雷(第一格的周圍八格不可以有地雷)
                    while countmine < 10:
                         (x,y) = (random.randint(0,8),random.randint(0,8))
                         wrongplace = 0
                         for i in range(-1,2):
                              if wrongplace == 1:
                                   break
                              for j in range(-1,2):
                                   if (x,y) == (a+i,b+j) or R[x][y] == 'X':
                                        wrongplace = 1
                                        break
                         if wrongplace == 0:
                              R[x][y] = 'X'
                              countmine +=1
                              for i in range(-1,2):
                                   for j in range(-1,2):
                                        if x+i >= 0 and x+i <= 8 and y+j >= 0 and y+j <= 8:
                                             if R[x+i][y+j] != 'X':
                                                  R[x+i][y+j] += 1
               #已經放旗子不能踩
               if r[a][b] == 'F':
                    show_table()
                    print('There is a flag there.')
                    print()
               #已經顯示出來
               elif r[a][b] != ' ':
                    show_table()
                    print('That cell is already shown.')
                    print()
               else:
                    ##踩到地雷則輸了，結束遊戲
                    if R[a][b] == 'X':
                         print('\nGame Over\n')
                         show_real()
                         break
                    #不是地雷
                    else:
                         #顯示該格，若為0，要一直複製到不為零的地方
                         if R[a][b] == 0:
                              zeros = [(a,b)] #把所有周圍為0的位置都存進list
                              #所有0周圍九宮格都顯示出來，且若為0的位置則再增加進list中再判斷
                              for (i,j) in zeros:
                                   for k in range(-1,2):
                                        for l in range(-1,2):
                                             if i+k >= 0 and i+k <= 8 and j+l >= 0 and j+l <= 8:
                                                  if r[i+k][j+l] != 'F':
                                                       r[i+k][j+l] = R[i+k][j+l]
                                                       if R[i+k][j+l] == 0 and not (i+k,j+l) in zeros:
                                                            zeros.append((i+k,j+l))     
                         #不為0則僅顯示該格
                         else:
                              r[a][b] = R[a][b]
                         show_table()
          #input的第三種可能:正確選擇一格放旗子(如:a5f)
          elif len(inp) == 3 and inp[0] in column and inp[1] in row and inp[2] == 'f':
               a = int(inp[1])-1
               b = column.index(inp[0])
               #已經顯示出數字則不能放
               if r[a][b] != 'F' and r[a][b] != ' ':
                    show_table()
                    print('Cannot put a flag there.')
                    print()
                    continue
               else:
                    #還沒有旗子則放
                    if r[a][b] == ' ':
                         r[a][b] = 'F'
                         mine -= 1
                    #已有旗子則移除
                    elif r[a][b] == 'F':
                         r[a][b] = ' '
                         mine += 1
                    ##判斷勝利
                    if mine == 0:
                         judgeWin = 1
                         for i in range(9):
                              for j in range(9):
                                   if r[i][j] == 'F':
                                        if R[i][j] != 'X':
                                             judgeWin = 0
                                             break
                         #勝利
                         if judgeWin == 1:
                              #結束計時
                              timeend = time.time()
                              time = int(timeend-timestart)
                              minute = time//60
                              second = time%60
                              print('\nYou Win. It took you %d minutes and %d seconds.\n' %(minute,second))
                              show_real()
                              break
                    show_table()
          #input的第四種可能:錯誤
          else:
               show_table()
               print('Invalid cell. Enter the column followed by the row (ex: a5). To add or \nremove a flag, add \'f\' to the cell (ex: a5f).')
               print()
     #結束一局，是否繼續玩
     play = input('Play again? (y/n): ')
     if play == 'y':
          continue
     else:
          break
