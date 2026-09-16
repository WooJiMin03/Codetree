from collections import deque
n = int(input())
r1, c1, r2, c2 = map(int, input().split())
directions = [[1,-2],[2,-1],[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2]]#x,y
queue = deque()
best=float('inf')
visited=[[False]*n for _ in range(n)]
queue.append((c1-1,r1-1,0))
visited[r1-1][c1-1] = True
while queue:
    x,y,count = queue.popleft()
    if(x==c2-1 and y==r2-1):
        if(best > count):
            best = count
    for ax,ay in directions:
        nx,ny=ax+x,ay+y
        if(0<=nx<n and 0<=ny<n and not visited[ny][nx]):
            queue.append((nx,ny,count+1))
            visited[ny][nx]=True
if(best == float('inf')):
    best = -1
print(best)
# Please write your code here.
