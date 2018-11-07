// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//
// Find the sum of all the primes below two million.

/**
 * Function to calculate sum of primes
 * @return {number} sum of primes
 */
function primesSum() {
  const maxPrimeValue = 2e+6;
  let sum = 0;

  for (let i = 2; i <= maxPrimeValue; ++i) {
    if (isPrime(i)) {
      sum += i;
    }
  }
  return sum;
}

/**
 * Function to test if it is a prime number
 * @param {number} n to be tested
 * @return {boolean} if it is a prime number, return true
 */
function isPrime(n) {
  // x is the largest value could be a prime number
  let x = Math.floor(Math.sqrt(n));
  while (x >= 2) {
    if (n % x === 0) {
      return false;
    }
    --x;
  }
  return true;
}

console.log(primesSum());
