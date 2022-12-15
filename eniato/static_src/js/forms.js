const color_input = document.getElementById('id_color')
const colors_elements = document.querySelectorAll('.color')

colors_elements.forEach(el => {
    el.addEventListener('click', event => {
        const target = event.target
        const color_activate = document.querySelector('.color.activate')
        
        color_activate.classList.toggle('activate')
        target.classList.toggle('activate')
        color_input.setAttribute('value', target.getAttribute('color'))
    })
})

$('form').submit(function () {
    $('.currency').each(function() {
        $(this).val($(this).maskMoney('unmasked')[0])
    })
})
