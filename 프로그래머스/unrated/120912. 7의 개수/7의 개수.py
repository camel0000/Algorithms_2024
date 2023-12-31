def solution(array):
    answer = 0
    for s in array:
        s_ = str(s)
        for i in range(len(s_)):
            if s_[i] == '7':
                answer += 1
    return answer