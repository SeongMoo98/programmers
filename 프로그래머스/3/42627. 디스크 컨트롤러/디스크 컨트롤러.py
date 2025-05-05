'''
하드 디스크는 한번에 하나의 작업만 수행

우선순위 디스크 컨트롤러
1. 작업 번호, 작업 요청 시간, 작업 소요시간을 저장해두는 Ready Queue가 있다
2. 디스크 컨트롤러는 HDD가 작업을 하고 있지 않고 Ready Queue가 비어있지 않다면, 우선순위가 높은 작업을 꺼냄
   HDD에서 그 작업을 진행(소요 시간이 짧은, 요청 시각이 빠른, 작업 번호가 작은 순)
3. 작업을 한 번 시작하면 작업을 마칠 때까지 그 작업만 수행
4. 어떤 작업을 마치는 시점과 다른 작업 요청이 들어오는 시점이 겹친다면, HDD가 작업을 마치자마자 디스크 컨트롤러는
   요청이 들어온 작업을 Ready Queue에 저장한 뒤 우선순위가 높은 작업을 꺼내서 HDD에서 수행
   
모든 요청의 작업 반환 시간의 평균의 정수 부분 return
반환시간 : 작업 요청부터 종료까지 걸린 시간 => 작업 종료 시각 - 요청 시각

각 작업에 대해 [작업 요청 시점, 작업 소요 시간]을 담은 2차원 배열 jobs : 1 <= len(jobs) <= 500
'''
import heapq
def solution(jobs):
    # jobs : [작업 요청 시점, 작업 소요시간]
    answer = 0
    N = len(jobs)
    jobs.sort(key=lambda x:(x[0]))
    visited = [False] * N
    t = 0 
    pq = []

    while True:
        if visited.count(True) == N and not pq:
            break
            
        for i in range(N):
            if t >= jobs[i][0] and visited[i] == False:
                # (소요 시간이 짧은, 요청 시각이 빠른, 작업 번호가 작은 순)
                heapq.heappush(pq, (jobs[i][1], jobs[i][0], i))
                visited[i] = True
                
        # 현재 시점 >= 우선순위 가장 높은 작업의 요청 시점
        if pq and t >= pq[0][1]:
            run_time, request_time, num = heapq.heappop(pq)
            t += run_time
            answer += (t - request_time)
        else:
            t += 1
    
    answer //= N
    
    return answer