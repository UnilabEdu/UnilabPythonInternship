let todoNode = document.querySelector('.ul');
let inputNode = document.querySelector('input');
let buttonNode = document.querySelector('.button');


function todoDone() {
    let liList = document.querySelectorAll('li')
    liList.forEach(item => {
        item.addEventListener('dblclick', function (){
            this.remove()
        })
        item.addEventListener("click", function (){
            this.style.setProperty("text-decoration", "line-through")
            this.style.color = 'red'
        })
    })
}

buttonNode.addEventListener('click',function() {
    // addTodo(inputNode.value)
    let li = document.createElement('li');
    li.innerText = inputNode.value;
    todoNode.append(li)
    inputNode.value = ''
    todoDone()
})



