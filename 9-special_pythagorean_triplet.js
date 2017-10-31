// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
//
// a2 + b2 = c2
// For example, 32 + 42 = 9 + 16 = 25 = 52.
//
// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.

(function findPythagoreanTriplet() {
  var a = 1, b = 2, c;
  while(a < 1000) {
    while(b < 1000 && b > a) {
      c = 1000 - a - b;
      if (c < b) {
        break;
      }
      if (Math.pow(a, 2) + Math.pow(b, 2) === Math.pow(c, 2)) {
        console.log(a * b * c);
        return a * b * c;
      }
      b++;
    }
    a++;
    b = a + 1;
  }
}());
