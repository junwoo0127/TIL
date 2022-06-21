# 빈 리스트 선언
a=list()
b= []
print(a)
print(b)

# 크기가 N이고 모든 값이 0 인 1차원 리스트
n=10
a=[0]*n
print(a)

# 리스트 특정 원소에 접근
# 뒤에서 첫번째 원소
a=[1,2,3,4,5,6,7,8,9]
print(a[-1])
# 두번째 원소 부터 네번째 원소 까지
print(a[1:4])

# 리스트 컴프리헨션 : 초기화
# 0에서 19 까지 수 중에서 홀 수만 포함하는 리스트
array=[i for i in range(20) if i%2==1]
print(array)

# 1부터 9까지 제복 값을 포함하는 리스트
array = [i*i for i in range(1,10)]
print(array)

# N X M 크기의 2차원 리스트 초기화
n=3
m=4
array = [[0]*m for _ in range(n)] # 반복을 위한 변수의 값을 무시할 때 _ 사용
print(array)
