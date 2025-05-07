'''
다단계 조직을 이용하여 짓솔 판매

판매원이 칫솔을 판매하면 그 이익이 피라미드 조직을 타고 조금씩 분배
어느정도 판매가 이루어진 후, 조직을 운영하던 민호는 조직 내 누가 얼마만큼의 이득을 가져가는지 궁금해짐

민호는 center, 나머지 판매원 존재
각각은 자신을 조직에 참여시킨 추천인에 연결되어 피라미드 식 구조를 이루고 있다.

조직의 이익 분배 규칙
- 모든 판매원은 칫솔의 판매 이익에서 10%를 추천인에게 배분, 나머지는 자신이 가짐
- 모든 판매원은 자신이 칫솔 판매에서 발생한 이익 뿐만 아니라, 자신이 추천하여 가입시킨 판매원에게서 발생하는 이익의 10%도 자신의 이익에 포함
- 자신의 이익 또한 마찬가지의 규칙으로 자신의 추천인에게 분배
- 10%를 계산할 때에는 원단위로 철저히 하며, 1원 미민인 경우 분배 x

각 판매원의 이름을 담은 배열 enroll : 1 <= len(enroll) <= 10000
각 판매원을 조직에 참여시킨 이름은 담은 배열 referral : len(referral) = len(enroll)
    어느 누구의 추천도 없이 가입한 사람은 "-"
판매량 집계 데이터의 판매원 이름을 나열한 배열 seller : 1 <= len(seller) <= 100,000
판매량 집계 데이터의 판매 수량 amount : len(amount) = len(seller)

칫솔 한개를 판매하여 얻어지는 이익은 100원
각 판매원이 득한 이익금을 나열한 배열
'''
import sys
sys.setrecursionlimit(10 ** 6)
def distribute(parent, x, curr_price, res):
    if curr_price == 0:
        return
    
    if x == "-":
        return
    else:
        remain = int(curr_price * 0.1)
        res[x] += (curr_price-remain)
        curr_price = remain
        distribute(parent, parent[x], curr_price, res)
        
def solution(enrolls, referrals, sellers, amounts):
    answer = []
    N = len(enrolls)
    parent = {}
    res = {}
    for enroll, ref in zip(enrolls, referrals):
        parent[enroll] = ref
        res[enroll] = 0
    
    for seller, amount in zip(sellers, amounts):
        # seller가 100 * amount의 이익을 냈고 parent를 따라 가면서 이익 계산
        total = 100 * amount
        # 재귀 깊이 초과? -> 시간 초과
        # 즉, DFS로 시간 초과 발생
        # 올라가면서 분배하고, 0이면 그만
        distribute(parent, seller, total, res)
            
    for enroll in enrolls:
        answer.append(res[enroll])
    
    return answer