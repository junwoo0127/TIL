## Class 2 (16문제)

> 체스판 다시 칠하기

```python
N, M = map(int,input().split())
arr = [list(map(str,input())) for _ in range(M)]
count = []
for i in range(N-7):
    for j in range(M-7):
        first_W = 0
        first_B = 0
        for k in range(i,i+8):
            for l in range(j,j+8):
                if (k+l) % 2 == 0:
                    if arr[k][l] != "W":
                        first_W = first_W + 1
                    if arr[k][l] != "B":
                        first_B = first_B + 1
                else:
                    if arr[k][l] != "B":
                        first_W = first_W + 1
                    if arr[k][l] != "W":
                        first_B = first_B + 1
        count.append(min(first_W, first_B))
print(min(count))
```

> 직사각형에서 탈출

```python
x,y,w,h = map(int,input().split())
print(min(x, y, w-x, h-y))
```

> 1181.단어 정렬

```pyth
n = int(input())
lst = []

for i in range(n):
    lst.append(input())
set_lst = set(lst)	## set으로 변환해서 중복값을 제거
lst = list(set_lst)	## 다시 list로 변환
lst.sort()
lst.sort(key = len)

for i in lst:
    print(i)
```

> 2789 블랙잭

```python
N, M = map(int,input().split())
arr = list(map(int,input().split()))
result = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if arr[i] + arr[j] + arr[k] >M:
                continue
            else:
                result = max(result, arr[i]+arr[j]+arr[k])
print(result)

# continue 예시
# a = [1,2,3,4,5,6]
# for i in a:
#     if i == 3:
#         continue
#     else:
#         print(i)
```

> 달팽이는 올라가고 싶다

```python
a,b,v = map(int,input().split())
k = 0	#올라가는 데 걸리는 일수
d = 0	#올라간 높이
while 1:
    k+=1
    if a*k-b*(k-1)>=v:
        break
print(k)
```

> 2231 분해합

```python
N = int(input())
result = 0
for i in range(1,N+1):
    A = sum(map(int,str(i)))
    result = i + A
    if result == N:
        print(i)
        break
    if i == N:
        print(0)

```

> 1966 프린터 큐

```pyt
test_cases = int(input())

for _ in range(test_cases):
    n,m = list(map(int, input().split( )))
    imp = list(map(int, input().split( )))
    idx = list(range(len(imp)))
    idx[m] = 'target'

    # 순서
    order = 0
    
    while True:
        # 첫번째 if: imp의 첫번째 값 = 최댓값?
        if imp[0]==max(imp):
            order += 1
                        
            # 두번째 if: idx의 첫 번째 값 = "target"?
            if idx[0]=='target':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)

        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))   
```

> 2108 통계학

```python
from collections import Counter
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()
cnt = Counter(arr).most_common(2)
print(sum(arr)//N)
print(arr[len(arr)//2])
if len(arr) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(arr)-min(arr))
```

> 2292 벌집

```python
N = int(input())
pile = 1
cnt = 1
while N > pile:
    pile += 6 * cnt
    cnt += 1

print(cnt)
```

> 2775  부녀회장이 될테야

```python
T = int(input())
for tc in range(T):
    k = int(input())
    n = int(input())
    apt = [i for i in range(1, n+1)]
    for i in range(k):
        for j in range(1,n):
            apt[j] += apt[j-1]
    print(apt[-1])
```

> 2805 나무자르기(이분탐색)

```python
N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) #이분탐색 검색 범위 설정

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2
    
    log = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid
    
    #벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
```

> 2869 달팽이는 올라가고 싶다

```python
A,B,V = map(int,input().split())
k = (V-B)/(A-B)
print(int(k) if k == int(k) else int(k)+1)

```

> 10989 수 정렬하기 3

```py
import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
```

> 15829 Hashing

```python
L = int(input())
string = input()
answer = 0

for i in range(L):
    answer += (ord(string[i])-96) * (31 ** i) #아스키 코드 값을 돌려주는 ord함수
print(answer % 1234567891)
```

> 18111 마인크래프트

```python
import sys

n, m, b = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
answer = sys.maxsize
idx = 0

# 0층부터 256층까지 반복
for target in range(257):
    max_target, min_target = 0, 0

    # 반복문을 통해 블록을 확인
    for i in range(n):
        for j in range(m):

            # 블록이 층수보다 더 크면
            if graph[i][j] >= target:
                max_target += graph[i][j] - target

            # 블록이 층수보다 더 작으면
            else:
                min_target += target - graph[i][j]

    # 블록을 뺀 것과 원래 있던 블록의 합과 블록을 더한 값을 비교
    # 블록을 뺀 것과 원래 있던 블록의 합이 더 커야 층을 만들 수 있음.
    if max_target + b >= min_target:
        # 시간 초를 구하고 최저 시간과 비교 
        if min_target + (max_target * 2) <= answer:
        	# 0부터 256층까지 비교하므로 업데이트 될수록 고층의 최저시간
            answer = min_target + (max_target * 2) # 최저 시간
            idx = target # 층수

print(answer, idx)
```

