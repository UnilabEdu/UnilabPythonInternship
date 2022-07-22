let hover = document.getElementById("hover")
let click = document.getElementById("click")
let doublclick = document.getElementById("double")

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

// Python
// for in range(10)

// let listItems = document.getElementsByTagName("li")

// for item in listItems
// item.addEventListener()