// n! means n × (n − 1) × ... × 3 × 2 × 1
//
// For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
// and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27
//
// Find the sum of the digits in the number 100!

// In JavaScript, integer can't use more than 53 bits.
let bigInt = require('big-integer');

/**
 * Calculate factorial of a non-negative integer n
 * @param {number} n
 * @return {number} factorial
 */
function factorial(n) {
  let res = bigInt(1);
  for (let i = n; i > 0; --i) {
    // can't use res *= i for bigInt
    res = res.multiply(i);
  }
  return res;
}

/**
 * Find the sum of the digits in factorial of n
 * @param {number} n
 * @return {number}
 */
function digitSum(n) {
  let sum = 0;
  const num = factorial(n);
  for (let i = 0; i < num.toString().length; ++i) {
    sum += parseInt(num.toString()[i]);
  }
  return sum;
}

console.log(digitSum(100));
