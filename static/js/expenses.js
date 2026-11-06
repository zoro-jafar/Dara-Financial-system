document.addEventListener("DOMContentLoaded", function() {
    
    // =============================
    // ۱. باز و بسته کردن پنجره (مودال)
    // =============================
    const openModal = document.getElementById("openModal");
    const closeModal = document.getElementById("closeModal");
    const expenseModal = document.getElementById("expenseModal");

    if (openModal && expenseModal) {
        openModal.addEventListener("click", function () {
            expenseModal.classList.add("active");
        });
    }

    if (closeModal && expenseModal) {
        closeModal.addEventListener("click", function () {
            expenseModal.classList.remove("active");
        });
    }

    if (expenseModal) {
        expenseModal.addEventListener("click", function (event) {
            if (event.target === expenseModal) {
                expenseModal.classList.remove("active");
            }
        });
    }

    // =============================
    // ۲. نمودار
    // =============================
    const chart = document.getElementById("expenseChart");
    
    if (chart) {
        new Chart(chart, {
            type: "doughnut",
            data: {
                labels: typeof chartLabels !== 'undefined' ? chartLabels : [],
                datasets: [{
                    data: typeof chartValues !== 'undefined' ? chartValues : [],
                    backgroundColor: ["#F2B544", "#16B8D4", "#5FAF8A", "#D979A8", "#8A9BA8"],
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { 
                        position: "bottom", 
                        labels: { color: "#F4F5F6", font: { family: "Vazir" }, padding: 15 } 
                    }
                    tooltip:{
                        callbacks:{
                            label: function(context) {
                                let label = context.label || '';
                                if (label) {
                                    label += ': ';
                                }
                                if (context.parsed !== null) {
                                    label += context.parsed.toLocaleString('fa-IR');
                                }
                                return label;
                            }
                        }
                    }
                }
            }
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