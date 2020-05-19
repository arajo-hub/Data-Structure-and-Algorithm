# Merge Sort는 요소를 쪼개고, 합치는(Merge) 과정에서 정렬을 시키는 방법이다.

def mergeSort(numList):
    if len(numList)>1: # 리스트의 길이가 1이 될 때까지 리스트를 쪼갠다.
        middle=len(numList)//2
        left=numList[:middle]
        right=numList[middle:]

        mergeSort(left) # 재귀함수. 위에서 만든 left를 계속 쪼갠다.
        mergeSort(right) # 재귀함수. 위에서 만든 right를 계속 쪼갠다.

        i = j = k= 0

        while i<len(left) and j<len(right): # left와 right가 아직 있을 때
            if left[i]<right[j]: # 왼쪽리스트의 값이 더 작다면
                numList[k]=left[i] # 리스트의 값을 왼쪽리스트의 값으로 바꿔준다.
                i+=1 # 그리고 왼쪽리스트의 빠진 값 다음값과 비교해야하므로 +1을 해준다.
            else: # 오른쪽리스트의값이 더 작다면
                numList[k]=right[j] # 리스트의 값을 오른쪽리스트의 값으로 바꿔준다.
                j+=1 # 그리고 오른쪽리스트의 빠진 값 다음값과 비교해야하므로 +1을 해준다.
            k+=1 # 이미 왼쪽리스트의 값으로든 오른쪽리스트의 값으로든 리스트의 값이 바뀌었으므로 리스트의 다음칸으로 간다.

        while i<len(left): # 왼쪽에 아직 정렬되지 않은 값이 남아있다면
            numList[k]=left[i] # 합쳐진 리스트에 그 값을 넣는다.
            i+=1
            k+=1

        while j<len(right): # 오른쪽에 아직 정렬되지 않은 값이 남아있다면
            numList[k]=right[j] # 합쳐진 리스트에 그 값을 넣는다.
            j+=1
            k+=1

        return numList