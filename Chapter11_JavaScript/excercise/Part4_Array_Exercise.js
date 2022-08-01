// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew (name){
    roster.push(name)
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript

function remove(name){
    var index = roster.indexOf(name)

    if (index >= 0){
        roster.splice(index)
    }
}

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.


// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.

function display(){
    var answer = prompt("Do you want to yous the web app? type Y or N ")
    while (answer === "Y"){
        let action = prompt("Type the action you want to use: add, remove, display or quit")
        if (action=== "add"){
            let name = prompt("Enter the name you want to add: ")
            addNew(name)
        }else if (action==="remove"){
            let name = prompt("Enter the name you want to Delete: ")
            remove(name)
        }else if(action === "display"){
            console.log(roster)

        }else if(action==="quit"){
            break
        }else {
            console.log("Wrong input")
        }
    }
}












