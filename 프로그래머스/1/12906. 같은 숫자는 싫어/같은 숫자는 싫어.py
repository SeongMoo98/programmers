'''
arr의 원소는 숫자 0부터 9까지
연속적으로 나타나는 숫자는 하나만 남기고 전부 제거
제거된 후 남은 수들을 반환할 때는 베열 arr의 연소들의 순서를 유지해야한다

'''
def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if answer[-1] == arr[i]:
            continue
        else:
            answer.append(arr[i])
        
    return answer