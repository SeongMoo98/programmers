'''
주어진 항공권을 모두 이용하여 여행경로를 짜려고 한다(항상 "ICN" 공항에서 출발)

항공권 정보가 담긴 2차원 배열 tickets이 주어질 때, 방문하는 공항 경로를 배열에 담아 return

- 모든 공항은 알파벳 대문자 3글자
- 주어진 공항의 수는 3개 이상 10000개 이하
- 주어진 항공권은 모두 사용
- 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로 선택
- 모든 도시를 방문할 수 없는 경우는 주어지지 않는다

'''
from collections import defaultdict

# "항공권이 중복 될 수 있다"
# ==> tickets에서 하나씩 빼서 사용
def solution(tickets):

    answer = []
    visited = [False] * len(tickets)



    def dfs(curr, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return

        for idx, ticket in enumerate(tickets):
            u, v = ticket
            if u == curr and visited[idx] == False:
                visited[idx] = True
                dfs(v, path + [v])
                visited[idx] = False


    dfs("ICN", ["ICN"])

    answer.sort()

    return answer[0]

solution([["ICN", "BBB"], ["BBB", "ICN"], ["ICN", "AAA"]])