const SYMBOLS = "012345789ABCDEF"


let hover = document.getElementById("hover")
let click = document.getElementById("click")
let doublclick = document.getElementById("double")
let title = document.querySelector("h1")

hover.addEventListener("mouseover", function () {
    this.style.color = "Red"
})

hover.addEventListener("mouseout", function () {
    this.style.color = "Black"
})

click.addEventListener("click", function () {
    this.style.setProperty("text-decoration", "line-through")
})


doublclick.addEventListener("dblclick", function () {
    this.remove()
})


function getRandomColor(){
    var color = "#";
    // for (init; condition; updater)
    for (let i=0; i < 6 ; i++){
        index = Math.floor(Math.random()*15);
        color += SYMBOLS[index]
    }
    return color;
}

function changeTitleColor(){
    let newColor = getRandomColor();
    title.style.color = newColor;
    console.log(newColor);
}

setInterval("changeTitleColor()", 500);

// Python
// for in range(10)

// let listItems = document.getElementsByTagName("li")

// for item in listItems
// item.addEventListener()