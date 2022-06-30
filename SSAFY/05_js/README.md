# 1 - JS 기본 문법
> 참고 : https://poiemaweb.com/js-syntax-basics

## 1. 변수 (Variable)

값(value)을 저장(할당)하고 참조하는 저장공간이 변수다.

일회용이 아닌, 유지(캐싱)가 필요한 값은 변수에 담아쓴다.  
변수 이름으로 값을 담아쓰면 값의 의미를 변수의 이름으로 알수 있어서, 코드의 가독성이 좋아진다.
 
변수의 값은 메모리 주소에 저장되는데, 이것을 접근하기 위해 사람이 아는 언어로 지정한 식별자(identifier)이다.   
그래서 사람은 식별자로 변수를 접근해서, 변수의 값이 있는 메모리 주소를 접근할 수 있는 것이다. 

```js
var x   // 변수를 선언
x= 10   // 변수에 정수(10)를 할당
```

변수를 선언할 때 ```var``` 키워드를 변수이름 앞에 사용한다.  
그리고 할당 연산자 ```=```으로, 변수에 값을 할당한다.


## 2. 값 (Value)

단어|뜻
:---:|:---:
자료형(데이터 타입, Data Type)|프로그래밍 언어에서 사용할 수 있는 값의 종류
변수(Variable)|값이 저장된 메모리 공간의 주소를 가리키는 식별자(identifier)
리터럴(literal)|소스코드 안에서 직접 만들어 낸 상수 값 자체를 말하며 값을 구성하는 최소 단위

**값,** 프로그램으로 조작가능한 대상이라 표현하며, 간편한 방법으로 리터럴 표기법(literal notation)을 사용한다.

리터럴이란 단어가 생소한데, 아래와 같은 방법으로 표현하는 것이다.

```js
// 숫자 리터럴
10.50
1001

// 문자열 리터럴
'Hello'
"World"

// 불리언 리터럴
true
false

// null 리터럴
null

// undefined 리터럴
undefined

// 객체 리터럴
{ name: 'Lee', gender: 'male' }

// 배열 리터럴
[ 1, 2, 3 ]

// 정규표현식 리터럴
/ab+c/

// 함수 리터럴
function() {}
```

위에서 봤듯이, 값들도 각각의 자료형(데이터 타입)이 있는데, js의 모든 값들은 7가지 자료형 중 하나에 속한다.

원시 타입 (primitive data type)
- number
- string
- boolean
- null
- undefined
- symbol (ES6에서 추가됨)
객체 타입 (Object data type)
- object

참고로 js는 변수를 선언할 때 위같은 자료형을 지정하지 않고, 알아서 변수에 할당되는 값의 자료형(동적)으로 변수의 자료형이 정해진다.  
(이것을 **동적 타이핑** 이라 한덴다.)


## 3. 연산자 (Operator)

```js
// 산술 연산자
var area = 5 * 4; // 20

// 문자열 연결 연산자
var str = 'My name is ' + 'Lee'; // "My name is Lee"

// 할당 연산자
var color = 'red'; // "red"

// 비교 연산자
var foo = 3 > 5; // false

// 논리 연산자
var bar = (5 > 3) && (2 < 4);  // true

// 타입 연산자
var type = typeof 'Hi'; // "string"

// 인스턴스 생성 연산자
var today = new Date(); // Sat Dec 01 2018 00:57:19 GMT+0900 (한국 표준시)
```
연산자로 연산되는 대상을 피연산자라고 하는데,  
js에서 피연산자의 타입은 무조건 같을 필요가 없이, 암묵적인 타입 강제 변환으로 연산을 수행한다.

```js
var wow = 1 + '1'   // '11'
var lol = 1 * '10'  // 10
```


# 4. 키워드 (Keyword)

```js
// 변수의 선언 : var
var x = 5 + 6;

// 함수의 선언 : function
function foo (arg) {
  // 함수 종료 및 값의 반환 : return
  return ++arg;
}

var i = 0;
// 반복문 : while
while (1) {
  // 조건문 : if
  if (i > 5) {
    // 반복문 탈출 : break 
    break;
  }
  console.log(i);
  i++;
}
```
위같이 수행할 동작이 정해져있는 단어들을 키워드라 한다. 예약어라고도 하는 것 같다.


# 5. 주석 (Comment)

작성된 코드의 의미를 설명하려고, 실제 코드와는 상관없는 텍스트를 덧붙이는 것이 주석이다. (해석기(parser)도 주석은 무시해서 실행시키지 않는다.)

```js
// 한줄주석

/*
여러줄
주석
*/
```
적절히 코드를 설명하는 용도로만 쓰자. 주석없이 읽을 수 있는 코드를 지향하자.


# 6. 문 (Statement)

프로그램(스크립트)은 컴퓨터(호스팅 환경에 따라 자세하게는 다름)에 의해 단계별로 수행될 명령들의 집합이다.

각각의 명령을 **문(statement)**이라 하며 문이 실행되면 무슨 일인가가 일어나게 된다.

문은 리터럴, 연산자(Operator), 표현식(Expression), 키워드(Keyword) 등으로 구성되며 세미콜론(;)으로 끝나야 한다.   
세미콜론을 생략해도, 인터프리터는 세미콜론 자동 삽입(ASI, automatic semicolon insertion)으로 세미콜론을 자동으로 붙여주기에 안붙여도 돌아가기는 한다.

이 문은 **코드 블록(code block) {}** 으로 그룹으로 묶어줄 수 있다.


# 7. 표현식 (Expression)

표현식은 하나의 값으로 평가(Evaluation)된다고 한다.   
그니까 ```값(리터럴), 변수, 배열의 요소, 함수 호출, 메서드 호출, 피연산자와 연산자 조합```같은 것은 표현식으로, 이 표현식의 결과는 하나의 값이 되기에, 다른 표현식의 일부로 쓰여서 복잡한 표현식을 짤 수도 있다.

```js
// 표현식
5
5 * 10

```

그럼 문과 표현식은 뭔 차이냐면,  
문(statement)은 마침표로 끝나는 하나의 완성 문장이고, 표현식은 문을 구성하는 요소다. (표현식 자체로 문이 될 수도 있다.)   
그리고 표현식은 값에 대한 것 이외에는 하는 게 없지만, 문은 선언식으로 변수, 함수, 제어문 등을 생성해서 프로그램의 흐름을 제어할 수 있다.

```js
// 선언문(Declaration statement)
var x = 5 * 10; // 표현식 x = 5 * 10를 포함하는 문이다.
// 할당문(Assignment statement)
x = 100; // 이 자체가 표현식이지만 완전한 문이기도 하다.
```

# 8. 함수 (Function)

한 작업을 수행하기 위해 필요한 문들의 집합을 정의한 코드 블록({})으로, **함수명, 매개변수**를 가질 수 있고, 함수를 원하는 때 호출할 수 있다.

```js
// 함수의 정의(함수 선언문)
function square(number) {
  return number * number;
}

// 함수의 호출
square(3); // 9
```
이때 호출은 여러번 가능해서, 반복되는 코드를 재사용할 수 있다.


## 9. 객체 (Object)

js는 객체기반 스크립트 언어로, js의 대부분은 객체로 이뤄진다. (아까 자료형의 원시타입을 제외한 나머지는 모두(함수, 배열, 정규표현식 등이) 객체다.)

js 객체는 키와 값으로 구성된 **프로퍼티(property)** 집합으로, 이 프로퍼티의 값에 js의 사용가능한 모든 값을 사용할 수 있다.  
**js의 함수는 일급 객체**여서 값으로 취급할 수 있는데, 그래서 프로퍼티의 값으로 함수가 들어갈 수 있으며, 그래서 프로퍼티의 값으로 들어가는 함수를, 일반함수와 구분하려고 메서드라 한다.

```js
var obj = {
    name: '횻홍홍',
    hi: function(){
        console.log(name)
    }
}

console.log(typeof obj) // object
console.log(obj)    // (obj 객체의 구조) { name: '횻홍홍', hi: [Function: hi]}
obj.hi()    // 횻홍홍
```
객체는 프로퍼티 + 메서드 로 구성된 집합이다.  
js의 객체는 객체지향 상속을 구현하려고 **프로토타입** 이란, 객체의 프로퍼티, 메서드를 상속받을 수 있다. (이건 js만의 중요 개념이다)


# 11. 배열 (Array)

```js
var arr = [1, 2, 3]
console.log(arr[0])     // 1
```

1개의 변수에 여러 값을 순차적으로 저장할 때 배열을 사용한다.  
js에선 배열도 객체여서, 배열을 쓸 때 유용한 내장 메서드를 사용할 수 있다.