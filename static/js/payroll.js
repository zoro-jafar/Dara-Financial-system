document.addEventListener("DOMContentLoaded", function() {
    
    // =============================
    // ۱. باز و بسته کردن پنجره (مودال)
    // =============================
    const openBtn = document.getElementById("openPayrollModal");
    const closeBtn = document.getElementById("closePayrollModal");
    const modal = document.getElementById("payrollModal");

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

    // =============================
    // ۲. ماشین حساب حقوق
    // =============================
    const calculateSalary = document.getElementById("calculateSalary");
    if (calculateSalary) {
        calculateSalary.addEventListener("click", function () {
            const base = Number(document.getElementById("baseSalary").value) || 0;
            const ben = Number(document.getElementById("benefits").value) || 0;
            const ded = Number(document.getElementById("deductions").value) || 0;
            const final = base + ben - ded;
            document.getElementById("salaryResult").textContent = final.toLocaleString("fa-IR") + " تومان";
        });
    }

    // =============================
    // ۳. منوی موبایل
    // =============================
    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.querySelector(".space");
    if (menuToggle && navLinks) {
        menuToggle.addEventListener("click", function () {
            navLinks.classList.toggle("mobile-menu");
        });
    }
});