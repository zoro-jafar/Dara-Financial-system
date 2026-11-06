document.addEventListener("DOMContentLoaded", function() {
    
    // =============================
    // ۱. باز و بسته کردن پنجره (مودال)
    // =============================
    const openInvoiceModal = document.getElementById("openInvoiceModal");
    const closeInvoiceModal = document.getElementById("closeInvoiceModal");
    const invoiceModal = document.getElementById("invoiceModal");

    if (openInvoiceModal && invoiceModal) {
        openInvoiceModal.addEventListener("click", function () {
            invoiceModal.classList.add("active");
        });
    }

    if (closeInvoiceModal && invoiceModal) {
        closeInvoiceModal.addEventListener("click", function () {
            invoiceModal.classList.remove("active");
        });
    }

    if (invoiceModal) {
        invoiceModal.addEventListener("click", function (event) {
            if (event.target === invoiceModal) {
                invoiceModal.classList.remove("active");
            }
        });
    }

    // =============================
    // ۲. منوی موبایل
    // =============================
    const menuToggle = document.getElementById("menuToggle");
    const navLinks = document.querySelector(".space");

    if (menuToggle && navLinks) {
        menuToggle.addEventListener("click", function () {
            navLinks.classList.toggle("mobile-menu");
        });
    }

});