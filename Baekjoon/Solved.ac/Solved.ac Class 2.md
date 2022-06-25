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

