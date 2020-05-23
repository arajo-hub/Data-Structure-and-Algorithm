# Heap Sort는 완전이진트리를 이용하여 정렬하는 방법이다.

def Heapify(numList, n, i): # 여기에서의 n은 list의 길이를 말한다. HeapSort메소드에서 등장한다.
    root_largest=i # 트리구조에서 root_largest는 가운데에 위치하고
    left=2*i+1 # left는 트리구조에서 root_largest 아래의 왼쪽,
    right=2*i+2 # right는 트리구조에서 root_largest의 오른쪽에 위치한다.

    # 추가. 리스트를 이진트리로 바꾸는 것에 대해.
    # 예를 들어, ['a','b','c','d', 'e']라는 리스트를 트리구조로 나타내면 아래와 같다.
    #                        a(list[0])
    #                b(list[1])       c(list[2])
    #          d(list[3])    e(list[4])
    # 위 구조에서 b(list[1])과 d(list[3]), e(list[4])의 관계를 보자면,
    # 왼쪽에 있는 값은 제일 위에 있는 값의 index값을(b이니까 1이 되겠다.) 2배를 하고 1을 더했다는 것을 알 수 있다.
    # 오른쪽 index값은 당연히 왼쪽index값보다 1보다 크므로 2*i+2가 된다.

    if left<n and list[i]<list[left]: # root가 그 왼쪽에 있는 값보다 작다면,
        root_largest=left # 왼쪽에 있는 값의 index를 root와 바꿔준다.
    if right<n and list[root_largest]<list[right]: # 오른쪽에 있는 값과 비교해서 작다면,
        root_largest=right # 오른쪽에 있는 값의 index를 root로 바꿔준다. 즉, 아래에 더 큰 값이 있다면 그 값으로 index를 바꿔주는 과정이다.
    if root_largest!=i: # 위의 결과에 따라 최종적으로 결정된 root의 index와 원래 root의 index값이 다르다면(=왼쪽이든 오른쪽이든 더 큰 수가 있어서 root가 바뀌었다면)
        list[i], list[root_largest]=list[root_largest], list[i] # 그 더 큰 수와 root의 자리를 바꿔준다.
        Heapify(list, n, root_largest) # 위의 과정을 계속 반복한다.

def HeapSort(numList):
    n=len(list)
    for i in range(n, -1, -1):
        Heapify(list, n, i)

    for i in range(n-1, 0, -1):
        list[i], list[0]=list[0], list[i]
        Heapify(list, i, 0)

    return numList

list=[3, 2, 5, 10, 7]
HeapSort(list)
print(list)