// ELEMENTS
const cats = document.querySelectorAll("div.func");
const dogs = document.querySelectorAll("div.pole-opisu");
let storage = localStorage.getItem("elem");
const poleOpisu = document.querySelectorAll(".pole-opisu");
const botNote = document.querySelectorAll(".bot-note");
const opis = document.querySelectorAll(".znikniety-opis");

let i = 0;
let j = 0;

//FUNC

//NOTE BG
function noteBg() {
  poleOpisu.forEach((element) => {
    element.style.backgroundColor = col[storage];
    element.style.filter = "saturate(30%)";
  });
}

//ASSIGNMENT OF ID FOR BOT-NOTE
function noteBotId() {
  botNote.forEach((e) => {
    e.id = j;
    j++;
  });
}

// NOTE ACTIVATION
function noteAppear() {
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
      const noteBottom = botNote[id];
      noteBottom.classList.toggle("widoczny");
      const yourOpis = opis[id];
      yourOpis.classList.toggle("widoczny");
    });
  });
}
// MAIN
function main() {
  noteBotId();
  noteBg();
  noteAppear();
}

main();
