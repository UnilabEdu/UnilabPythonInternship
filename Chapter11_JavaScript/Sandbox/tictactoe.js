var squares = document.querySelectorAll("td")

function clearBoard() {
    for (index in squares){
        squares[index].innerHTML = "";
    }
}

var resetButton = document.querySelector("#restart")

resetButton.addEventListener("click", clearBoard)

function markSquare(){
    if (this.textContent === ""){
        this.textContent = "X";
    } else if (this.textContent === "X"){
        this.textContent = "O";
    } else {
        this.textContent = ""
    }
}

for (index in squares){
    squares[index].addEventListener("click", markSquare)
}