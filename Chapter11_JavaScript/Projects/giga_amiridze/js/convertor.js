const weight = document.getElementById("weight");
const convertBtn = document.getElementById("convertor");

convertBtn.onclick = () => {
    alert(weight.value * 0.454 + "Kg");
}

console.log("Conversion Completed");