name = 'The Window';

// Solution 1
var alpha = {
  name: 'My Alpha',
  getNameFunc: function() {
    var that = this;
    return function() {
      // return this.name;
      // will return 'The Window' because when a function is called by itself it
      // is bound to the global context, this will be bound to the global object
      return that.name;
    };
  }
};

// Solution 2
var beta = {
  name: 'My Beta',
  getNameFunc: function() {
    return (function() {
      return this.name;
    }).bind(this);
  }
};

console.log(alpha.getNameFunc()());
console.log(beta.getNameFunc()());
