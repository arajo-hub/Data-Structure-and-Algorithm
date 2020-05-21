# Heap Sort는 완전이진트리를 이용하여 정렬하는 방법이다.

def Heapify(numList, n, i): # 여기에서의 n은 list의 길이를 말한다. HeapSort메소드에서 등장한다.
    root_largest=i
    left=2*i+1
    right=2*i+2

    if left<n and list[i]<list[left]:
        root_largest=left
    if right<n and list[root_largest]<list[right]:
        root_largest=right
    if root_largest!=i:
        list[i], list[root_largest]=list[root_largest], list[i]
        Heapify(list, n, root_largest)

def HeapSort(numList):
    n=len(list)
    for i in range(n, -1, -1):
        Heapify(list, n, i)

    for i in range(n-1, 0, -1):
        list[i], list[0]=list[0], list[i]
        Heapify(list, i, 0)

list=[3, 2, 5, 10, 7]
HeapSort(list)
print(list)