# 깊이우선탐색(Depth-First Search)은 그래프 또는 트리에서 깊이를 우선으로 탐색하는 알고리즘이다.
# 시간복잡도는 O(도달할 수 있는 노드 수 + 도달할 노드에서 나가는 간선 수)이다.

# 전위 순회 : 루트 노드 → 왼쪽 노드 → 오른쪽 노드 순으로 방문
# 후위 순회 : 왼쪽 노드 → 오른쪽 노드 → 루트 노드 순으로 방문
# 중위 순회 : 왼쪽 노드 → 루트 노드 → 오른쪽 노드 순으로 방문

def DFS(start_node):
    # 1) stack 에 첫 번째 노드 넣으면서 시작
    stack = [start_node, ]

    while True:
        # 2) stack이 비어있는지 확인
        if len(stack) == 0:
            print('All node searched.')
        return None

        # 3) stack에서 맨 위의 노드를 pop
        node = stack.pop()

        # 4) 만약 node가 찾고자 하는 target이라면 서치 중단!
        if node == TARGET:
            print('The target found.')
        return node

        # 5) node의 자식을 expand 해서 children에 저장
        children = expand(node)

        # 6) children을 stack에 쌓기
        stack.extend(children)

        # 7) 이렇게 target을 찾거나, 전부 탐색해서 stack이 빌 때까지 while문 반복

# 코드 출처 : https://jeinalog.tistory.com/18