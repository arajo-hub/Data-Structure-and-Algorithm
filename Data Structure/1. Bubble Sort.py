# Bubble Sort는 나열된 수들을 앞에서부터 비교해가면서 작으면 왼쪽, 크면 오른쪽으로 위치를 바꾸어 정렬하는 방법이다.

def BubbleSort(numList):
    for i in range(len(numList)-1): # 앞에서부터 하나의 수를 뽑는다고 했을 때, 그 수의 경우의 수. 만약 5개의 수가 들어있는 리스트라면 비교를 위해 뽑는 제일 앞 수의 경우의 수는 네 가지가 되는 이치이다.
        for j in range(len(numList)-1-i): # 하나의 수를 뽑았다면, 그 수의 다음 수와 비교해야 하므로 len(numList)-1에 -i를 해준다.
            if numList[j] > numList[j+1]:
                numList[j], numList[j+1]=numList[j+1], numList[j]
    return numList

# 반복문의 중첩이므로 시간복잡도는 O(n^2)이다.

# [ 백준 2947번 : 나무 조각 ]

# 동혁이는 나무 조각을 5개 가지고 있다. 나무 조각에는 1부터 5까지 숫자 중 하나가 쓰여져 있다. 또, 모든 숫자는 다섯 조각 중 하나에만 쓰여 있다.
# 동혁이는 나무 조각을 다음과 같은 과정을 거쳐서 1, 2, 3, 4, 5 순서로 만들려고 한다.
# 첫 번째 조각의 수가 두 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 두 번째 조각의 수가 세 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 세 번째 조각의 수가 네 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 네 번째 조각의 수가 다섯 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
# 만약 순서가 1, 2, 3, 4, 5 순서가 아니라면 1 단계로 다시 간다.
# 처음 조각의 순서가 주어졌을 때, 위치를 바꿀 때 마다 조각의 순서를 출력하는 프로그램을 작성하시오.

# [ 풀이 ]

import sys

parts=list(map(int, sys.stdin.readline().split()))

for i in range(len(parts)-1):
    for j in range(len(parts)-1-i):
        if parts[j] > parts[j+1]:
            parts[j], parts[j+1]=parts[j+1], parts[j]
            print(*parts)