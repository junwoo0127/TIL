class Wow:
    def __init__(self, n):
        self.i = n

    def __lt__(self, other):    # 매직메쏘드__lt__로 < 연산자를 오버로딩함.
        return self.i < other.i, self.i


ten = Wow(10)
nine = Wow(9)
print(ten < nine)   # < 연산자를 호출했지만, 인스턴스의 클래스에서 < 연산자를 오버로딩 했기에,
# ten < nine 이 ten.__lt__(nine)으로 실행됨, 그래서 매직메쏘드로 넘어가서 __lt__(ten, nine) 메쏘드의 반환값이 반환됨.
""" 스페셜 메쏘드, 매직 메쏘드(magic methods):
매직 메쏘드는 이름대로 파이썬에서 클래스의 마법?을 추가하는 특수 메쏘드다.
메쏘드 이름의 앞 뒤에 더블 언더스코어(__)가 붙으며, 이런 형식을 던더 메쏘드(dunder method)라고 부름. 
(이런 메쏘드를 부를때 '던더(메쏘드이름)던더' 로 부르는것이 가장 이상적) 
매직 메쏘드는 기본적으로 어떤 상황의 동작을, 매직 메쏘드안의 코드로 재정의하는, 오버로딩으로 쓰임.

생성자와 소멸자 처럼, 클래스의 생성 초기화에 관련된 매직매쏘드는,
__init__, __del__ 말고도 __new__(cls, [...])가 있다. 
__new__는 사실 __init__보다도 인스턴스 생성시 가장 먼저 호출되는 메쏘드로, 클래스를 인자값으로 받고 
__init__로 보낼 인자값도 받는다. 근데 잘 안쓰는 메쏘드이다.


대표적으로 다양한 연산자를 클래스가 쓰는 경우, 기존 연산자의 동작방식과 다르게 동작하도록 하는, 연산자 오버로딩을
매직메쏘드로 구현할 수 있다. 
연산자 오버로딩이란 +, - 같은 이미 있는 연산자들의 동작을 사용자가 정의한 함수로 동작하게 하는 것인데,
인스턴스에서 쓰이는 연산자의 연산동작을 매직매쏘드로 정의할 수 있는 것이다.


비교 연산자와 매칭되는 매직메쏘드 : 
__eq__(self, other) : == 연산자의 동작 정의. (인스턴스 == 인스턴스 의 동작을 정의)
__ne__(self, other) : != 연산자의 동작 정의.
__lt__(self, other) : < 연산자의 동작 정의.
__gt__(self, other) : > 연산자의 동작 정의.
__le__(self, other) : <= 연산자의 동작 정의.
__ge__(self, other) : >= 연산자의 동작 정의.
__cmp__(self, other) : __cmp__는 비교 매직 메소드의 가장 기본.   # 이해못함, 나중에 추가보충할 것
                    모든 비교 연산자 (<, ==,! = 등)에 대해 실제로 동작을 구현하지만 원하는대로 수행되지 못할 수 있습니다 
                    (예를 들어, 한 인스턴스가 다른 인스턴스와 동일한 지 여부가 하나의 기준에 의해 결정되고 인스턴스가 
                    다른 인스턴스보다 큰지 아닌지가 다른 것으로 결정되는 경우) __cmp__은 self < other이면 음수를 반환하고 
                    self == other이면 0을 반환하고 self > other이면 양수를 반환해야합니다. 
                    일반적으로 한 번에 정의할 필요없이 각 비교를 정의하는 것이 가장 좋지만, __cmp__은 비슷한 기준으로 
                    구현된 모든 비교가 필요할 때 반복을 저장하고 명확성을 향상시키는 좋은 방법이 될 수 있습니다.

단항 연산자와 매칭되는 매직메쏘드 :
__pos__(self) : + 단항(양수부호)연산자의 동작 정의. (+인스턴스 의 동작을 정의)
__neg__(self) : - 단항(음수부호)연산자의 동작 정의.
__abs__(self) : abs() (절댓값구하는 내장)함수의 동작 정의.
__invert__(self) : ~ (not, 논리부정, 반전)연산자의 동작 정의.
__round__(self, n) : round() (반올림하는 내장)함수의 동작 정의. (매개변수 n은 반올림할 소수 자릿수임)
__floor__(self) : math.floor() 함수의 동작 정의. (가장 가까운 정수로 반올림)

산술 (이항)연산자와 매칭되는 매직메쏘드 : 
__add__(self, other) : + (덧셈)연산자의 동작 정의. (인스턴스 + 인스턴스의 동작을 정의)
__sub__(self, other) : - (뺄셈)연산자의 동작 정의.
__mul__(self, other) : * (곱셈)연산자의 동작 정의.
__floordiv__(self, other) : // (몫)연산자의 동작 정의.
__div__(self, other) : / (나눗셈)연산자의 동작 정의.
__truediv__(self, other) : 오차범위 없는 나눗셈연산자의 동작 정의. (__future__ import division 이 유효한 경우에만 동작)
__mod__(self, other) : % (나머지)연산자의 동작 정의.
__divmod__(self, other) : divmod() 함수의 동작 정의 (long 나눗셈을 위한 동작)
__pow__ : ** (제곱, 지수)연산자의 동작 정의.
__lshift__(self, other) : << (왼쪽쉬프트)연산자의 동작 정의.
__rshift__(self, other) : >> (오른쪽쉬프트)연산자의 동작 정의.
__and__(self, other) : & 비트간 논리곱(비트and)연산자의 동작 정의.
__or__(self, other) : | 비트간 논리햡(비트or)연산자의 동작 정의.
__xo__(self, other) : ^ 비트간 배타논리합(비트xor)연산자의 동작 정의.

(이항 연산자는 피연산자(항)이 두개이므로, 매개변수도 self 와 other 두개를 사용하는데,
(인스턴스1) (연산자) (인스턴스2) 라면, 인스턴스1이 self, 인스턴스2가 other 로 전달된다.)

self (연산자) other 가 아니라, other (연산자) self 처럼, 두 피연산자의 위치를 바꿔서 전달할 수도 있는데, 
이런걸 뒤집힌 산술 (이항)연산자라고 하며, 이에 대한 매직메쏘드도 있다 :
__radd__(self, other) : 뒤집힌 덧셈(+)의 동작 정의.
__rsub__(self, other) : 뒤집힌 뺄셈(-)의 동작 정의.
__rmul__(self, other) : 뒤집힌 곱셈(*)의 동작 정의.
__rfloordiv__(self, other) : 뒤집힌 몫 연산자(//)의 동작 정의.
__rdiv__(self, other) : 뒤집힌 나눗셈(/)의 동작 정의.
__rtruediv__(self, other) : 뒤집힌 정확한 나눗셈의 동작 정의. (__future__ import division 이 유효한 경우에만 작동)
__rmod__(self, other) : 뒤집힌 나머지 연산자(%)의 동작 정의.
__rdivmod__(self, other) : divmod(other, self)가 호출될 때 divmod() 내장 함수를 사용하여 long 나눗셈에 대한 동작을 구현합니다.
__rpow__ : 뒤집힌 지수(제곱)연산자(**)의 동작 정의.
__rlshift__(self, other) : 뒤집힌 왼쪽 비트 시프트연산자(<<)의 동작 정의.
__rrshift__(self, other) : 뒤집힌 오른쪽 비트 시프트연산자(>>)의 동작 정의.
__rand__(self, other) : 뒤집힌 비트간 논리곱(비트and)연산자(&)의 동작 정의.
__ror__(self, other) : 뒤집힌 비트간 논리합(비트or)연산자(|)의 동작 정의.
__rxor__(self, other) : 뒤집힌 비트간 배타논리합(비트xor)연산자(^) 동작 정의.
특징으로는 기존 산술연산자의 매직매쏘드 이름앞에 r 이 붙은것 빼곤 동일하다.

산술+대입연산자(복합대입연산자)에 대한 매직메쏘드도 있는데, 기존 산술연산자의 매직매쏘드 이름앞에 i 이 붙은것 빼곤 동일하다.
(ex> __add__ -> __iadd__) (뒤집힌 산술 연산자같이 다 쓸려했으나, 차피 이름이 모두 동일(i + 기존이름)해서 생략)

타입변환 함수에 대한 매직메쏘드도 있다 :
__int__(self) : int로 타입 변환(int())의 동작을 정의. (int(인스턴스)가 호출될 때의 동작을 정의.)
__float__(self) : float로 타입 변환(float())의 동작을 정의.
__complex__(self) : complex로 타입 변환(complex())의 동작을 정의.
__oct__(self) : 8진수로 타입 변환(oct())의 동작을 정의.
__hex__(self) : 16진수로 타입 변환(hex())의 동작을 정의.
__index__(self) : 슬라이스 표현식에서 객체가 사용될 때 타입 변환을 int로 구현합니다.       # 이해못함, 나중에 추가보충할 것
                  슬라이싱에 사용할 수 있는 사용자 지정 숫자 타입을 정의하는 경우, __index__를 정의해야 합니다.
__trunc__(self) : math.trunc(self) 가 호출될 때의 동작을 정의. (__trunc__는 self의 값을 정수형으로 반환)
__coerce__(self, other) : 혼합 모드 산술을 구현하는 메소드.       # 이해못함, 나중에 추가보충할 것
                          타입 변환이 불가능할 경우 __coerce__은 None을 반환해야 합니다. 그렇지 않으면 동일한 타입을 갖도록 조작된
                          self와 other의 쌍 (2-tuple)을 반환해야 합니다.

주로 클래스를 문자열로 표현하기도 하는데, 
클래스의 표현을 반환하는 방식을 사용자가 정의할 수 있는 매직메쏘드도 있다 :
__str__(self) : str(인스턴스)가 호출될 때의 동작을 정의.
__repr__(self) : repr()의 동작을 정의. 
                * 참고 : str()과 repr() 사이의 주요 차이점은 만들어진 대상임. 
                repr()은 주로 기계가 읽을 수 있는 출력(대부분, 유효한 파이썬 코드일 수 있음)을 생성하기 위한 것이며, 
                반면에 str()은 사람이 읽을 수 있도록 만들어짐.
__unicode__(self) : unicode()의 동작을 정의. 
                unicode()는 str()과 비슷하지만 유니코드 문자열을 반환. 
                * 주의 : 클라이언트가 클래스의 인스턴스에서 str()을 호출하고 __unicode__() 만 정의한 경우 작동하지 않음. 
                누군가 유니 코드를 사치스럽게 사용하지 못하는 경우를 대비하여 항상 __str__()을 정의해야함.
__format__(self, formatstr) : 클래스의 인스턴스가 새로운 스타일 문자열 포맷으로 사용될 때의 동작을 정의합니다. 
                              예를 들어 "Hello, {0 : abc}!".format(a)은 a.__format__("abc")를 호출합니다. 
                              특수 서식 옵션을 제공하려는 고유한 숫자 또는 문자열 유형을 정의할 때 유용할 수 있습니다.
__hash__(self) : hash()의 동작을 정의. 
                이 메소드는 정수를 반환해야 하며 그 결과는 사전에서 빠른 키 비교에 사용됨. 
                보통 __eq__도 구현해야 함을 주의. a == b는 hash (a) == hash (b)를 의미한다는 규칙을 따름.
__nonzero__(self) : bool()의 동작을 정의. 
                    인스턴스를 True 또는 False로 간주할지에 따라 True 또는 False를 반환함.
__dir__(self) : dir()의 동작을 정의. 
                이 메소드는 사용자의 속성 목록을 반환함. 
                일반적으로 __dir__을 구현하는 것은 불필요하지만 __getattr__ 또는 __getattribute__ (다음내용 참조)
                를 재정의하거나 그렇지 않으면 동적으로 속성을 생성하는 경우 
                클래스를 대화식으로 사용하는 것이 매우 중요할 수 있음.
__sizeof__(self) : sys.getsizeof()의 동작을 정의. 
                   이 메소드는 객체의 크기를 바이트 단위로 반환해야함. 
                   이것은 일반적으로 C확장으로 구현된 Python 클래스에 더 유용하지만, 이를 인식하는 데 도움이됨.

지금까지는 연산자와 관련된 기본적이고(지루한) 매직 메쏘드였으나,
이제부턴 고급적인 메쏘드에 대한 설명이 이어진다.
"""

"""
파이썬의 클래스는 진정한 캡슐화가 부족하데지만, (getter, setter 로 개인속성을 정의할 방법이 없데서)
파이썬은 메쏘드, 필드에 대한 명시적 변경자 대신 매직메쏘드를 이용해 많은 캡슐화를 수행한다. 

속성접근에 관한 매직 메쏘드는 아래와 같다 :
 __getattr__(self, name) : 사용자가 존재하지 않는 속성에 액세스하려고 시도할 때의 행위를 정의할 수 있음. 
                           이는 일반적인 맞춤법 오류를 포착하고 리다이렉트하고, 더 이상 사용되지 않는 속성 
                           (원하는 경우 해당 속성을 계산하고 반환하도록 선택할 수 있음)의 사용에 대한 경고를 제공하거나, 
                           AttributeError를 손쉽게 전달할 때 유용할 수 있음. 그러나 존재하지 않는 속성에 액세스할 때만 호출되므로 
                           실제 캡슐화 솔루션이 아님.

__setattr__(self, name, value) : __getattr__과 달리 __setattr__은 캡슐화 솔루션임. 
                                이 속성을 사용하면 특성값의 변경 사항에 대한 사용자 지정 규칙을 정의할 수 있으므로 
                                해당 특성의 존재 여부에 관계없이 특성에 할당할 동작을 정의할 수 있음. 
                                (* 아래의 코드참고, __setattr__을 사용하는 방법에 주의를 기울여야함.)

__delattr__(self, name) : 이것은 __setattr__과 완전히 동일하지만 속성을 설정하는 대신 삭제하는 것임. 
                         무한 재귀(__delattr__ 구현시 del self.name을 호출하면 무한 재귀가 발생함)
                         를 방지하기 위해 __setattr__과 동일한 예방 조치를 취해야함.

__getattribute__(self, name) : __getattribute__는 __setattr__ 및 __delattr__와 매우 잘 어울립니다.     # 안풀린 문제 덩어리 
                            그러나, 사용하지 않는 것이 좋음. __getattribute__는 새로운 스타일의 클래스에서만 사용할 수 있습니다.
                             모든 클래스는 최신 버전의 파이썬에서 새로운 스타일이며, 
                             이전 버전에서는 객체를 서브클래싱하여 새로운 스타일을 만들 수 있습니다. 
                             이 메소드는 속성값에 액세스할 때마다 규칙을 정의할 수 있습니다. 
                             이 메소드는 그들의 공범자와 같이 비슷한 무한재귀 문제를 겪습니다. 
                             (이번에는 베이스 클래스의 __getattribute__ 메소드를 호출하여 이것을 방지합니다). 
                             또한 __getattr__에 대한 필요성을 제거합니다. 
                             __getattribute__가 구현되면 명시적으로 호출되거나 AttributeError가 발생하는 경우에만 호출됩니다. 
                             이 메소드를 사용할 수는 있지만 (결국 사용자의 선택사항입니다.) 
                             사용 사례가 적기 때문에 권장하지 않습니다. 
                             (값을 할당하는 것보다 값을 획득할 때 특별한 조작이 필요한 상황은 훨씬 더 드뭅니다. 
                             (역자: 보통 값을 set할 때보다 get할 때에는 별다른 코드가 필요없다는 뜻인 것 같아요) 
                             왜냐하면 버그없이 구현하는 것은 정말로 어렵기 때문입니다.
"""


class Temp:
    def __setattr__(self, name, value):
        self.name = value
        # 속성이 할당될 때마다 __setattr__()이 호출되는데, 매직메쏘드 안에서 속성을 할당했으므로, 자기자신이 다시 호출됨.
        # 어 이거 완죤 재귀함수아니야? 맞음. 이 재귀는 영원히 충돌.

    def __delattr__(self, name):
        del self.name
        # 얘도 무한재귀, 속성을 삭제하면 호출되는 함수에서 속성을 삭제해버렸으니...


"""
파이썬 클래스가 파이썬의 내장 시퀀스(dict, tuple, list, str)처럼
동작하는 방밥에도 다양한 매직 메쏘드가 있다 :
__len__(self) : 컨테이너의 길이를 반환함. 
                불변 및 가변 컨테이너에 대한 프로토콜의 일부.
__getitem__(self, key) : self[key] 표기법을 사용하여 항목에 액세스할 때의 동작을 정의. 
                        이것은 가변 컨테이너 프로토콜과 불변 컨테이너 프로토콜의 일부이기도 함. 
                        * 이때에 적절한 예외를 발생시켜야힘. 
                        키의 유형이 잘못된 경우 TypeError를, 키에 해당하는 값이 없는 경우 KeyError를 지정.

__setitem__(self, key, value) : self[nkey] = value 표기법을 사용하여 항목이 할당된 경우의 동작을 정의. 
                                이것은 가변 컨테이너 프로토콜의 일부입니다.    
                                (KeyError와 TypeError를 적절히 발생시켜야 함.)

__delitem__(self, key) : 항목이 삭제 된 경우의 동작을 정의(ex> del self[key]). 
                        이것은 가변 컨테이너 프로토콜의 일부일뿐입니다. 
                        (유효하지 않은 키가 사용되면 적절한 예외를 발생시켜야함.)

__iter__(self) : 컨테이너에 대한 반복자를 반환해야함. 
                반복자는 많은 경우(특히 iter() 내장 함수와 for x in container: 형태를 사용할 경우등등)에서 반환됨.
                반복자는 자체가 객체이며 자체를 반환하는 __iter__ 메서드를 정의해야 함.

__reversed__(self) : reversed() 내장 함수의 동작을 정의. 
                    시퀀스의 반대 버전을 반환해야함. 
                    (시퀀스 클래스가 list 또는 tuple과 같이 정렬된 경우에만 이를 구현하길 바람.)

__contains__(self, item) : __contains__는 in과 not in(맴버 연산자)에 대한 동작을 정의. 
                        이 부분이 시퀀스 프로토콜의 일부가 아닌 이유를 물으신다면, 
                        __contains__가 정의되어 있지 않을 때, 
                        파이썬은 그냥 시퀀스를 반복하며 찾고 있는 항목을 발견할 경우 True를 반환하기 때문입니다.

__missing__(self, key) : __missing__은 dict의 서브 클래스에서 사용됨. 
                        사전에 존재하지 않는 키에 액세스 할 때마다의 동작을 정의. 
                        (ex> 딕셔러니 d가 있고 "george"가 dict에서 키가 아닌데 
                        d["george"]라고 말한 경우, d.__missing__("george")가 호출.)


위같은 매직 메쏘드로 독보적인 나만의 시퀀스 객체를 구현할 수 있다.
그리고 이정도 매직 메소드도 많은데 와.... 또 있다. 


이번엔 isinstance(), issubclass() 함수처럼 인스턴스가 클래스에 속하는지, 자식클래스가 부모클래스에 속하는지를 참, 거짓으로 반환하는
함수(리플렉션이 동작하는 방식)마저도 매직 메쏘드로 재정의 할수 있다 :

__instancecheck__(self, instance) : 인스턴스가 정의한 클래스의 인스턴스인지 확인할 때의 동작을 정의. 
                                    (예 : isinstance(instance, class)).
__subclasscheck__(self, subclass) : 클래스가 정의한 클래스의 하위 클래스인지 확인할 때의 동작을 정의. 
                                    (예 : issubclass(subclass, class)).


클래스의 인스턴스를 함수로 호출 할수 있는데, 함수이름() 형식처럼, 인스턴스이름() 형식도 가능하다는 것이다.
이럴때 인스턴스이름() 상황을 정의할 수 있는 매직메쏘드도 있다 :
__call__(self, [args ...]) : 클래스의 인스턴스를 함수로 호출할 때의 동작을 정의.. ( x() == x.__call__() )
                            __call__은 가변 인수(argument)를 취함. 

상태를 변경해기 위해 인스턴스를 호출하는 방법으로 활용하는 것이 직관적이고 우아한 방법이라고 한다...
(데코레이터를 클래스로 구현하는 경우에 __call__이 요긴히 사용된다. 자세한 것은 08-3 참고 )


파이썬에서 with as 문이 2.5버전 부터 추가됬는데, 이런 컨텍스트 매니저(관리자)는 with as 문이 있기 전부터 사실 있었다.
(파일과 with as 문에 대해서는 2폴더의 18-1 참고) 
이런 컨텍스트 매니저도 매직 메쏘드를 이용한 클래스로 구현할 수 있다.
__enter__(self) : with 문에 의해 생성된 블록의 시작 부분에서 컨텍스트 관리자가 수행하는 동작을 정의. 
                  __enter__의 반환값은 with 문의 대상 또는 as 다음의 이름에 바인딩됨.

__exit__(self, exception_type, exception_value, traceback) : 블록이 실행(또는 종료) 된 후에 컨텍스트 관리자의 동작을 정의. 
                예외를 처리하거나, 클린업을 실행하거나 또는 블록의 실행 직후에 항상 수행되는 작업을 진행할 수 있음. 
                블록이 성공적으로 실행되면 exception_type, exception_value 및 traceback은 None이 됨. 
                그렇지 않으면 예외를 처리하도록 선택하거나 사용자가 처리하도록 선택할 수 있음. 
                만약 별도로 예외로 처리하고 싶다면, __exit__이 모두 진술되고 완료된 후에 True를 반환하는지 확인. 
                컨텍스트 관리자가 예외를 처리하지 못하게 하려면 그냥 그대로 두면 됨.
                

디스크립터(Descriptor).
이부분에 대해서는 한번 제대로 정리할 필요가 있을 것 같다. (찾아보니까 이것도 이거대로 중요한것 같음)
java, c++ 에서는 클래스의 속성의 접근제어가 있는데, 파이썬은 사실 없다. (비공개 속성, 메쏘드도 가능하긴 하지만,(3-2 참고) 접근을 제어하기엔 애매하다.)
대신에 디스크립터를 이용해서 접근을 제어할 수 있다.
.(점)을 사용해서 객체의 속성(맴버)를 접근할 때, 인스턴스 속성, 클래스 속성 순으로 속성을 찾았는데, (4-1 참고)
이때 디스크립터를 만들었으면, 맴버를 바로 리턴하지 않고, 디스크립터 메소드(__get__, __set__, __delete__)를 호출한다.

__get__(self, instance, owner) : 디스크립터의 값이 회수될 때(속성을 접근할 때) 동작을 정의. 
                                instance는 해당하는 인스턴스이고. owner는 해당하는 클래스 자체다.

__set__(self, instance, value) : 디스크립터의 값이 변경될 때(속성을 변경할 때) 동작을 정의. 
                                instance는 해당하는 클래스의 인스턴스이고 value는 디스크립터에 설정하는 (속성을 변경하는) 값이다.

__delete__(self, instance) : 디스크립터의 값이 삭제될 때(속성을 삭제할 때) 동작을 정의. 
                            instance는 해당 객체의 인스턴스다.


복사.
2폴더의 #3 파일을 참고하면, 복사도 단순복사, 얕은복사, 깊은복사라는 3가지 형태가 있다.
여기서 대입으로 이뤄지는 단순복사는 빼고 봤을때, 객체의 얕은 복사, 깊은 복사도 매직 메쏘드로 재정의 할 수 있다.

__copy__(self) : 클래스의 인스턴스에 대해 copy.copy()에 대한 동작을 정의. 

__deepcopy__(self, memodict = {}) : 클래스의 인스턴스에 대해 copy.deepcopy()에 대한 동작을 정의. 
                                    개별 속성을 깊은 복사하려면, memdeict를 첫 번째 인수로 사용하여 해당 속성에 대해 
                                    copy.deepcopy()를 호출하면 된다.


피클링.
2폴더의 18-2 파일을 참고하면, 피클링과 언피클링을 배웠었다.
복습하자면, 객체를 파일에 저장하는 것을 피클링(말그대로 피클을 쟁여놓듯이 파일에 객체를 쟁여놈)
거꾸로 파일에서 저장한 객체를 가져오는 것을 언피클링이였다.
이것들을 하는 과정에서도 매직 메쏘드를 사용해서 동작을 재정의 할 수 있다.

__getinitargs__(self) : 클래스가 언피클되었을 때 __init__을 호출하고 싶다면, __getinitargs__를 정의. 
                        __getinitargs__는 __init__에 전달할 인수의 튜플을 반환해야 한다. (이 메소드는 구식 클래스에서만 작동)

__getnewargs__(self) : 새로운 스타일의 클래스의 경우, 언피클링을 할 때 __new__에 전달되는 인수에 영향을 줄 수 있다. 
                        이 메소드는 __new__로 전달되는 인수 튜플을 반환해야 한다.

__getstate__(self) : 객체의 __dict__ 속성이 저장되는 대신 객체가 피클될 때 저장할 수 있는 사용자 정의 상태를 반환할 수 있음. 
                    그 상태는 객체가 언피클 되었을 때 __setstate__에 의해 사용됩니다.

__setstate__(self, state) : 객체가 언피클 되었을 때 __setstate__가 정의 되었다면, 객체의 상태는 객체의 __dict__에 직접 적용되지 않고 전달됨. 
                            이 메쏘드는 __getstate__와 함께 사용되며, 둘 다 정의되면 객체의 피클된 상태를 내가 원하는대로 나타낼 수 있다.

__reduce__(self) : 확장 타입(즉, 파이썬의 C API를 사용하여 구현된 타입)을 정의 할 때 파이썬에서 피클링하려는 경우 피클링 방법을 지정해야함. 
                    __reduce__()는 정의된 객체가 피클될 때 호출되며. 파이썬이 찾고 피클하는 전역 이름을 나타내는 문자열 또는 튜플을 반환할 수 있다. 
                    튜플은 아래에서 말하는 2 ~ 5 개의 요소를 포함함. 
                    객체를 다시 생성하기 위해 호출되는 호출 가능 객체, 호출 가능 객체에 대한 인수의 튜플, 
                    __setstate__에 전달될 상태 (이건 선택 사항), 피클링될 리스트 항목을 생성하는 반복자(=이터레이터)(이것도 선택 사항), 
                    피클링할 딕셔너리 항목을 생성하는 반복자 (요것도 선택 사항)가 있다.

__reduce_ex__(self) : __reduce_ex__은 호환성을 위해 존재한다. 정의된 경우, __reduce_ex__는 피클링시에 __reduce__를 통해 호출된다. 
                      __reduce__는 __reduce_ex__을 지원하지 않는 이전 버전의 피클링 API에 대해서도 정의할 수 있다.
"""

# 파이썬에서 스페셜 매쏘드(매직 매쏘드)는 전반적인 아키텍처를 담는다라고 할정도로 사실 중요한 개념이라한다.
# 이부분은 심화부분이고, 그만큼 어려운 부분이긴 하지만, 좋은 자료들을 찾았기에, 모두 정리해볼 예정이다.
# # # # https://ziwon.github.io/post/python_magic_methods/

# https://kwonkyo.tistory.com/234
# http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-oop-part-6-%EB%A7%A4%EC%A7%81-%EB%A9%94%EC%86%8C%EB%93%9C-magic-method/
# https://niceman.tistory.com/196
