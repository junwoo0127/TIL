'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

numbers = int(input('숫자를 입력하세요: '))     # int를 씌워줘야 숫자로 인식

for i in range(1,numbers+1):
    print(i)