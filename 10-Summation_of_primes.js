// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//
// Find the sum of all the primes below two million.

(function primesSum() {
  var maxPrimeValue = 2e+6;
  var i = 2;
  var sum = 0;

  while(i <= maxPrimeValue) {
    if(isPrime(i) === true) {
      sum += i;
    }
    i++;
  }

  function isPrime(n) {
    //x is the largest value could be a prime number
    var x = Math.floor(Math.sqrt(n));

    while (x >= 2) {
      if (n % x === 0) {
        return false;
      }
      x--;
    }
    return true;
  }

  console.log(sum);
  return sum;
}());
