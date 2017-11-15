// The following iterative sequence is defined for the set of positive integers:
//
// n → n/2 (n is even)
// n → 3n + 1 (n is odd)
//
// Using the rule above and starting with 13, we generate the following sequence:
//
// 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
// It can be seen that this sequence (starting at 13 and finishing at 1) contains
// 10 terms.
// Although it has not been proved yet (Collatz Problem), it is thought that all
// starting numbers finish at 1.
//
// Which starting number, under one million, produces the longest chain?
//
// NOTE: Once the chain starts the terms are allowed to go above one million.

function sequence(n, collatzSequence) {
  let count = 0;
  while (n != 1) {
    // Test if it is already calculated nbTerms for n
    if (collatzSequence.has(n)) {
      return collatzSequence.get(n) + count;
    } else if (n % 2 == 0) {
      n = n / 2;
    } else {
      n = 3 * n + 1;
    }
    ++count;
  }
  return count;
}

function findStartNum() {
  let longestChainStartNum = 0;
  let longestChain = 0;
  let collatzSequence = new Map();

  for (let n = 1; n < 1e6; ++n) {
    let nbTerms = sequence(n, collatzSequence);
    collatzSequence.set(n, nbTerms);

    if (nbTerms > longestChain) {
      longestChain = nbTerms;
      longestChainStartNumber = n;
    }
  }
  return longestChainStartNumber;
}

console.log(findStartNum());
