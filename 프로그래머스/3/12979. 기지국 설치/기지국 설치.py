'''
N개의 아파트, 일부 아파트 옥상에 4g 기지국이 설치되어 있다

4g 기지국을 5g 기지국으로 바꾸려한다.
이 때, 5g 기지국은 4g 기지국 보다 전달 범위가 좁아서 어떤 아파트에는 전파가 도달하지 않는다
(전파의 도달 거리가 W(양쪽으로 W만큼))

이때, 5g 기지국을 최소로 설치하면서 모든 아파트에 전파를 전달하려 한다.

아파트 개수 N : 1 <= N <= 200,000,000
기지국이 설치된 아파트 번호 stations 배열 : 1 <= stations[i] <= 10,000 
    stations는 오름차순 정렬
전파도달 거리 W : 1 <= W <= 10,000
'''
def solution(n, stations, W):
    answer = 0
    
    # 일단 O(N)은 안됨
    start = 1
    end = n
    for station in stations:
        u, v = station - W, station + W
        end = u - 1
        if (end - start + 1) % (2*W+1) == 0:
            answer += (end - start + 1) // (2*W+1)
        else:
            answer += (end - start + 1) // (2*W+1) + 1    
        start = v + 1
        
    if start <= n:
        end = n
        if  (end - start + 1) % (2*W+1) == 0:
            answer += (end - start + 1) // (2*W+1)
        else:
            answer += (end - start + 1) // (2*W+1) + 1   

    
    return answer