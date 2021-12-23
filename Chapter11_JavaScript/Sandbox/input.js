const textInput = document.querySelector("#text-input")
const addButton = document.querySelector("#add-button")
const toDoList = document.querySelector("#todo-list")
addButton.addEventListener("click", function () {
    let newItem = document.createElement("P")
    newItem.textContent = textInput.value
    toDoList.appendChild(newItem)
    textInput.value = ""
})

// create element
