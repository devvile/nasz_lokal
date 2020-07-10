// ELEMENTS
const cats = document.querySelectorAll("div.func");
const dogs = document.querySelectorAll("div.pole-opisu");
let storage = localStorage.getItem("elem");

let i = 0;

// Pole-text ACTIVATION
cats.forEach((element) => {
  element.id = i;
  i++;
  element.style.backgroundColor = col[storage];
  element.addEventListener("click", () => {
    id = element.id;
    const yourDog = dogs[id];
    yourDog.classList.toggle("active");
  });
});
