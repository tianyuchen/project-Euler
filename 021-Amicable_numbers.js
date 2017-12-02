// Let d(n) be defined as the sum of proper divisors of n (numbers less than n
// which divide evenly into n).
// If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
// each of a and b are called amicable numbers.
//
// For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
// 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
// 71 and 142; so d(284) = 220.
//
// Evaluate the sum of all the amicable numbers under 10000.

/**
 * Function to calculate the sum of divisors
 * @param {number} n
 * @return {number} sum of divisors
 */
function sumDivisors(n) {
  // Every number has divisor value 1
  let sum = 1;
  let sqrtNum = Math.floor(Math.sqrt(n));
  for (let i = 2; i <= sqrtNum; ++i) {
    if (n % i == 0) {
      sum += i;
      sum += n / i;
    }
  }
  // The square root divisor shouldn't be counted twice
  if (Number.isInteger(Math.sqrt(n)) && n != 1) {
    sum -= Math.sqrt(n);
  }
  return sum;
}

/**
 * Find the sum of all the amicable numbers under n
 * @param {number} n
 * @return {number}
 */
function findEmicableNum(n) {
  let sum = 0;
  for (let i = 2; i < n; ++i) {
    if ((sumDivisors(sumDivisors(i))) == i && i != sumDivisors(i)) {
      sum += i;
    }
  }
  return sum;
}

console.log(findEmicableNum(10000));
