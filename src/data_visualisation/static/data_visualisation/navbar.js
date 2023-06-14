document.addEventListener("DOMContentLoaded", function (event) {
    const page = window.location.pathname.split('/')[1] === '' ? "home" : window.location.pathname.split('/')[1]
    document.getElementById(page).classList.add('active')
})