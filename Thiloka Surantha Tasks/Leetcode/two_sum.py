def solution(num, target) :
    for i in range(0,len(num)) :
        for j in range(i+1, len(num)) :
            if num[i] + num[j] == target :
                return [i,j]


result = solution([1,2,3,4,5,6,7,8,9],12)
print(result)