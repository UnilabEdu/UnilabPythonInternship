// Part 6 - Objects Exercise
// PROBLEM 1 //////
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31
}
function nameLength(obj) {console.log(obj.name.length)}
nameLength(employee)
//PROBLEM 2 /////
// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31
}
function something(obj) {
  console.log("Name is " + obj.name)
  console.log("Works as " + obj.job)
  console.log("Is " + obj.age + " years old")
}
something(employee)

// PROBLEM 3 /////
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31
}
function splitstring(obj) {
  const myArray = obj.name.split(" ");
  let word = myArray[1];
  console.log(word)
}
splitstring(employee)
