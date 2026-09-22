n = int(input())
num = [0]*max(3,(n+1))
num[1]=1
num[2]=3
for i in range(3,n+1):
    num[i]=num[i-2]*2+num[i-1]

print(num[n]%10007)
# Please write your code here.
