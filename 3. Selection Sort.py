# Selection Sort는 남아있는 수들 중 가장 작은 값을 선택하여(Selection) 앞으로 꺼내면서 정렬하는 방법이다.

def SelectionSort(numList):
    for i in range(len(numList)-1):
        min_index=i # 가장 작은 값의 위치를 나타낼 min_index. 수의 나열 중 가장 앞에 있는 수를 초기값으로 갖는다.
        for j in range(i+1, len(list)): # min_index 다음으로 나열된 수들 중 가장 작은 수를 찾는다.
            if numList[min_index]>list[j]: #제일 앞에 있는 수(numList[i])보다 뒤에 나열된 수들 중 작은 수가 있다면,
                min_index=j # min_index를 그 작은 수의 인덱스(j)로 바꿔준다.
        numList[i], numList[min_index]=numList[min_index], numList[i] # 그리고 새로 찾은 가장 작은 수와 가장 앞에 있던 수를 바꿔준다.
    return numList