'''
섬 연결하기

N개의 섬 사이에서 다리를 건설하는 비용이 주어질 때, 최소의 비용으로 모든 섬이 서로 통행가능 하도록 만들 때 
필요한 최소 비용 return

1 <= N <= 100
1 <= len(costs) <= ((n-1)n) / 2
'''

'''
모든 노드를 연결하는 그래프 만들기 -> Minimum Spanning Tree
'''

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    
    if a != b:
        parent[a] = b
    return parent

def find(x, parent):
    if parent[x] == x:
        return x
    # 경로 압축
    parent[x] = find(parent[x], parent)
    return parent[x]
    
        
def solution(N, costs):
    answer = 0
    parent = list(range(N))
    visited = [False] * N
    
    costs.sort(key=lambda x : x[2])
    MST, total_weight = [], 0 
    
    for cost in costs:
        u, v, c = cost
        if find(u, parent) != find(v, parent):
            parent = union(u, v, parent)
            MST.append(cost)
            total_weight += c
    
    return total_weight