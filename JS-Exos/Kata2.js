// Create an object prototype is to use an object constructor function
function Person(name) {
  this.name = name;
}

// Add method to prototype Person
Person.prototype.greet = function(otherName) {
  return "Hi " + otherName + ", my name is " + this.name;
}

var person = new Person("Titi");
console.log(person.greet("Tutu"));
