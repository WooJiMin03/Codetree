import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

max_height = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] > max_height:
            max_height = grid[i][j]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(y, x, k, visited):
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        

        if 0 <= ny < N and 0 <= nx < M:
            if not visited[ny][nx] and grid[ny][nx] > k:
                visited[ny][nx] = True
                dfs(ny, nx, k, visited)

best_k = 1
max_zones = -1

for k in range(1, max_height + 1):
    visited = [[False] * M for _ in range(N)]
    zones = 0
    
    for i in range(N):
        for j in range(M):
           
            if grid[i][j] > k and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, k, visited)
                zones += 1  
                
    if zones > max_zones:
        max_zones = zones
        best_k = k

print(best_k, max_zones)

# Please write your code here.
