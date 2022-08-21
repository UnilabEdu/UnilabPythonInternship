// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!

var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT
function add(name) {
    roster.push(name);
}

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array

// REMOVE STUDENT
function remove(name) {
    let index = roster.indexOf(name);
    roster.splice(index, 1);
}

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript

// DISPLAY ROSTER
function display() {
    console.log(roster)
}

// Create a function called display that prints out the roster to the console.

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.

while (true) {
    let result = prompt("What do you want to do? (add, remove, display, quit)");
    if (result === "add") {
        let name = prompt("Student's name?");
        add(name);
    } else if (result === "remove") {
        let name = prompt("Student's name?");
        remove(name);
    } else if (result === "display") {
        display();
    } else if (result === "quit") {
        break;
    }
}
