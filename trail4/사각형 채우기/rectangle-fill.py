n = int(input())

n_list=[0]*max(3,(n+1))
n_list[1]=1
n_list[2]=2
for i in range(3,n+1):
    n_list[i]=n_list[i-1]+n_list[i-2]
print(n_list[n]%10007)
# Please write your code here.2*2 
