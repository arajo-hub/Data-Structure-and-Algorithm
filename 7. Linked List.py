# Linked List는 기차처럼 각 노드가 한 줄로 연결되어있는 방식이다.

class Node:
    def __init__(self, data):
        self.data=data # 입력된 데이터가 저장되는 부분
        self.next=None # 이 데이터의 다음 데이터를 나타내는 부분(포인터)

node1=Node(10) # data는 10, next는 None
node2=Node(20) # data는 20, next는 None
node3=Node(30) # data는 30, next는 None

node1.next=node2 # 10 다음의 데이터는 20이 되고,
node2.next=node3 # 20 다음의 데이터는 30이 된다.

# [ 백준 1158번 : 요세푸스 문제 ]

# 요세푸스 문제는 다음과 같다.
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# [ 풀이 ]

import sys

N, K=map(int, sys.stdin.readline().split())

numList=list(range(1, N+1))
result=[]
index=K-1 # list의 특성상 index는 0부터 시작하므로 index변수에 -1을 해준다.

for i in range(N): # 주어진 N개의 숫자를 모두 나열해야하므로 N번만큼 for문을 돌린다.
    if len(numList)>index: # N개의 숫자가 들어있는 리스트의 길이가 index보다 크다면
        result.append(numList.pop(index)) # result리스트에 numList에서 뽑은 index위치의 값을 넣는다. # N이 3이라면 numList의 3번째 값.(numList[2])
        index+=(K-1) # 그리고 index는 그자신만큼 더해준다.
    else:  # index가 리스트의 길이를 넘어서면 오류가 난다(out of range). 그렇기 때문에 index값의 수정이 불가피하다.
        index=index%len(numList) # index를 리스트의 길이로 나눈 나머지를 index로 한다. 리스트의 길이만큼 하나의 원을 완성하고 그이후부터 다시 index를 센다고 생각하면 된다.
        result.append(numList.pop(index)) # 그렇게 정의한 index위치에 있는 값을 뽑아 result에 저장한다.
        index+=(K-1) # 그리고 index는 그자신만큼 더해준다.

# 아래는 출력방식.
print("<", end="")
for j in result:
    if j==result[-1]:
        print(j, end="")
    else:
        print("{}, ".format(j), end="")
print(">")