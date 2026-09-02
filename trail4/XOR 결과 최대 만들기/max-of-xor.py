n, m = map(int, input().split())
A = list(map(int, input().split()))
best = 0
num_list=[]
def xor_best(start,count):
    global best 
    if(count == m):
        total = num_list[0]
        for i in range(1,m):
            total^=num_list[i]
        if(best < total):
            best = total
        return    
    for i in range(start,n):
        num_list.append(A[i])
        xor_best(i+1,count+1)
        num_list.pop()
xor_best(0,0)
print(best)