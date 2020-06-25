//ELEMENTS
const col = [
  "#ecc209",
  "#98d6ea",
  "#b590ca",
  "#f5cab3",
  "#a2de96",
  "#bac964",
  "#709fb0",
  "#726a95",
  "#ffbd69",
];
let ind = 0;
let bg = 2;
const boxy = document.querySelectorAll("div.box");

//EVENT LISTENRES
boxy.forEach((element) => {
  element.id = ind;
  ind++;
  element.style.backgroundColor = col[element.id];
  element.addEventListener("click", () => {
    bg = element.id;
  });
});
