function findDuplicate(...args) {
  // new Set([iterable]): A value in the Set may only occur once
  return (args.length !== new Set(args).size);
}

console.log(findDuplicate(1, 2, 3));
console.log(findDuplicate(1, 2, 3, 2));
console.log(findDuplicate('1', '2', '3', '2'));
