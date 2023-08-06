// show/hide navitagion
let btn = document.getElementById('btnMenu')
let nav = document.querySelector('div.base-container > nav')

btn.addEventListener('click', () => {
    nav.classList.toggle('display-hide')
})
