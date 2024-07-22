
//***************Hamburger Nav******************
const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".navbar-links");

hamburger.addEventListener("click", () =>{
    hamburger.classList.toggle("active");
    navMenu.classList.toggle("active");
});