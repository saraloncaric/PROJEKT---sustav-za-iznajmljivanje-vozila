document.addEventListener("DOMContentLoaded", () => {
    const vehicleTypeSelect = document.getElementById("vehicleType");
    const vehicleBrandSelect = document.getElementById("vehicleBrands");

    const vehicleBrands = {
        automobil: ['Hyundai', 'Volkswagen', 'Ford', 'BMW', 'Audi'],
        motor: ['Yamaha', 'Suzuki', 'Kawasaki', 'Ducati', 'Aprilia'],
        kombi: ['Citroën', 'Ford', 'Volkswagen', 'Opel', 'Mercedes-Benz']
    };

    vehicleTypeSelect.addEventListener("change", (event) => {
        const selectedType = event.target.value;

        while (vehicleBrandSelect.options.length > 1) {
            vehicleBrandSelect.remove(1);
        }

        if (vehicleBrands[selectedType]) {
            vehicleBrands[selectedType].forEach((brand) => {
                const option = document.createElement("option");
                option.value = brand;
                option.textContent = brand;
                vehicleBrandSelect.appendChild(option);
            });

            vehicleBrandSelect.disabled = false;
        } else {
            vehicleBrandSelect.disabled = true;
        }
    });

    const cancelButton = document.getElementById("cancelButton");
    cancelButton.addEventListener("click", () => {
        document.getElementById("rentalForm").reset();
        vehicleBrandSelect.disabled = true;
    });

    const menuIcon = document.querySelector(".menu-icon");
    const navLinks = document.querySelector(".nav-links");

    menuIcon.addEventListener("click", () => {
        navLinks.classList.toggle("active");
    });

    const vehicleRentals = {
        automobil: 50,
        motor: 30,
        kombi: 20
    };

    const brandPercentages = {
        Hyundai: 20,
        Volkswagen: 30,
        Ford: 25,
        BMW: 15,
        Audi: 10
    };

    const ctxBar = document.getElementById('vehicleTypeChart')?.getContext('2d');
    if (!ctxBar) {
        console.error('Failed to get 2D context for vehicleTypeChart');
    } else {
        new Chart(ctxBar, {
            type: 'bar',
            data: {
                labels: Object.keys(vehicleRentals),
                datasets: [{
                    label: 'Broj iznajmljivanja',
                    data: Object.values(vehicleRentals),
                    backgroundColor: ['#ff6347', '#36a2eb', '#ffce56']
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    const ctxPie = document.getElementById('brandPercentageChart')?.getContext('2d');
    if (!ctxPie) {
        console.error('Failed to get 2D context for brandPercentageChart');
    } else {
        new Chart(ctxPie, {
            type: 'pie',
            data: {
                labels: Object.keys(brandPercentages),
                datasets: [{
                    data: Object.values(brandPercentages),
                    backgroundColor: ['#ff6347', '#36a2eb', '#ffce56', '#4bc0c0', '#9966ff']
                }]
            },
            options: {
                responsive: true
            }
        });
    }
});