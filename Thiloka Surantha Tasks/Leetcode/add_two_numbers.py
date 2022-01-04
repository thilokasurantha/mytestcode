def solution(get_list) :
    s = ""
    i = -1

    while True :
        s = s + str(get_list[i])

        i = i -1

        if len(s) == len(get_list) :
            break

    return s

first = solution([2,3,4])
last = solution([5,6,4])

answer = int(first) + int(last)
print(answer)