// a calculator can calculate the average for a arbitrary number of arguments
var Calculator = {
  average: function() {
    return [].reduce.call(arguments, function(sum, argument) {
      return sum + argument;
    }, 0) / arguments.length || 0;
  }
}

console.log(Calculator.average(3, 4, 5));
console.log(Calculator.average());
