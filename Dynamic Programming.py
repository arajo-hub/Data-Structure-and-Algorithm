# 동적계획법(Dynamic Programming)은 복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법이다.
# 메모이제이션(Memoization)은 프로그램이 동일한 계산을 반복할 때,
# 이전에 계산한 값을 메모리에 저장함으로써 동일한 계산의 반복적인 수행을 생략하여 프로그램의 실행 속도를 빠르게 하는 기법이다. (동적계획법의 핵심)

# 대표적인 예로 피보나치 수열이 있다.

import sys

N=int(sys.stdin.readline())
numList=[0 for i in range(N+1)] # N번째 피보나치 수를 구하고자 할 때, N길이의 0이 들어있는 리스트를 만든다.
numList[1]=1 # 1번째 값에는 1을 넣어준다. numList=[0, 1, ... ]와 같이 된다.

for i in range(2, N+1): # 두번째부터(위에서 첫번째까지는 값을 넣어주었기 때문에)
    numList[i]=numList[i-1]+numList[i-2]
    print(numList)# 앞앞수와 앞수를 더해서 값을 바꿔준다.

print(numList[-1]) # 제일 마지막에 있는 수를 출력하면 된다.