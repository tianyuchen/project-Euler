// spread function call the func with args
function spread(func, args) {
  return func.apply(this, args);
}

function someFunction(...args) {
  return args.join(' & ');
}

console.log(someFunction(1, true, "Foo", "bar"));
console.log(spread(someFunction, [1, true, "Foo", "bar"]));
