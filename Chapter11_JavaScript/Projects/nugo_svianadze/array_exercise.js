// ''  PART4 Array Exercise ''

// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array

function addNew(name) {
    //Code Goes Here
    roster.push(name);
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

function remove(name) {
    //Code Goes Here
    var index = roster.indexOf(name);
    roster.splice(index, 1);
}

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.

function display() {
    //Code Goes Here
    console.log(roster);
}

// Start by asking if they want to use the web app



// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.

while (true) {
    var action = prompt("What would you like to do? (add, remove, display, quit)");
    if (action === "add") {
        var name = prompt("What is the student's name?");
        addNew(name);
    } else if (action === "remove") {
        var name = prompt("What is the student's name?");
        remove(name);
    } else if (action === "display") {
        display();
    } else if (action === "quit") {
        break;
    }
}