// ==========================
// نمودار مقایسه هزینه‌ها
// ==========================

new Chart(document.getElementById("expenseBar"), {

    type: "bar",

    data: {
        labels: expenseLabels,

        datasets: [{
            label: "هزینه",

            data: expenseValues,

            backgroundColor: "#F2B544",

            borderRadius: 8,

            borderSkipped: false,

            barThickness: 40,

            maxBarThickness: 30

        }]
    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        plugins: {
            legend: {
                display: false
            }
        },

        scales: {

            x: {
                ticks: {
                    color: "#F4F5F6",

                    font: {
                        family: "vazir",
                        size: 11
                    }
                },

                grid: {
                    display: false
                }
            },

            y: {
                ticks: {
                    color: "#9DA3AA",

                    font: {
                        family: "vazir"
                    }
                    
                    callback: function(value) {
                        return value.toLocaleString('fa-IR')
                    }
                },

                grid: {
                    color: "rgba(255,255,255,0.06)"


                
                }
            }
        }
    }
});


// ==========================
// نمودار روند درآمد
// ==========================

new Chart(document.getElementById("incomeLine"), {

    type: "line",

    data: {
        labels: incomeLabels,

        datasets: [{

            label: "درآمد",

            data: incomeValues,

            borderColor: "#16B8D4",

            backgroundColor: "rgba(22, 184, 212, 0.10)",

            borderWidth: 3,

            tension: 0.35,

            fill: true,

            pointRadius: 4,

            pointHoverRadius: 7,

            pointBackgroundColor: "#16B8D4",

            pointBorderWidth: 0
        }]
    },

    options: {

        responsive: true,

        maintainAspectRatio: false,

        plugins: {
            legend: {
                display: false
            }
        },

        scales: {

            x: {
                ticks: {
                    color: "#F4F5F6",

                    font: {
                        family: "vazir",
                        size: 12
                    }
                },

                grid: {
                    display: false
                }
            },

            y: {
                ticks: {
                    color: "#9DA3AA",

                    font: {
                        family: "vazir"
                    }

                    callback: function(value) {
                        return value.toLocaleString('fa-IR')
                    }
                },

                grid: {
                    color: "rgba(255,255,255,0.06)"
                }
            }
        }
    }
});



dateElement.textContent = persianDate


let lines = document.getElementById("lines");
let closeBtn = document.getElementById("closeBtn");
let sidebar = document.getElementById("sidebar");

lines.addEventListener("click", function () {
    sidebar.classList.add("active");
});

closeBtn.addEventListener("click", function () {
    sidebar.classList.remove("active");
});





const userNameElement = document.getElementById("userName");

const savedName = localStorage.getItem("userFullName");

if (savedName && userNameElement) {
    userNameElement.textContent = savedName;
}