n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
#3개의 폭탄중 N개 고르기 - 경우의 수 (3**폭탄수) 하나 씩 돌면서 초토화 범위 구하기
location=[] # 폭탄 위치 찾기
best = 0
bomb_list=[]
for i in range(n):
    for j in range(n):
        if(grid[i][j]==1):
            location.append((i,j))

def get_bomb(depth,max_bomb):    
    if (depth==max_bomb):
        n_grid = [row[:] for row in grid] 
        global best
        bomb = 0

    #마지막 폭탄까지 골랐으면 폭파 지역 추가
        for b in range(max_bomb):
            y,x = location[b]
            if(bomb_list[b]==0):
                y-=2
                for boom in range(5):
                    if(y>=0 and y<n):
                        n_grid[y][x]=1
                    y+=1
            elif(bomb_list[b]==1):
                grid_xy=[[1,0],[0,1],[-1,0],[0,-1]]
                for boom in range(4):
                    if(x+grid_xy[boom][1]>=0 and x+grid_xy[boom][1]<n and y+grid_xy[boom][0]>=0 and y+grid_xy[boom][0]<n):
                        n_grid[y+grid_xy[boom][0]][x+grid_xy[boom][1]]=1
            else:
                grid_xy=[[1,1],[-1,1],[-1,-1],[1,-1]]
                for boom in range(4):
                    if(x+grid_xy[boom][1]>=0 and x+grid_xy[boom][1]<n and y+grid_xy[boom][0]>=0 and y+grid_xy[boom][0]<n):
                        n_grid[y+grid_xy[boom][0]][x+grid_xy[boom][1]]=1        
    #갯수 세기 후 비교 
        for i in range(n):
            for j in range(n):
                if(n_grid[i][j]==1):
                    bomb+=1
        if(bomb > best):
            best=bomb
        return 

    for shape in range(3):
        bomb_list.append(shape)
        get_bomb(depth+1,max_bomb)
        bomb_list.pop()

get_bomb(0,len(location))
print(best)
  
   

     