# 문제
# 원소가 n 개인 list 입력 받기
n, m, k=map(int,input().split())
data = list(map(int, input().split()))
data.sort()
#.sort() => 오름차순 정렬
#.sort(reverse=True) => 내림차순 정렬

result = (data[n-1]*k*(m//k)) + (data[n-2]*(m%k))
# result는 m개의 가장 큰 수와 두번째로 큰 수의 합으로 이뤄짐
# 가장 큰 수(data[n-1]) * k는 m 나누기 k 의 몫 만큼 등장
# 그리고 data[n-2]는 m 나누기 k의 나머지 만큼 등장
# 따라서 총 합을 구하기 위해서는 가장 큰수가 k 번 나오는 값에다가 몇번 등장하는지를 곱하여주고
# 그 값에 두번째로 큰 수가 등장하는 값을 곱한값을 더해준다.

print(result)
