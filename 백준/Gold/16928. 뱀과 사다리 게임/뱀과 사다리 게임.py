from collections import deque

N, M  = map(int, input().split())

# 사다리 정보
ladders = {}
for _ in range(N):
    u, v = map(int, input().split())
    ladders[u] = v
# 뱀의 정보
snakes = {}
for _ in range(M):
    u, v = map(int, input().split())
    snakes[u] = v

q = deque([1])
visited = [False] * 101
board = [0] * 101

while q:
    curr = q.popleft()

    if curr == 100:
        print(board[curr])
        break

    for dice in range(1, 7):
        next = curr + dice
        # 범위 내, 미방문
        if next <= 100 and visited[next] == False:
            # 사다리
            if next in ladders:
                next = ladders[next]
            # 뱀
            if next in snakes:
                next = snakes[next]
            # 아무것도 x
            if visited[next] == False:
                visited[next] = True
                board[next] = board[curr] + 1
                q.append(next)


