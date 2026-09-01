n = int(input())
num = list(map(int, input().split()))
least = 10000

def dfs(location,count):
    global least
    if(location == n-1):
        if(count < least):
            least=count
            return
    if(num[location] != 0):        
        for i in range(1,num[location]+1):
            if(location+i<n):
                dfs(location+i,count+1)        
    else:
        return
# Please write your code here.
dfs(0,0)
if(least == 10000):
    least = -1
print(least)