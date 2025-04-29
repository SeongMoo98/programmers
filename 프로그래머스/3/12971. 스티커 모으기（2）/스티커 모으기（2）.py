'''
N개의 스티커가 원형으로 연결

원형으로 연결된 스티커에서 몇 장의 스티커를 뜯어내어 뜯어낸 스티커에 적힌 숫자의 합이 최대
단, 스티커 한 장을 뜯어내면 양쪽으로 인접해있는 스티커는 찢어져서 사용 x

스티커에 적힌 숫자가 배열 형태로 주어질 때, 스티커를 뜯어내어 얻을 수 있는 숫자의 합의 최댓값을 구하여라

1 <= len(sticker) <= 100,00
첫번째 원소와 마지막 원소가 연결되어있다고 간주
'''

def solution(sticker):
    answer = 0
    N = len(sticker)
    # Edge Case
    if N == 1:
        return sticker[0]
    
    # 처음과 끝이 이어진 DP에서는 2개의 DP Table 사용
    # 0번째 sticker를 떼었을때
    dp1 = [0] * N
    dp1[0], dp1[1] = sticker[0], sticker[0]
    
    for i in range(2, N):
        # i-1을 떼거나, 2를 떼고 현재를 뗴거나
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
        
    # 0번째 sticker를 떼지 않았을 때
    dp2 = [0] * N
    dp2[0], dp2[1] = 0, sticker[1]
    for i in range(2, N):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
        
    answer = max(dp1[N-2], dp2[N-1])
    
# DFS 시간 초과
#     visited = [False] * N
    
#     def dfs(curr, visited, res):
#         global answer
                
#         if visited.count(True) == N:
#             answer = max(answer, res)

#         for i in range(N):
#             if visited[i] == False:
#                 left, right = (i-1) % N, (i+1) % N
#                 temp = [i]
#                 visited[i] = True
#                 if visited[left] == False:
#                     visited[left] = True
#                     temp.append(left)
#                 if visited[right] == False:
#                     visited[right] = True
#                     temp.append(right)
#                 res += sticker[i]
#                 dfs(i, visited, res)
#                 for j in temp:
#                     visited[j] = False
#                 res -= sticker[i]
        
#     dfs(0, visited, 0)

    return answer
