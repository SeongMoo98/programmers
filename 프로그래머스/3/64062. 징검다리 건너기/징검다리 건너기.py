'''
가을 소풍 가는 중에 징검다리가 있는 개울을 만나서 건너편으로 건너려 한다.

- 징검다리는 일렬로 놓여있고 각 징검다리의 디딤돌에는 숫자가 적혀있다(밟으면 1씩 줄어듦)
- 디딤돌의 숫자가 0이 되면 더 이상 밟을 수 없으며, 이때는 다음 디딤돌로 한번에 여러 칸을 건너뛸 수 있다
- 단, 다음으로 밟을 수 있는 디딤돌이 여러 개인 경우 무조건 가장 가까운 디딤돌로만 건너뛸 수 있다

한번에 한명씩 징검다리를 건너야 하며, 한 친구가 모두 건넌 후 그 다음 친구가 건넌다

징검다리를 건너야 하는 친구들의 수는 무제한이라 간주
디딤돌에 적힌 숫자 stones : 1 <= len(stones) <= 200,000
한번에 건너뛸 수 있는 디딤돌의 최대 칸 수 k : 1 <= k <= len(stones)

최대 몇 명까지 징검다리를 건널 수 있는지 구하여라

'''

def solution(stones, k):
    
    # 시간 초과..!
    # 이분 탐색? Heap?
    left, right = 1, 200000000
    
    while left <= right:
        mid = (left+right) // 2
        zero_count = 0
        for i in range(len(stones)):
            if stones[i] - mid <= 0:
                zero_count += 1
            else:
                zero_count = 0
            if zero_count >= k:
                break
                
        if zero_count >= k:
            right = mid - 1
        else:
            left = mid + 1
            
    return left
    
    
    
        
        
    

    

#     # 답은 맞는데 시간 초과
#     N = len(stones)
#     while True:
#         zero_count = 0
#         count = 0
#         min_value = float('inf')
#         for i in range(N):
#             if stones[i] == 0:
#                 count += 1
#             else:
#                 count = 0
#                 min_value = min(min_value, stones[i])
#             zero_count = max(zero_count, count)
            
#         if zero_count >= k:
#             break
#         answer += min_value
#         for i in range(N):
#             if stones[i] != 0:
#                 stones[i] -= min_value
        
    