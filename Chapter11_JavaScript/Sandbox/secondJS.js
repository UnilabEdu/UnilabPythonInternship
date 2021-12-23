var header = document.querySelector("h1")

function getRandomColor(){
    let symbols = "0123456789ABCDEF"
    let color = "#"

    for (i = 0; i <6; i++){
        color += symbols[Math.floor(Math.random()*16)];
    }
    return color;


}

function changeHeaderColor(){
    header.style.color = getRandomColor();
}

setInterval("changeHeaderColor()", 1000)

let hover = document.querySelector("#hover")
let click = document.querySelector("#click")
let double = document.querySelector("#double")

hover.addEventListener("mouseover",function(){
    hover.style.color = "Blue"
})

hover.addEventListener("mouseout",function(){
    hover.style.color = "Black"
})


click.addEventListener("click",function(){
    click.style.setProperty("text-decoration", "line-through")
    }
)

double.addEventListener("dblclick",function(){
    double.remove()
})