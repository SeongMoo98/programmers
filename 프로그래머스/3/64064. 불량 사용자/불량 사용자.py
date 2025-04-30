'''
이벤트에 비정상적인 방법으로 당첨을 시도한 "불량 응모자" 발견

이들의 목록을 만들어서 당첨 처리 시 제외하려한다.
이 때, 개인정보 보호를 위해 사용자 아이디 중 일부 문자를 "*"로 마스킹
가리고자 하는 문자 하나에 "*" 문자 하나를 사용하였고, 아이디 당 최소 하나 이상의 "*"를 사용

불량 사용자 목록에 매핑된 응모자 아이디를 "제재 아이디"라 한다.

응모자 아이디 목록 user_id (마스킹 x) : 1 <= len(user_id) <= 8
    1 <= len(user_id[i]) <= 8
불량 사용자 아이디 목록 banned_id(마스킹) : 1 <= len(banned_id) <= len(user_id)

당첨에서 제외되어야 할 제재 아이디 목록은 몇가지 경우의 수가 가능한지 return
'''
from itertools import permutations
def check(users, banned_id):
    for i in range(len(banned_id)):
        if len(users[i]) != len(banned_id[i]):
            return False

        for j in range(len(users[i])):
            if banned_id[i][j] == "*":
                continue
            if banned_id[i][j] != users[i][j]:
                return False
    return True

def solution(user_id, banned_id):
    
    answer = []
    # user_id에서 제재 사용자 수 만큼 추출
    user_permutation = list(permutations(user_id, len(banned_id)))
    
    for users in user_permutation:
        if check(users, banned_id):
            users = set(users)
            if users not in answer:
                answer.append(users)

                                
                        
    return len(answer)