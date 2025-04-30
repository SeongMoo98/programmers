'''
쇼핑을 할 때면 매장 진열대의 특정 범위의 물건들을 모두 싹쓸이 구매하는 습관이 있다

하지만 어느날은
'진열된 모든 종류의 보석을 적어도 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매'

진열대 번호 순서대로 보석들의 이름이 저장된 배열 gems : 1 <= len(gems) <= 100,000

가장 짧은 구간의 시작 진열대 번호와 끝 진열대 번호를 차례대로 배열에 담아 return
가장 짧은 구간이 여러개라면 시작 진열대 번호가 가장 작은 구간 선택
 
'''
def solution(gems):
    answer = [0, len(gems)]
    
    unique_gems = set(gems)
    left, right = 0, len(gems)-1
    
    gem_dict = dict()
    for right in range(len(gems)):
        gem = gems[right]
        gem_dict[gem] = gem_dict.get(gem, 0) + 1

        # 모든 종류가 포함됐을 때
        while len(gem_dict) == len(unique_gems):
            # 현재 구간이 더 짧다면 업데이트
            if right - left < answer[1] - answer[0]:
                answer = [left, right]

            # 왼쪽 포인터 줄이기
            gem_dict[gems[left]] -= 1
            if gem_dict[gems[left]] == 0:
                del gem_dict[gems[left]]
            left += 1

    return [answer[0] + 1, answer[1] + 1]  # 문제 조건이 1-indexed

#     # 시간 초과
#     unique_gems = set(gems)
#     k = len(unique_gems)
    
#     while True:
#         for i in range(len(gems)-k+1):
#             if set(gems[i:i+k]) == unique_gems:
#                 return [i + 1, i+k]
#         else:
#             k += 1
        