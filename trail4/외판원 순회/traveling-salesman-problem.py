n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]
visited = [False]*(n) #순열 구하기
visited[0] =True
least = float('inf')
num_list = [1]
def dfs(count):
    global least
    if(count == n):
        total = 0
        for i in range(n):
            if(i==n-1):
                a=b
                b=1-1
                if(A[a][b]==0):
                    return
                total+=A[a][b]
                break
            a=num_list[i]-1
            b=num_list[i+1]-1
            total+=A[a][b]
        
        if(total < least):
            least = total
        
    for i in range(n):
        a=num_list[-1]-1
        if(not visited[i] and (A[a][i] != 0)):
            num_list.append(i+1)
            visited[i]=True
            dfs(count+1)
            num_list.pop() 
            visited[i]=False 
dfs(1)
print(least)
# 1부터 N까지의 정점 찍을때 최소 값 구하기 -> 방문 순서(시작은 1행 -> 1행에서 고른 j행으로 이동 -> 이전에 고른 행빼고 선택 visited 있어야할듯 + 0일 경우 방문x)
# Please write your code here.
