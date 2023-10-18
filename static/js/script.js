// CARTA GIRATOTIA
document.querySelectorAll('.flip-button').forEach(button => {
    button.addEventListener('click', function() {
        const card = this.closest('.card');
        card.classList.toggle('flipped');
    });
});

