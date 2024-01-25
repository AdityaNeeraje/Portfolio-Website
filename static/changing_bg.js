document.addEventListener('DOMContentLoaded', function () {
const slideshowContainer = document.getElementById('slideshow');
const url = `${window.location.href}/images`;
fetch(url, { method: 'POST' })
    .then(response => response.json())
    .then(data => {
        var imagePathString = data.imagePaths;
        var imagePaths = imagePathString.split(',');
        var altString = data.alts;
        var alts = altString.split(',');
        console.log(imagePaths);
        console.log(alts);
        let currentIndex = randomInt = Math.floor(Math.random() * imagePaths.length);

    function changeBackground() {
        slideshowContainer.src = imagePaths[currentIndex];
        slideshowContainer.alt = alts[currentIndex];
        currentIndex = (currentIndex + 1) % imagePaths.length;
    }

    changeBackground();

    setInterval(changeBackground, 5000);
    })
    .catch(error => console.error('Error:', error));

//const imagePaths = ['/static/images/Othello.png', '/static/images/Snake Game.png', '/static/images/2048.png', '/static/images/Cookie Clicker.png', '/static/images/Name the States of the US.png'];
//const alts = ['Othello - Can be played Multiplayer or against the Computer', 'Snake Game - Have encoded multiple levels of difficulty', '2048 Game', 'Playing the Cookie Clicker game for 5 minutes using Selenium', 'Name the States of the US Game, with hints']
});
