S=input('Enter a string: ')
L=len(S)
s=''                               #用s儲存最長的回文

'''因為單數個字的回文 跟 雙數個字的回文之間特性不太相同，因此分開做判斷'''
'''這裡都是使用兩層迴圈，以i作為基準，j則是向i左右尋找回文的範圍，
   i由左至右移動,j則使範圍由內向外延伸'''

for i in range(1,L):               #判斷單數個字的回文
     for j in range(0,min(i+1,L-i)):
          if S[i-j]==S[i+j]:       #單數的回文不論中間字母為何,左右對稱即可
               s1=S[i-j:i+j+1]     #s1暫存新找到的回文
               if len(s1)>len(s):  #若新找到的回文長度更長則取代舊的
                    s=s1           
               continue
          else:                    #若不對稱則直接退出繼續找下一個i
               break
               
for i in range(0,L):               #判斷雙數個字的回文
     for j in range(0,min(i+1,L-i-1)):
          if S[i-j]==S[i+j+1]:
               s2=S[i-j:i+j+2]
               if len(s2)>len(s):
                    s=s2
               continue
          else:
               break

print('Longest palindrome substring is:',s)  #輸出結果
print('Length is:',len(s))
          
