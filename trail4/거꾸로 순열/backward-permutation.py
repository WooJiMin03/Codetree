import itertools

n = int(input())

# N부터 1까지 내림차순으로 리스트 생성
nums = [i for i in range(n, 0, -1)]

# permutations는 입력된 리스트의 순서를 기준으로 순열을 생성하므로 
# 역사전순으로 바로 출력됨
for p in itertools.permutations(nums):
    print(*p)


# Please write your code here.
