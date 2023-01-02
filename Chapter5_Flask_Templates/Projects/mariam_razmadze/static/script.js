const open = document.getElementById("open");
const close = document.getElementById("close");
const container = document.querySelector(".container-fluid");
const labels = document.querySelectorAll(".form-control label");
const textarea = document.querySelector("textarea");
const toggles = document.querySelectorAll(".q-toggle");
const buttons = document.querySelectorAll(".ub");

open.addEventListener("click", () => container.classList.add("show-nav"));
close.addEventListener("click", () => container.classList.remove("show-nav"));

labels.forEach((label) => {
  label.innerHTML = label.innerText
    .split("")
    .map(
      (letter, idx) =>
        `<span style="transition-delay:${idx * 50}ms">${letter}</span>`
    )
    .join("");
});

buttons.forEach((button) => {
  button.addEventListener("click", function (e) {
    const x = e.clientX;
    const y = e.clientY;

    const buttonTop = e.target.offsetTop;
    const buttonLeft = e.target.offsetLeft;

    const xInside = x - buttonLeft;
    const yInside = y - buttonTop;

    const c = document.createElement("span");
    c.classList.add("c");
    c.style.top = yInside + "px";
    c.style.left = xInside + "px";

    this.appendChild(c);
    setTimeout(() => c.remove(), 1000);
  });
});

toggles.forEach((toggle) => {
  toggle.addEventListener("click", () => {
    toggle.parentNode.classList.toggle("active");
  });
});

textarea.addEventListener("keyup", (e) => {
  textarea.style.height = "auto";
  let hght = e.target.scrollHeight;
  textarea.style.height = `${hght}px`;
});
