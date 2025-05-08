'''
배달
N개의 마을로 이루어진 나라(양방향 통행)
N개의 마을 중에서 K시간 이하로 배달이 가능한 마을만 주문 받으려 한다

마을의 개수 N : 1 <= N <= 50
각 마을을 연결하는 도로의 정보 road : 1 <= len(road) <= 50
    두 마을을 연결하는 도로는 여러개 있을 수 있다.
음식 배달 가능한 시간 K

1번 마을에 있는 음식점이 K 이하의 시간에 배달 가능한 마을의 개수
'''
import heapq
from collections import defaultdict

def dijkstra(graph, start, distances):
    distances[start] = 0
    
    pq = [(0, start)]
    
    heapq.heapify(pq)
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        
        for next_node, next_dist in graph[curr_node]:
            total_dist = distances[curr_node] + next_dist
            if total_dist < distances[next_node]:
                distances[next_node] = total_dist
                heapq.heappush(pq, (total_dist, next_node))
    return distances
    
def solution(N, road, K):
    answer = 0
    graph = defaultdict(list)
    graph_temp = [[0] * (N+1) for _ in range(N+1)]
    for u, v, c in road:
        if graph_temp[u][v] != 0:
            graph_temp[u][v] = min(graph_temp[u][v], c)
            graph_temp[v][u] = min(graph_temp[v][u], c)
        else:
            graph_temp[u][v] = c
            graph_temp[v][u] = c
            
    for u in range(1, N+1):
        for v in range(1, N+1):
            if graph_temp[u][v] != 0:
                graph[u].append((v, graph_temp[u][v]))
    print(graph)
    INF = float('inf')
    distances = [INF] * (N + 1)
    res = dijkstra(graph, 1, distances)
    
    for a in res:
        if a <= K:
            answer += 1
    return answer