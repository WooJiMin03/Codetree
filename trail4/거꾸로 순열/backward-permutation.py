n = int(input())

nums = [i for i in range(n, 0, -1)]
cur_num = []
visited = [False]*n
def dfs():
    global visited
    if(len(cur_num)==n):
        print(*cur_num)
        return
    for i in range(n):
        if(visited[i] == False):
            cur_num.append(nums[i])
            visited[i] = True
            dfs()
            cur_num.pop()
            visited[i] = False
dfs()        
# Please write your code here.
