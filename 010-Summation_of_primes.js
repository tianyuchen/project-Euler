// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//
// Find the sum of all the primes below two million.

function primesSum() {
  const maxPrimeValue = 2e+6;
  let sum = 0;

  for (let i = 2; i <= maxPrimeValue; ++i) {
    if(isPrime(i)) {
      sum += i;
    }
  }

  function isPrime(n) {
    // x is the largest value could be a prime number
    var x = Math.floor(Math.sqrt(n));
    while (x >= 2) {
      if (n % x === 0) {
        return false;
      }
      --x;
    }
    return true;
  }
  return sum;
}

console.log(primesSum());
