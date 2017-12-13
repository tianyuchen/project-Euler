// Find the last element of a list
// A list can be an array, a string or a list of arguments

// Solution 1
function findLastElement(list) {
  if (arguments.length === 1) {
    return list[list.length - 1];
  } else {
    return arguments[arguments.length - 1];
  }
}

// Solution 2
function lastElement(list) {
  var last = arguments[arguments.length - 1];
  console.log(last);
  return last[last.length - 1] || last;
}

console.log(lastElement([1, 2, 3, 4]));
console.log(lastElement("xyz"));
console.log(lastElement(1, 2, 3, 4));
