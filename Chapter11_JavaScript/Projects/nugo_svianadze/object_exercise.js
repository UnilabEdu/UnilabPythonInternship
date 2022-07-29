/ objects exercise here


////////////////////
// PROBLEM 1 //////
//////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31
}

// Add a method called nameLength that prints out the
// length of the employees name to the console.

function nameLength(employee) {
    //Code Goes Here
    console.log(employee.name.length);
}

///////////////////
// PROBLEM 2 /////
/////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31
}

// Write program that will create an Alert in the browser of each of the
// object's values for the key value pairs. For example, it should alert:

// Name is John Smith, Job is Programmer, Age is 31.

function alertObject(employee) {
    //Code Goes Here
    alert("Name is " + employee.name + ", Job is " + employee.job + ", Age is " + employee.age);
}

///////////////////
// PROBLEM 3 /////
/////////////////

// Given the object:
var employee = {
  name: "John Smith",
  job: "Programmer",
  age: 31
}

// Add a method called lastName that prints
// out the employee's last name to the console.

function lastName(employee) {
    //Code Goes Here
    console.log(employee.name.split(" ")[1]);
}