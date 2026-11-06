const startBtn = document.getElementById("startBtn");
const nameModal = document.getElementById("nameModal");
const modalClose = document.getElementById("modalClose");
const submitName = document.getElementById("submitName");
const fullName = document.getElementById("fullName");
const nameError = document.getElementById("nameError");


startBtn.addEventListener("click", function (event) {

    event.preventDefault();

    nameModal.classList.add("active");

    fullName.focus();
});


modalClose.addEventListener("click", function () {

    nameModal.classList.remove("active");

    nameError.textContent = "";
});


submitName.addEventListener("click", function () {

    const name = fullName.value.trim();

    if (name === "") {

        nameError.textContent = "لطفاً نام و نام خانوادگی خود را وارد کنید.";

        return;
    }

    if (name.split(" ").length < 2) {

        nameError.textContent = "لطفاً نام و نام خانوادگی را وارد کنید.";

        return;
    }

    localStorage.setItem("userFullName", name);

    window.location.href = "dashboard.html";
});



// =============================
// Mobile Navbar
// =============================

const menuToggle = document.getElementById("menuToggle");
const navLinks = document.querySelector(".space");

if (menuToggle && navLinks) {

    menuToggle.addEventListener("click", function () {

        navLinks.classList.toggle("mobile-menu");

    });

}