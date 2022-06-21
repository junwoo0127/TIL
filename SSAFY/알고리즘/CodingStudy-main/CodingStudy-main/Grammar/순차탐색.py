#순차 탐색 소스 코드 구현
#O(N)
def sequential_search(n,target,array):
  for i in range(n):
    if array[i] == target:
      return i+1

print("생성한 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하시오")
input_data=input().split()
#0번째 데이터는 갯수이므로 n에 할당
n=int(input_data[0])
#1번째 데이터는 타겟
target=input_data[1]

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한칸으로 합니다.")
array=input().split()

#입력 원소 중 타겟이 들어간 원소가 몇번째인지 출력
print(sequential_search(n,target,array))
