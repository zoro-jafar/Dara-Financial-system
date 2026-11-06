document.addEventListener("DOMContentLoaded", function() {
    
    // باز و بسته کردن مودال
    const openBtn = document.getElementById("openInvestmentModal");
    const closeBtn = document.getElementById("closeInvestmentModal");
    const modal = document.getElementById("investmentModal");

    if (openBtn && modal) {
        openBtn.addEventListener("click", function () { modal.classList.add("active"); });
    }
    if (closeBtn && modal) {
        closeBtn.addEventListener("click", function () { modal.classList.remove("active"); });
    }
    if (modal) {
        modal.addEventListener("click", function (e) { 
            if (e.target === modal) modal.classList.remove("active"); 
        });
    }

    // منوی موبایل
    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.querySelector(".space");
    if (menuToggle && navLinks) {
        menuToggle.addEventListener("click", function () {
            navLinks.classList.toggle("mobile-menu");
        });
    }
});