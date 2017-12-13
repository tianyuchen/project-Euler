//Test if all parameters are Number type

// Solution 1
function numbers(...args) {
  for (let i = 0; i < args.length; ++i) {
    if (typeof args[i] !== 'number') {
      return false;
    }
  }
  return true;
}

// Solution 2
function ifNumber() {
  return Array.prototype.filter.call(arguments, function(argument) {
    return typeof argument !== 'number';
  }).length === 0;
}

console.log(numbers(1, 4, 3, 2, 5));
console.log(numbers(1, "a", 3));
console.log(numbers(1, 3, NaN));
