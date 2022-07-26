let weight_input = document.getElementById("weight_input")
let convert_butt = document.getElementById("convert_butt")

convert_butt.onclick = () => {
    alert(weight_input.value * 0.454 + " Kg")
}

console.log("Conversion Completed")
