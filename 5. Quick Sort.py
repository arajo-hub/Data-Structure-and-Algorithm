# Quick Sort는 pivot을 지정하여 pivot을 기준으로 크면 오른쪽, 작으면 왼쪽으로 정렬하는 방법이다.

def listSplit(numList, low, high):
    pivot=list[high] # pivot값을 제일 오른쪽에 있는 값으로 지정한다.
    i=low-1
    for j in range(low, high): # numList를 훑어서
        if list[j]<pivot: # pivot값보다 작다면
            i=i+1 # i를 한 칸 당겨서
            list[i], list[j]=list[j], list[i] # list[i]와 list[j]를 바꿔준다.
    list[i+1], list[high]=list[high], list[i+1] # list[i+1]에는 pivot값이 들어가게 되고, list[i+1]이었던 값은 가장 오른쪽으로 넘어간다.
    # 이렇게 되면 결과적으로 pivot값을 기준으로 왼쪽으로는 작은 값들이, 오른쪽으로는 큰 값들이 모이게 된다. 하지만 그 값들끼리 크기에 따라 정렬이 되어있는지는 모른다.

    return i+1 # pivot값의 index를 반환한다.

def QuickSort(numList, low, high): # QuickSort메소드는 리스트와 리스트가 시작되는 인덱스값(low), 끝나는 인덱스값(high)을 변수로 한다.
    if low<high:
        pivotPosition=listSplit(numList, low, high)

        QuickSort(list, low, pivotPosition-1)
        QuickSort(list, pivotPosition+1, high)