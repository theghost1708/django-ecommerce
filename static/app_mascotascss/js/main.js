window.addEventListener('load', () => {
    const contenedor_loader = document.querySelector('.contenedor_loader')
    contenedor_loader.style.opacity = 0
    contenedor_loader.style.visibility = 'hidden'
})


document.querySelector('.menu-btn').addEventListener('click', () => {
    document.querySelector('.nav-menu').classList.toggle('show');
});

