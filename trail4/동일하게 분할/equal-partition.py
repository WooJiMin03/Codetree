n = int(input())
arr = list(map(int, input().split()))
total_sum=sum(arr)

sums={0}
for num in arr:
    temp=set()
    for s_num in sums:
        temp.add(num+s_num)
    sums.update(temp)
least=float('inf')
for a_sum in sums:
    b_sum=total_sum-a_sum
    diff=abs(a_sum-b_sum)
    least=min(least,diff)

if (least == 0):
    print("Yes")
else:
    print("No")
# Please write your code here.
