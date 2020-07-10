//ELEMENTS

let ind = 0;
const boxy = document.querySelectorAll("div.box");

//EVENT LISTENRES

//RANDOM COLOR FROM LIST PLUS INHERITACNE FOR DETAIL VIEW
function main() {
  boxy.forEach((element) => {
    element.id = ind;
    ind++;
    element.style.backgroundColor = col[element.id];
    element.addEventListener("click", () => {
      localStorage.setItem("elem", element.id);
    });
  });
}

main();
