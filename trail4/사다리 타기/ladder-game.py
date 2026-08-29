n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
result_arr = [0]*n
for i in range(n):
    result_arr[i]=i+1 
edges.sort(key = lambda x: (x[1],x[0]))
for a,b in edges:
    tmp = result_arr[a-1]
    result_arr[a-1] = result_arr[a]
    result_arr[a]=tmp

least = m
choice = []
arr = [0]*n
for i in range(n):
    arr[i]=i+1

def edge_choice(start,count):
    global least
    global arr
    #확인
    if count >= least: return
    if arr == result_arr:
        least = count
        return
    #선택
    for i in range(start,len(edges)):
        a,b = edges[i]
        arr[a-1], arr[a] = arr[a], arr[a-1]
        edge_choice(i+1,count+1)
        arr[a-1], arr[a] = arr[a], arr[a-1]

edge_choice(0,0)
print(least)
# Please write your code here.
