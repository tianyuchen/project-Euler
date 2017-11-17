// If the numbers 1 to 5 are written out in words: one, two, three, four, five,
// then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
//
// If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
// words, how many letters would be used?
//
//
// NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty
// -two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters.
// The use of "and" when writing out numbers is in compliance with British usage.

const ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
              'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
              'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'];

const tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
              'eighty', 'ninety'];

function countLetters(n) {
  let sum = 0;
  for (let i = 1; i <= n; ++i) {
    sum += numberToEnglish(i).length;
  }
  return sum;
}

function numberToEnglish(n) {
  if (n < 20) {
    return ones[n];
  }
  else if (n < 100) {
    return tens[Math.floor(n / 10)] + ones[n % 10];
  }
  else if (n < 1000) {
    return ones[Math.floor(n / 100)] + 'hundred' + (n % 100 == 0 ? '' : 'and' +
    numberToEnglish(n % 100));
  }
  else if (n < 1000000){
    return numberToEnglish(Math.floor(n / 1000)) + 'thousand' + (n % 1000 == 0 ? '' :
    numberToEnglish(n % 1000));;
  }
}

console.log(countLetters(1000));
