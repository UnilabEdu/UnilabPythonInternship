// პრიმიტივები

10 // integers
11.23 // float
-45 // negatives

"Hello World" // string
'Another Hello World String' // string

// booleans
true
false

// ცარიელი მნიშვნელობა - None
undefined
null

myVariable = null

// operations on numbers

2 + 2
2 - 2
2 * 2
10 / 2

10 ** 3

15 % 14

// We can use:
var countries = ["USA", "Germany", "Georgia", "Ukraine", "China", "Russia"];
var lastItem = countries.pop()
var lastItem = countries.pop()
countries.push("Moldova")

for (var index = 0; index < countries.length; index++){
  console.log(countries[index])
}

for (index in countries){
  console.log(countries[index])
}

for (countrie of countries){
  console.log(countrie)
}

function printName(name){
  console.log("The name is " + name)
}

countries.forEach(printName)


countries.forEach(country => console.log(country))

var carInfo = {
  maker: "Toyota",
  year: 1990,
  model: "Camry",

  honk: function(){
    console.log("Hooonk! Hooonk! 📯");
  },
  // self -> this
  repr: function(){
    console.log("The car is " + this.year + "s " + this.maker +" "+ this.model);
  }
}

carInfo.honk()

carInfo.repr()

var mess = { a: "hello", b: ['x','y','z'] , c: {'inside': [ 4 ,5, ["weird"]]}};

mess["b"][0] = "o"

// console.log(mess)

// for (var key in carInfo){
//   console.log(key +": "+ carInfo[key])
// }
