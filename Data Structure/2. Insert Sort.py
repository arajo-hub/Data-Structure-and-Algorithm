# Insert Sort는 key로 설정한 값보다 크면 오른쪽으로 한칸씩 옮겨 key를 적당한 위치에 삽입하여(Insert) 정렬하는 방법이다.
# key보다 작을 경우는 왼쪽에 남겨둔다.

def InsertSort(numList):
    for i in range(1, len(numList)): # key의 경우의 수는 제일 앞에 있는 수를 뺀 나머지 수들. 제일 앞에 있는 수는 두번째 수를 key로 할 때 위치가 정해진다.
        key=numList[i] # key값을 설정하고,
        j=i-1 # j는 key값 앞에 있는 수의 index이다. numList[j]가 key값 앞에 있는 수.
        while j>=0 and key<numList[j]: # key값이 앞에 있는 수보다 작다면,
            numList[j+1]=numList[j] # key값 앞에 있는 수를 뒤로 한 칸 밀고,(=key값의 자리로 밀고)
            j-=1 # key 앞의 수가 하나가 아니라 여러 개일 수 있으므로, key 앞의 수들을 다 가져다가 비교한다.
        numList[j+1]=key # key값이 앞에 있는 수보다 크다면, 그 수의 다음 자리에 key를 넣어준다.
    return numList

# 반복문의 중첩이므로 시간복잡도는 O(n^2)이다.