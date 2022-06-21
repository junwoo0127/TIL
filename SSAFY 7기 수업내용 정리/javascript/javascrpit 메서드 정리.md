## Math

- `Math.min(a, b)`: a, b 중 더 작은 값 리턴
- `Math.max(a, b)`: a, b 중 더 큰 값 리턴
- `Math.ceil(a)`: 올림함수 ex) Math.ceil(3.1)=4
- `Math.floor(a)`: 내림함수 ex) Math.floor(3.7)=3
- `Math.round(a)`: 반올림(반내림)함수 ex) Math.round(3.1)=3 / Math.round(3.7)=4
- `Math.sqrt(a)`: 제곱근 함수 ex) Math.sqrt(121)=11 (11^2=121)

## String

- `String.replace(/A/g, '#')`: s 문자열에서 "A"( /A/ )를 모두( g(global) ) 찾아, "#"( '#' )으로 바꿔라 (https://regexr.com/)
- `String.split('R')`: s 문자열에서 구분자 'R'을 기준으로 문자열 str이 나누어진다. 그리고 배열로 만든다.
  만약, 아래 문자열을 s라고 했을 때 s.split('R').length=6이다. 즉 R구분자로 인해 6개의 덩어리가 생긴다. 구분자 좌우로 덩어리가 생긴다고 생각하자!
  결국, s.split('R').length===구분자('R')의 갯수+1이다. 이를 기억하고 문제에 활용할 수 있다.
- `String.toUpperCase()`: string 문자열을 대문자로 변환
- `String.toLowerCase()`: string 문자열을 소문자로 변환
- `String.charCodeAt()`: string의 아스키코드를 리턴한다.
  대문자의 아스키코드: 65~90(26개)
  소문자의 아스키코드: 97~122(26개)
  이다. 이들사이의 차이는 32이다. 만약, 대문자->소문자로 변환하고 싶다면 +32를하면 된다. 반대로 소문자->대문자로 변환하고 싶다면 -32를 하면 된다.
  만약, `String.charCodeAt(i)`와같이 쓰면, string의 i번째 인덱스의 아스키를 리턴한다.
- `String.fromCharCode(num-32)`: (num-32) 아스키코드를 문자(String)으로 변환한다. 즉, num이 소문자일 때 num-32를 통해 대문자로 변환할 수 있다.
- `String.slice(i, j)`: i번째 인덱스부터 j번째 인덱스 '전'까지(substring과 같음)
  `String.slice(0, -1)`은 가장 마지막 문자 제거
- `String.substring(i, j)`: i번째 인덱스부터 j번째 인덱스 '전'까지(slice와 같음)
  ex) s="STUDY"일 때, s.substring(2, 3)은 2번째 인덱스부터 3번째 인덱스 전까지이기 때문에 2번째 인덱스만 채택해서 "u"이다.
  즉, s.substring(i, i+1)은 i번째 인덱스 요소만 선택한다.
  배열에서는 slice를 사용한다.(string에서도 slice 사용)
- `String.substr(x,y)`: string문자열에서 x번째 인덱스부터 y개 뽑아내는 함수이다. `String.substring(i, j)`와 헷갈리지 않도록 주의!
- `String.indexOf('k')=0` : (string="ksekkset"이라고 가정)'k'문자가 '처음'으로 발견되는 인덱스를 리턴한다.
  `String.indexOf('k', 1)=3`: 1번째 인덱스이후 'k'문자가 있는 인덱스
  `String.indexOf(문자)=-1`이면, 문자를 문자열에서 발견하지 못한 경우이다. 즉 문자가 문자열에 없을 때 -1을 리턴한다.
- `String.trim()`: string 문자열의 양끝 공백 제거
- `Sting.split('').reverse().join('')`: string을 ''으로 나누어 배열로 만들고, 그 배열을 뒤집어서, ''로 합쳐서 문자열로 다시 만든다. (3-1, 3-2예제)
- `String.toLowerCase().replace(/[^a-z]/g, '')`: string 문자열을 소문자로 바꾸고, 그 문자열에서 a-z가 아닌 모든 것들을 ''로 대체하라
- `parseInt(String, radix)`: String문자열을 radix(2-36)진법으로 변환한다. 만약 radix가 없을 때, String이 0으로 시작한다면 radix는 8진이거나 10진이다.

## Array

- `Array.splice(i, 1)`: 배열 arr에서 i번째 인덱스 요소를 1개 삭제
  splice()의 반환값은 제거한 요소를 담은 배열이다.
  또한, Array.splice(i, 1, replace)는 i번째 인덱스요소부터 한개를 replace로 대체한다는 뜻이다. (mdn 참고)
  `realReserve.splice(realReserve.indexOf(x+1), 1);`만 해도 원하는 요소가 삭제된다. 만약, `const a=realReserve.splice(realReserve.indexOf(x+1), 1);`와 같이 한다면 삭제된 요소가 a에 담겨서 반환된다.
- `Array.filter(콜백함수)`: 주어진 함수의 테스트를 통과하는 모든 요소를 필터링해서 새로운 배열로 반환합니다.
  https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/filter
- `Array.forEach(콜백함수)`: 주어진 함수를 array의 각 요소에게 실행 및 적용한다
  https://www.w3schools.com/jsref/jsref_foreach.asp
- `Array.map(콜백함수)`: 주어진 함수를 array의 각 요소에게 실행하여, 함수의 결과로 새로운 배열을 만든다
  https://www.w3schools.com/jsref/jsref_map.asp
- `Array.reduce(콜백함수)`:
  arr.reduce((a, b)=>a+b, 0)): 여기서 a는 누적값이며, 초깃값은 0이다(2번째 인자). 여기서 b의 값을 바꿔가며 a에 계속 누적하여 더한다. b는 배열 arr의 요소를 하나씩 돈다고 생각하면 된다.
  https://www.w3schools.com/jsref/jsref_reduce.asp
- `Array.find(콜백함수)`: array에서 콜백함수 조건을 만족하는 첫번째 요소를 리턴한다. 만약 없으면 undefined를 리턴한다.
  https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/find
- `Array.some(콜백함수)`:
  some() 메서드는 배열 안의 어떤 요소라도 주어진 판별 함수를 통과하는지 테스트한다. true, false로 결과를 반환한다. (프로그래머스: 기능개발)
  https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/some
- `Array.every(콜백함수)`: array의 모든 요소가 콜백함수의 조건을 통과하는지 테스트한다. 모든요소가 true이면 true를 반환하고, 그렇지 않으면 false를 리턴한다.
- `Array.reverse()`: 배열을 뒤집음
  만약, reverse()메소드 사용하지 않고 뒤집는다면, 다음코드와 같음

```null
  while(x){
	let t=x%10; //1의 자리
	res=res*10+t; 
	x=parseInt(x/10); //Math.floor도 됨. 여기서 parseInt는 몫만 나타내기 위해 사용(몫만 나타내려면 Math.floor, parseInt 사용가능)
}
```

- `Array.join('')`: ''을 사이사이에 넣어서 string으로 합친다
- `Array.sort()`:
  - array.sort()는 기본적으로 문자 정렬이다. 즉, 콜백함수 없이 array.sort()와같이 작성하면 문자열 오름차순 정렬이다. 만약 문자열 내림차순 정렬을 하고싶다면 array.sort().reverse()를 하면 된다.
  - 만약, 숫자정렬을 하고싶다면 콜백함수를 넣으면 된다.
    array.sort((a,b)=>a-b)는 배열을 오름차순, sort((a, b)=> b-a)는 배열을 내림차순 정렬한다. 만약, 그냥 sort()를 하면 문자로 정렬하기 때문에, 잘못된 정렬이 나온다.(a,b,c의 순서/1, 20,3의 순서) 따라서, 숫자 정렬을 하고싶을 때는 정렬의 기준이 되는 콜백함수를 반드시 넣어주자!(양수: 순서바꿈, 음수: 순서바꾸지 않음)
- `Array.push(x)`: 배열에 요소 x를 추가한다.
  `Array.pop()`: 배열의 마지막 요소를 꺼낸다(가장 마지막에 들어간 요소)
- `Array.unshift(x)`: 배열 가장 앞에 x를 집어넣음
- `Array(n).fill(x)`: 길이가 n이고 x로 채운 배열 생성
- `Array.from({length:n}, ()=>0)`: 길이가 n이고 value가 0인 유사배열 생성
- `Array.from({length:n}, (v, i)=>i+1)`: 길이가 n이고 value의 값을 i+1으로 생성(1, 2, 3, 4...)
  `Array.from(Array(35), ()=>Array(35).fill(0))`: 35행 35열 유사배열 생성
  `Array.from(Array(n), ()=>Array())`: n행 유사배열 만듦(열은 미정)
- `let sortArr=arr.slice()` : 깊은 복사(sortArr와 arr는 독립적으로 움직임)
  `let sortArr=arr.slice(i, j)`: 또한, i번째 인덱스에서 j-1번째 인덱스까지를 깊은 복사 하는 역할도 한다. (i~j-1까지의 요소만 리턴)

## stack

- `let stack=[]`으로 스택을 생성했다고 가정하자.
  `stack.push(x)`: 배열에 요소 x를 추가한다.
  `stack.pop()`: 배열의 마지막 요소를 꺼낸다(가장 마지막에 들어간 요소)

## queue

- `let queue=[]`으로 큐를 생성했다고 가정하자.
  `queue.shift()`: 큐 배열 가장 앞에 있는 원소 꺼냄
  `queue.push(x)`: 큐 배열에 요소 x추가
  `it(queue.includes(x))`: 큐에 x가 있는지 확인. true이면 큐에 x가 있는 것이다.

## 기타

#### 판단

- `isNaN(x)`: is Not a Number x? 즉, x가 숫자가 아니니?(true: 숫자X / false: 숫자O)
  `!isNaN(x)`: x가 숫자이니?
- `Number.isInteger(x)`: x가 정수인지 확인한다(정수라면 true 리턴)

#### 자료형 변경

- `Number(x)`: x를 숫자 자료형으로 변경 (parseInt로도 가능)
- `x.toString()`: x를 문자 자료형으로 변경

#### 소수점 삭제

- `parseInt(x), Math.floor(x)`: x의 소수점을 삭제한다. 즉, 몫만 나타내야할 때 반드시 사용해준다.

## 객체

- `Set()객체`: 중복 제거 객체(let x=new Set()과 같이 객체를 생성한다)
  `x.add()`: Set()객체 x에 자료를 추가하는 메소드
  `x.size()`: Set()객체의 length
- `Array.from(x)`: x 객체를 배열로 만듦
- `Map()객체`: 맵 객체를 생성한다. 맵 객체는 **key:value**의 쌍으로 이루어져있다.
  (let sH=new Map()과 같이 객체 생성한다)
  `sH.has(x)`: key=x가 있는지 확인한다. key=x가 있으면 true, 없으면 false 리턴한다.
  `sH.set(x, 1)`: key=x의 value를 1로 세팅한다.
  `sH.get(x)`: key=x인 value를 가져온다.
  `sH.delete(x)`: key=x를 삭제한다
  `sH.size`: sH의 사이즈



## 주요 메서드 정리(array 위주)

### 1. concat() - 배열 합치기

```
array.concat([value1[, value2[, ...[, valueN]]]])
```

- 인자로 주어진 배열이나 값들을 기존 배열에 합쳐서 새 배열을 반환한다.
- 기존 배열이나 값을 변경시키지 않는다.

```js
let arr1 = [1, 2, 3, 4];
let arr2 = [5, 6];
let arr3 = [7, 8];

console.log(arr1.concat(arr2)); // [1, 2, 3, 4, 5, 6];
console.log(arr1.concat(arr2, arr3)); // [1, 2, 3, 4, 5, 6, 7, 8];
console.log(arr1); // [1, 2, 3, 4]
console.log(arr2); // [5, 6]
console.log(arr3); // [7, 8]
```



### 2. push, unshift - 배열에 항목 추가하기

- `push()` : 배열 끝에 항목 추가
- `unshift()` : 배열 앞에 항목 추가
- 반환 값 : 호출한 배열의 새로운 length 속성
- 기존 배열을 변경시킨다.

```js
let arr = ['가', '나', '다'];

console.log(arr.push('라')); // 4
console.log(arr); // ['가', '나', '다', '라']

console.log(arr.unshift('마')); // 5
console.log(arr); // ['마', '가', '나', '다', '라']
```



### 3. pop, shift - 배열에서 항목 제거하기

- `pop()` : 배열 끝에 항목 제거
- `shift()` : 배열 앞에 항목 제거
- 반환 값 : 제거한 항목
- 기존 배열을 변경시킨다.

```js
let arr = ['가', '나', '다'];

console.log(arr.pop()); // 다
console.log(arr); // ['가', '나']

console.log(arr.shift()); // 가
console.log(arr); // ['가']
```



### 4. splice() - 배열 요소를 삭제 또는 교체하거나 추가하기

```
array.splice(start[, deleteCount[, item1[, item2[, ...]]]])
```

- `start` : 배열의 변경을 시작할 인덱스
- `deleteCount` : 배열에서 삭제할 요소의 수
- `item1, item2, ...` : 배열에 추가할 요소 (아무 요소도 지정하지 않으면 배열에 추가하지 않고 삭제만 한다)
- 반환 값 : 제거한 요소를 담은 배열
- 기존 배열을 변경시킨다.

```js
let arr = ['가', '나', '다', '라'];

// 삭제 후 추가
console.log(arr.splice(2, 1, '마')); // ['다']
console.log(arr); // ['가', '나', '마', '라']

// 추가만
console.log(arr.splice(1, 0, '바')); // []
console.log(arr); // ['가', '바', '나', '마', '라']

// 삭제만
console.log(arr.splice(0, 2)); // ['가', '바']
console.log(arr); // ['나', '마', '라']
```



### 5. slice() - 배열의 일부분으로 새로운 배열 만들기

```
arr.slice([begin[, end]])
```

- 배열의 `begin`부터 `end - 1`까지에 대한 얕은 복사본을 새로운 배열 객체로 반환한다.
- 기존 배열을 변경시키지 않는다.

```js
let arr = [1, 2, 3, 4, 5];

console.log(arr.slice(2, 5)); // [3, 4, 5]
console.log(arr); // [1, 2, 3, 4, 5]
```



### 6. length - 배열의 길이

```js
let arr = [1, 2, 3, 4, 5];

console.log(arr.length); // 5
```



### 7. fill() - 특정 값으로 배열 채우기

```
arr.fill(value[, start[, end]])
```

- 배열의 `start` 인덱스부터 `end - 1` 인덱스까지 정적인 값 하나로 채웁니다.
- `start`, `end` 값이 없을 경우 `value` 값으로 배열을 채운다.
- 기존 배열을 변경시킨다.

```js
let arr = [1, 2, 3, 4, 5];

console.log(arr.fill(0)); // [0, 0, 0, 0, 0];
console.log(arr.fill(1, 1, 3)); // [0, 1, 1, 0, 0];
console.log(arr.fill(5, 2)); // [0, 1, 5, 5, 5];

console.log(arr) // [0, 1, 5, 5, 5];
```



### 8. includes() - 배열에 요소 포함 여부 확인하기

```
arr.includes(valueToFind[, fromIndex])
```

- `fromIndex` : 이 배열에서 검색을 시작할 위치. 기본값은 `0`.

```js
let names = ['Jessie', 'Justin', 'Leah'];

console.log(names.includes('Jessie')); // true
console.log(names.includes('Eddy')); // false
console.log(names.includes('Jessie', 1)); // false
```



### 9. join() - 배열을 문자열로 결합하기

```
arr.join([separator = ',']);
```

- separator : 배열을 문자열로 결합할 때 이어 붙일 값 (기본값은 `,`)
- 기존 배열을 변경시키지 않는다.

```js
let arr = [1, 2, 3, 4, 5];

console.log(arr.join()); // 1,2,3,4,5
console.log(arr.join('-')); // 1-2-3-4-5
console.log(arr.join('')); // 12345
console.log(arr); // [1, 2, 3, 4, 5]
```



### 10. filter() - 조건을 만족하는 요소들로 새로운 배열 만들기

```
arr.filter(callback(element[, index[, array]])[, thisArg])
```

- `element` : 처리할 현재 요소
- `index` : 처리할 현재 요소의 인덱스
- `array` : filter를 호출한 배열
- `thisArg` : callback을 사용할 때 this로 사용하는 값
- 배열 내에서 원하는 요소들만 필터링할 수 있는 유용한 메서드다.
- 기존 배열을 변경시키지 않는다.

```js
let scores = [30, 40, 60, 75, 90];
let resultScores = [];

resultScores = scores.filter((score) => {
	return score > 70;
});

console.log(resultScores); // [75, 90]
console.log(scores); // [30, 40, 60, 75, 90]
```



### 11. map() - 함수를 실행한 결과로 새로운 배열 만들기

```
arr.map(callback(element[, index[, array]]) [, thisArg])
```

- `element` : 처리할 현재 요소
- `index` : 처리할 현재 요소의 인덱스
- `array` : map을 호출한 배열
- `thisArg` : callback을 사용할 때 this로 사용하는 값
- map은 filter와 매우 유사하다. 차이점은 filter는 조건을 만족하는 요소를 필터링할 때 주로 쓰이지만 map은 요소가 아닌 새로운 값을 만들어서 return할 수 있다.
- 기존 배열을 변경시키지 않는다.

```js
let arr = [1, 2, 3, 4, 5];
let resultArr = [];

resultArr = arr.map((item) => {
	return item ** 2;
});

console.log(resultArr); // [1, 4, 9, 16, 25]
console.log(arr); // [1, 2, 3, 4, 5]
```



### 12. sort() - 배열 정렬하기

```
arr.sort([compareFunction])
```

- `compareFunction` : 정렬 순서를 정의하는 함수. 생략하면 배열은 각 요소의 문자열 변환에 따라 각 문자의 유니 코드 코드 포인트 값에 따라 정렬된다.
- 기존 배열을 변경시킨다.

```js
let arr = [1, 2, 100, 10, 222, 3];

// 유니코드에 따라 정렬
arr.sort();
console.log(arr); // [1, 10, 100, 2, 222, 3]

// 오름차순 정렬
arr.sort((a, b) => {
	return a - b;
});
console.log(arr); // [1, 2, 3, 10, 100, 222]

// 내림차순 정렬
arr.sort((a, b) => {
	return b - a;
});
console.log(arr); // [222, 100, 10, 3, 2, 1]
```



### 13. reverse() - 배열을 역순으로 정렬하기

```
arr.reverse()
```

- 기존 배열을 변경시킨다.

```js
let arr = [4, 2, 3, 5, 1];

arr.reverse();
console.log(arr); // [1, 5, 3, 2, 4]
```





- 기본: .setAtrribute(속성,값)
- 클래스: .classList.add()
- 스타일: .style.CSS속성.add()