/// PROBLEM 1 ///
//While loop
var i = 0
while (i<5){console.log("Hello")
    i++}
//For Loop
for (var j = 0; j < 5; j++) {console.log("Hello")}


// PROBLEM 2 ///

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
//While Loop
var i = 1

while (i <= 25) {
    if (i % 2 == 1){
        console.log(i)
    }
    i++
}

//For Loop
for (var i = 1; i <= 25; i++){
    if (i % 2 == 1){
        console.log(i)
    }
}
