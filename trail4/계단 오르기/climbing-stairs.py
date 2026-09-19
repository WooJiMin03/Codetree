n = int(input())
count = 0
n_list = [-1]*max(4,n+1)
n_list[1]=0
n_list[2]=1
n_list[3]=1
def dfs(num):
    for i in range(4,n+1):
        n_list[i]=n_list[i-2]+n_list[i-3]
dfs(n)
print(n_list[n]%10007)
# Please write your code here.