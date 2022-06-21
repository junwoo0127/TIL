// Array Helper Method

// 4. .reduce(callback)
// 배열의 각 요소에 대해 주어진 reduce 함수를 실행하고, 하나의 결과 값을 반환한다.
// reduce 는 배열 내의 숫자 총합, 평균 등 배열의 값을 하나로 줄이는 동작을 한다.
// map은 배열의 각 요소를 변형한다면, reduce는 배열 자체를 변형한다.

// 총합
const ssafyTests = [90, 90, 80, 77,]
const sum = ssafyTests.reduce(function (total, x) {
  return total += x // 0 쓰면 오류남
}, 0) // 초기값 주려면 여기에 줘야됨

// const sum = ssafyTests.reduce( (total, x) => total += x, 0) // 0 : 초기값
// const sum = ssafyTests.reduce( (total, x) => total += x) // 0 없어도 초기값 === 0

console.log(sum)

// callback 함수의 첫번째 매개변수는 누적값(전 단계의 결과) === total
// 두번째 매개변수는 현재 배열 요소, 현재 인덱스, 배열 자체 순이다. === x
// 초기값 === 0 ( 첫 total 값 )
// 초기값이 생략되면 배열의 첫번째 요소가 초기값이 된다.

// 4-1 연습
// 다음 배열 내의 요소의 총합을 구하시오
const arr = [0, 1, 2, 3,]
const sum1 = arr.reduce( (total1, y) => total1 += y, 0)

console.log(sum1)
