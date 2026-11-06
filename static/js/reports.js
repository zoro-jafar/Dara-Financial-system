// =============================
// Report Button
// =============================

const showReport =
    document.getElementById("showReport");

const reportType =
    document.getElementById("reportType");


showReport.addEventListener("click", function () {

    const selectedReport =
        reportType.value;

    if (selectedReport === "trial") {

        alert("گزارش تراز آزمایشی نمایش داده شد.");

    } else if (selectedReport === "profit") {

        alert("گزارش سود و زیان آماده است.");

    } else if (selectedReport === "income") {

        alert("گزارش درآمد و هزینه آماده است.");

    } else {

        alert("گزارش گردش حساب آماده است.");

    }

});


// =============================
// Export Report
// =============================

const exportReport =
    document.getElementById("exportReport");


exportReport.addEventListener("click", function () {

    alert("گزارش برای دریافت آماده شد.");

});


// =============================
// Mobile Menu
// =============================

const menuToggle =
    document.getElementById("menuToggle");

const navLinks =
    document.querySelector(".space");


if (menuToggle && navLinks) {

    menuToggle.addEventListener("click", function () {

        navLinks.classList.toggle("mobile-menu");

    });

}