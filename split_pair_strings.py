def solution(n):
    result = []
    for i in range(0, len(n), 2):
        if len(n) % 2 != 0:
            n += "_"
        result.append(n[i:i + 2])
        
    print(result)
        

solution("asdfadsf")
solution("asdfads")
solution("")
solution("x")



        