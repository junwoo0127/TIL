#두 배열의 원소 교체
# 내가 푼 방식
# A리스트를 오름차순 B리스트를 내림차순으로정렬해서
# 각 원소들을 바꿔주는 방식
# 그러나 B가 A보다 작아질 수도 있는 조건을 만족하지 못함
n,k=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort(reverse=True)

for i in range(k):
  A[i],B[i]=B[i],A[i]

print(sum(A))

# 책에서 푼 방식
# 같은 방식이지만 비교 조건을 넣어준 방식
n,k=map(int,input().split())
a=list(map(int, input().split()))
b=list(map,input().split())

a.sort()
b.sort(reverse=True)

for i in range(k):
  if a[i]<b[i]:
    a[i],b[i]=b[i],a[i]
  else:
    break

print(sum(a))
