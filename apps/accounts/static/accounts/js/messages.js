let cancelBtns = document.querySelectorAll(".cancel-alert")
cancelBtns.forEach((value, key, parent) => {
    value.addEventListener('click', () => {
        value.parentElement.style.display = 'none'
    })
})
