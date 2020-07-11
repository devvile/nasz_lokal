// ELEMENTS
const cats = document.querySelectorAll("div.func");
const dogs = document.querySelectorAll("div.pole-opisu");
let storage = localStorage.getItem("elem");
const poleOpisu = document.querySelectorAll(".pole-opisu");
const koszyk = document.querySelectorAll(".znikniety");
const opis = document.querySelectorAll(".znikniety-opis");

let i = 0;
let j = 0;

function main() {
  // BIN ID ASSING
  koszyk.forEach((e) => {
    e.id = j;
    j++;
  });
  // Pole-text ACTIVATION

  cats.forEach((element) => {
    element.id = i;
    i++;
    element.style.backgroundColor = col[storage];
    if (element.id % 2 === 0) {
      element.style.filter = "sepia(20%)";
    } else {
      element.style.filter = "sepia(50%)";
    }
    element.addEventListener("click", () => {
      id = element.id;
      const yourDog = dogs[id];
      yourDog.classList.toggle("active");

      /*
      const yourBin = koszyk[id];
      yourBin.classList.toggle("widoczny");
      const yourOpis = opis[id];
      yourOpis.classList.toggle("widoczny");
      */
    });
  });

  // Pole opisu kolor
  poleOpisu.forEach((element) => {
    element.style.backgroundColor = col[storage];
    element.style.filter = "saturate(30%)";
  });
}
main();
