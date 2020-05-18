# Merge Sort는 요소를 쪼개고, 합치는(Merge) 과정에서 정렬을 시키는 방법이다.

def MergeSort(numList):
    if len(numList)>1: # 리스트의 길이가 1이 될 때까지 리스트를 쪼갠다.
        middle=len(numList)//2
        left=list[:middle]
        right=list[middle:]
        MergeSort(left) # 재귀함수. 위에서 만든 left를 계속 쪼갠다.
        MergeSort(right) # 재귀함수. 위에서 만든 right를 계속 쪼갠다.

        i=0
        j=0
        merged=[]

        while i<len(left) and j<len(right): # left와 right가 아직 있을 때
            if left[i]<right[j]: # 왼쪽리스트의 값이 더 작다면
                merged.append(left[i]) # left와 right를 합치는 결과리스트에 왼쪽리스트의 값을 추가한다.
                i+=1 # 그리고 왼쪽리스트의 빠진 값 다음값과 비교해야하므로 +1을 해준다.
            else: # 오른쪽리스트의 값이 더 작다면
                merged.append(right[j]) # left와 right를 합치는 결과리스트에 오른쪽리스트의 값을 추가한다.
                j+=1 # 그리고 오른쪽리스트의 빠진 값 다음값과 비교해야하므로 +1을 해준다.

        while i<len(left):
            merged.append(left[i])
            i+=1

        while j<len(right):
            merged.append(right[j])
            j+=1

        return merged

list=[3, 5, 4, 7, 10]
MergeSort(list)
print(list)