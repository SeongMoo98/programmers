# 두개의 단어 begin, target
# 단어의 집합 words
# 1. 한 번에 한 개의 알파벳만 바꿀 수 있다
# 2. words에 있는 단어로만 변환 가능

# 최소 몇단계의 과정을 거쳐 begin에서 target으로 변환할 수 있는지 

from collections import deque
# 모든 단어의 길이는 같다
def bfs(begin, target, words):
    q = deque()
    visited = []
    
    q.append(begin)
    visited.append(begin)
    ret = 0
    while q:
        nq = deque()
        
        for curr in q:    
            if curr == target:
                return ret 
            for word in words:
                if word in visited:
                    continue
                count = 0
                for i in range(len(curr)):
                    if curr[i] != word[i]:
                        count += 1

                if count == 1:
                    nq.append(word)
                    visited.append(word)

        q = nq
        ret += 1
    return 0
                    
                    
    
def solution(begin, target, words):
    visited = [False] * len(words)
    answer = bfs(begin, target, words)
    return answer