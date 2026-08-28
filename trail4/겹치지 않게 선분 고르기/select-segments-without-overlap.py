n = int(input())
x1, x2 = [], []
for _ in range(n):
    a, b = map(int, input().split())
    x1.append(a)
    x2.append(b)
line = []
best = 0
def select_line(start,count):
    global best
    for i in range(start,n):
        a,b =x1[i],x2[i] 
        if(safe(a,b)):
            line.append([a,b])
            if(count+1>best):
                best=count+1
            select_line(i+1,count+1)
            line.pop()
    return
# Please write your code here.

def safe(a,b):
    for a1,b1 in line:
        if(a1<=a<=b1 or a1<=b<=b1 or (a<=a1 and b>=b1)):
            return False
    return True

select_line(0,0)
print(best)