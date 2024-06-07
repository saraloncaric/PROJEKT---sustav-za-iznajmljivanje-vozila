document.addEventListener("DOMContentLoaded", () => {
    const vehicleTypeSelect = document.getElementById("vehicleType");
    const vehicleBrandSelect = document.getElementById("vehicleBrand");

    const vehicleBrands = {
        automobil: ['Hyundai', 'Volkswagen', 'Ford', 'BMW', 'Audi'],
        motor: ['Yamaha', 'Suzuki', 'Kawasaki', 'Ducati', 'Aprilia'],
        kombij: ['Cirtoën', 'Ford', 'Volkswagen', 'Opel', 'Mercedes-Benz']
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

    // Mobile menu toggle
    const menuIcon = document.querySelector(".menu-icon");
    const navLinks = document.querySelector(".nav-links");

    menuIcon.addEventListener("click", () => {
        navLinks.classList.toggle("active");
    });
});
