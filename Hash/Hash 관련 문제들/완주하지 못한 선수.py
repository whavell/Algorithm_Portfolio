def solution(participant, completion):
    runners = {}
    answer = 'Error'

    for i in participant: # 딕셔너리를 채우는 for문
        if i not in runners:
            runners[i] = 1
        
        else:
            runners[i] += 1

    for l in completion: # com을 돌면서 딕셔너리값을 갱신하는 for문
        if l in runners:
            runners[l] = runners[l]-1

        else:
            return l

    for j in runners: # 선수가 들어왔는지 확인하는 for문
        if runners[j] == 0:
            pass

        else:
            answer = j

    return answer
