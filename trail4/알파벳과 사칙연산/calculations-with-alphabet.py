expression = input()
dictionary = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0} #a~i에 하나씩 넣기 2**12
best = -2**31
def select_num(count):
    global best
    global dictionary
    arr='abcdef'
    if(count == 6):
        total = dictionary[expression[0]]
        for e in range(1,len(expression),2):
            operator = expression[e]
            next_val = dictionary[expression[e+1]]
            if(operator=='+'):
                total+=next_val
            elif(operator=='-'):
                total-=next_val
            elif(operator=='*'):
                total*=next_val
            #최댓값 인지 계산 
        if(total > best):
            best = total

    for i in range(count,6):
        current_char=arr[count]
        for j in range(4):
            dictionary[current_char]=j+1
            select_num(i+1)

select_num(0)
print(best)
# Please write your code here.
