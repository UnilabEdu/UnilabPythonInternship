const textInput = document.querySelector("#textInput")
const addButton = document.querySelector("#addButton")
const toDoList = document.querySelector("#ToDoList")
var todoItems;
var isActivate = false

addButton.addEventListener("click", function () {

    let newDiv = document.createElement("div")
    toDoList.appendChild(newDiv)

    let newItem = document.createElement("p")
    newItem.textContent = textInput.value
    newDiv.appendChild(newItem)
    textInput.value = ""
    todoItems = document.querySelectorAll("p")

    let newBtn = document.createElement("button")
    newBtn.textContent = "delete"
    newDiv.appendChild(newBtn)



    todoItems.forEach(function(item){
        item.addEventListener('dblclick', function(){
            if(isActivate){
                item.style.color = 'black'
                isActivate = !isActivate
            } else {
                item.style.color = 'green'
                isActivate = !isActivate
            }
        })

    })

    newBtn.addEventListener('click', function(){
        newBtn.parentNode.remove();
    })
})







