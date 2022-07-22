var pounds_num1 = document.querySelector("#lbs")
var submit_button = document.querySelector("#btn")

submit_button.addEventListener('click', function (){

    var answer = pounds_num1.value * 0.454

    alert(answer + "KG")
    console.log("Conversion Completed")

})

