// PART 8 - LOOP EXERCISES
// Before we continue on with your project, let's practice some loops!
// You'll have just two problems, but you'll need to use each loop type we
// learned about to solve them!

// PROBLEM 1

// Use a For Loop to print (console.log()) out the word "hello" 5 times.
// Do this with a While Loop and a For Loop

// While Loop
var i = 0

while (i < 5) {
    console.log("Hello")
    i++
}

// For Loop
for (let j = 0; j <5; j++){
    console.log("Hello")
}


// PROBLEM 2

// Use Loops to console.log() (print out) all the odd numbers from 1 to 25
// Do this using two methods, a while loop and a for loop

// METHOD ONE
// While Loop
var i = 1

while (i <= 5) {
    if (i % 2 == 1){
        console.log(i);
    }
    i++
}

// METHOD TWO
// For Loop
for (let j = 0; j <= 25; ++j){
    if (j % 2 == 1){
        console.log(j);
    }
}