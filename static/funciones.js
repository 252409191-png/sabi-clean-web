document.addEventListener("DOMContentLoaded", () => {
    const boton = document.querySelector(".menu-toggle");
    const menu = document.querySelector(".nav");

    if (boton && menu) {
        boton.addEventListener("click", () => {
            const abierto = menu.classList.toggle("open");
            boton.setAttribute("aria-expanded", String(abierto));
            boton.setAttribute("aria-label", abierto ? "Cerrar menú" : "Abrir menú");
        });
    }

    // Confirmación antes de salir si el formulario está incompleto no es necesaria:
    // los campos required del navegador se encargan de validarlo.
});
