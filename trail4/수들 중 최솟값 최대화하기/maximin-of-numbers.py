n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [False]*n#첫번째 줄 행 두번째 줄 열
best = -float('inf')
def choose(count,least):
    global best
    if(count == n):
        if(least > best):
            best = least
        return
    for i in range(n):
        if(not visited[i]):
            visited[i]=True
            c_least=min(least,grid[count][i])
            choose(count+1,c_least)
            visited[i]=False
        
            
choose(0,float('inf'))
print(best)
# Please write your code here.
