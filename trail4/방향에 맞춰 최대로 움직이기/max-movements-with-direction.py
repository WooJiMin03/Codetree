n = int(input())
num = [list(map(int, input().split())) for _ in range(n)] #정수 2차원배열
move_dir = [list(map(int, input().split())) for _ in range(n)]#방향 2차원 배열
direction={1:(-1,0),2:(-1,1),3:(0,1),4:(1,1),5:(1,0),6:(1,-1),7:(0,-1),8:(-1,-1)}
r, c = map(int, input().split())
best = 0
def dfs(y,x,count):
    global best
    if(best < count):
        best = count
    cur_num=num[y][x]    
    cur_dir=move_dir[y][x]
    y1, x1=direction[cur_dir]    
    for i in range(n):
        x+=x1
        y+=y1
        if(0<=x<n and 0<=y<n):
            if(cur_num<num[y][x]):
                dfs(y,x,count+1)

dfs(r-1,c-1,0)
print(best)