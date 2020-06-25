// ELEMENTS
const cats = document.querySelectorAll("div.func");
const dogs = document.querySelectorAll("div.pole-opisu");

let i = 0;

cats.forEach((element) => {
  element.id = i;
  i++;
  element.addEventListener("click", () => {
    id = element.id;
    const yourDog = dogs[id];
    yourDog.classList.toggle("active");
  });
});
