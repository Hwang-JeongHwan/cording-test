def solution(s):
    N = len(s)
    answer = N
    # 1개 단위 (step) 부터 압축 단위를 늘려가며 확인
    for step in range(1, (N // 2) + 1):
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        result = ''
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, N, step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                result += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        # 남아있는 문자열에 대해서 처리
        result += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답 
        answer = min(len(result), answer)


    return answer


s = input()
print(solution(s))
