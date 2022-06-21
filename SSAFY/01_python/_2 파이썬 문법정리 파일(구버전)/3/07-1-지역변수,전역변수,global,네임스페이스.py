x = 10  # 여기서 x는 전역변수(파이썬 스크립트(파일) 어디서든지 접근할 수 있음)


def func():
    y = 20  # 여기서 y는 지역변수(변수를 선언한 함수에서만 접근할 수 있고, 함수 바깥에서는 접근할 수 없음)
    print(x, y)


func()
print(x)
""" 지역변수(local variable), 전역변수(global variable):
전역변수는 일반적으로 파이썬 스크립트에서 변수를 만들었을 때 해당되며, 
함수 안에서도 함수 바깥에서도 어디든지 사용할 수 있음. (물론 변수 선언 전에선 사용할 수 없음)

이런 전역변수에 접근할 수 있는 범위를 전역 범위(global scope)라고 함.


지역변수는 함수 안에서 변수를 만들었을 때 해당되며, 
만든 지역변수는, 변수를 만든 함수의 지역변수로, 그 함수에서만 접근 할 수 있고, 함수 바깥에선 사용할 수 없음.

마찬가지로 지역변수에 접근할 수 있는 범위를 지역 범위(local scope)라고 함.


참고로 지역변수와 전역변수 둘다 같은 이름일 수도 있는데, 그럴경우, 해당함수에선 지역변수가 우선임.
함수 안에선 전역변수를 읽고 참조하기만 할 뿐 전역변수의 값을 변경할 수 없음.
함수 안에서 전역변수를 변경하려면 global 키워드를 사용함.
"""
n = 10


def n_func():
    global n
    n += 10


n_func()
print(n)
"""
함수 안에서 
global 전역변수
를 붙이면 해당 전역변수를 함수안에서 사용할 수 있음. 
"""
# 참고로 이럴때 함수안에서 사용하는 전역변수는 프리변수(free variable)이라고 함.
# 프리변수는 어떤 코드블럭 안에서 사용은 됬는데, 그 코드블럭 안에서 정의되지는 않은 변수를 말함.


def m_func():
    global m
    m = 10


m_func()
print(m)
"""
해당 전역변수가 없다면, global 에서 붙인 변수이름을 가지고 새로운 전역변수를 선언함. 
(대신에 함수를 호출해야만 해당 전역변수가 선언됨.)
"""
print(locals())


def f():
    f1, f2 = 1, 2
    print(locals())


f()
""" 네임스페이스(namespace):
파이썬에서 변수는 네임스페이스(이름을 모아놓은 공간)에 저장되며, locals 함수를 이용해서 현재 네임스페이스를 반환할 수 있음.
함수 바깥 뿐만아니라, 함수안에서도 locals 함수를 사용할 수 있으며, 그럴시 지역범위에서의 네임스페이스를 반환함.
(지역 네임스페이스를 반환함) 
"""