# Heap은 이진 트리(Binary tree)의 자료구조를 나타낸다.
# Heap은 일반적으로, 리스트에서 가장 작은(또는 가장 큰) 요소에 반복적으로 접근할 경우 사용한다.
# Heap을 이용하여 가장 작은(또는 가장 큰) 요소를 처리할 경우, 시간복잡도는 O(1)이고, 그외 조회, 추가, 수정을 처리할 경우는 O(logN)이다.

# Heapq 모듈
# heapify : 리스트를 힙으로 변환해주는 함수
# heappush : 힙에 요소를 추가하는 함수
# heappop(heap) : 힙에서 가장 작은 항목을 제거하고 반환하는 함수
# 그외 heappushpop, heapreplace, merge 등이 있다.