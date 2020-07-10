// ELEMENTS
const cats = document.querySelectorAll("div.func");
const dogs = document.querySelectorAll("div.pole-opisu");
let storage = localStorage.getItem("elem");
const poleOpisu = document.querySelectorAll(".pole-opisu");

let i = 0;

function main() {
  // Pole-text ACTIVATION
  cats.forEach((element) => {
    element.id = i;
    i++;
    element.style.backgroundColor = col[storage];
    if (element.id % 2 === 0) {
      element.style.filter = "sepia(30%)";
    } else {
      element.style.filter = "sepia(65%)";
    }
    element.addEventListener("click", () => {
      id = element.id;
      const yourDog = dogs[id];
      yourDog.classList.toggle("active");
    });
  });
  // Pole opisu kolor
  poleOpisu.forEach((element) => {
    element.style.backgroundColor = col[storage];
  });
}
main();
