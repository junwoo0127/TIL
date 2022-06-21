#계수 정렬법을 이용한 정렬
n=int(input())
array=[]
for i in range(n):
  array.append(int(input()))
print(array)
count=[0]*(max(array)+1)
array2=[]
for i in range(len(array)):
  count[array[i]]+=1

for i in range(len(count)):
  for j in range(count[i]):
    array2.append(i)

array2.reverse()
print(array2)

#sort함수를 이용한 정렬
n=int(input())
array=[]
for i in range(n):
  array.append(int(input()))
print(array)
array.sort(reverse=True)
#array=sorted(array,reverse=True)로 표현 가능

for i in array:
  # 한문장에 여백 ' ' 로 출력하려면 end=을 써줘야함
  print(i,end=' ')
