// 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
// What is the sum of the digits of the number 2^1000?

// In JavaScript, integer can't use more than 53 bits.

function sumOfPowerDigits(exponent) {
  let sum = 0;
  let res = [ 1 ];

  for (let i = 0; i < exponent; ++i) {
    res = multiple2(res);
  }

  for (let i = 0; i < res.length; ++i) {
    sum += res[i];
  }

  return sum;
}

function multiple2(num) { // num is an array
  const len = num.length;
  let res = new Array(len);
  let carry = 0;

  for (let i = 0; i < len; ++i) {
    let product = num[i] * 2 + carry;
    carry = Math.floor(product / 10);
    res[i] = product % 10;
  }

  // If mutiple 2, overflow on the highest digit
  if (carry > 0) {
    res[len] = carry;
  }
  return res;
}

console.log(sumOfPowerDigits(1000));
