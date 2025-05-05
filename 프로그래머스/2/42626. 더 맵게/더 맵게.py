'''
모든 음식의 스코빌 지수를 K이상으로 만들고 싶어한다.
모든 음식의 스코빌 지수를 K이상으로 만들기 위해 스코빌 지수가 가장 낮은 두개의 음식을 아래와 같이 섞어 새로운 음식으로 만듦
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

모든 음식의 스코빌 지수가 K이상이 될 때까지 반복

스코빌 지수를 담은 배열 scoville : 2 <= len(scoville) <= 1,000,000
0 <= K <= 1,000,000,000

모든 음식의 스코빌 지수를 K이상으로 만들 수 없을 경우 -1
'''
import heapq
def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while len(scoville) >= 2 and scoville[0] < K:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        heapq.heappush(scoville, first + second*2)
        answer += 1
    
    if scoville[0] < K:
        return -1
    else:
        return answer
    