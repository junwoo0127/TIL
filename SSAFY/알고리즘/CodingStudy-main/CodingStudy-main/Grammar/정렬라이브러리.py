#sorted()
#정렬 라이브러리는 최악의 경우도 시간복잡도 NlogN임
#병렬 정렬과 삽입 정렬의 아이디어를 더한 하이브리드 방식의 알고리즘 사용
#별도의 요구가 없다면 기본 정렬 라이브러리 사용하고
# 데이터 범위가 한정되어 있으며 더 빠르게 동작해야할때는 계수정렬 사용하자

#리스트로 출력
array=[7,5,9,0,3,1,6,2,4,8]

result=sorted(array)
print(result)

#바로 정렬
array=[7,5,9,0,3,1,6,2,4,8]

array.sort()
print(array)

#key를 매개 변수로 받는 경우
#key를 정렬기준으로 하여 정렬

array=[('바나나',2),('사과',5),('당근',3)]

def setting(data):
  return data[1]

result=sorted(array,key=setting)
print(result)
