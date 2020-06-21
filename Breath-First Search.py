# 너비 우선 탐색(Breath-First Search)은 트리 또는 그래프에서 너비를 우선하여 탐색하는 알고리즘이다.
# 너비 우선 탐색을 사용하는 문제는 일반적으로 시작 노드에서 특정 노드에 도달하는 데 필요한 최단 경로를 찾는 문제.
# 시간복잡도는 O(도달할 수 있는 노드 수 + 도달할 노드에서 나가는 간선 수)이다.

def BFS(start_node):
    # 1) queue 에 첫 번째 노드 넣으면서 시작
    queue = [start_node, ]

    while True:
        # 2) queue가 비어있는지 확인
        if len(queue) == 0:
            print('All node searched.')
        return None

        # 3) queue에서 맨 앞의 노드를 dequeue (0번 인덱스를 pop)
        node = queue.pop(0)

        # 4) 만약 node가 찾고자 하는 target이라면 서치 중단!
        if node == TARGET:
            print('The target found.')
        return node

        # 5) node의 자식을 expand 해서 children에 저장
        children = expand(node)

        # 6) children을 stack에 쌓기
        queue.extend(children)

# 코드 출처 : https://jeinalog.tistory.com/18

# append와 extend는 리스트에 새로운 원소를 추가하는 방법이지만, 출력물에서 차이가 있다.
# append(['a','b']인 경우, 본래의 리스트에 [['a', 'b']]의 식으로 추가되지만,
# extend는 ['a', 'b']의 형태로 추가된다.
# 그리고 append('Hello')의 경우['hello']의 식으로 추가되지만,
# extend는 ['h', 'e', 'l', 'l', 'o']의 식으로 추가된다.