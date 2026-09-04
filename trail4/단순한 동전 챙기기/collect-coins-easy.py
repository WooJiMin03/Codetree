n = int(input())
grid = [list(input()) for _ in range(n)]
dictionary={}
coin_list=[]
least = 1000000
for i in range(n):
    for j in range(n):
        if(grid[i][j]=='S'):
            dictionary['S']=(i,j)
        elif(grid[i][j]=='E'):
            dictionary['E']=(i,j)
        elif(grid[i][j]!='.'):
            num=int(grid[i][j])
            dictionary[num]=(i,j)
            coin_list.append(num)
coin_list.sort()
pick = []
def choose(start_index):
    global least
    if(len(pick) >= 3):
        dis = 0
        dis+=distance(dictionary['S'],dictionary[pick[0]]) #시작부터 첫번쨰 코인
        for c in range(len(pick)-1):
            dis+=distance(dictionary[pick[c]],dictionary[pick[c+1]])
        dis+=distance(dictionary[pick[-1]],dictionary['E'])
        if(dis < least):
            least=dis
            
    for i in range(start_index,len(coin_list)):
        pick.append(coin_list[i])
        choose(i+1)
        pick.pop()

def distance(p1,p2):
    p1_y,p1_x=p1
    p2_y,p2_x=p2
    result=abs(p1_y-p2_y)+abs(p1_x-p2_x)
    return result
choose(0)
if(least==1000000):
    least=-1
print(least)
# Please write your code here.
