const track = document.querySelector('.carousel-track');
const slides = Array.from(document.querySelectorAll('.carousel-slide'));
const nextButton = document.querySelector('.carousel-btn.next');
const prevButton = document.querySelector('.carousel-btn.prev');

const mediaQuery = window.matchMedia('(max-width: 600px)');


let currentSlide = 0;
const slideWidth = slides[0].offsetWidth;

document.addEventListener('DOMContentLoaded', function () {
  nextButton.click();
  prevButton.click();
});

function updateCarousel() {
  const newTranslateX = -slideWidth * currentSlide + 70;
  track.style.transform = `translateX(${newTranslateX}px)`;
}

nextButton.addEventListener('click', () => {
  if (currentSlide < slides.length - 1) {
    currentSlide++;
    updateCarousel();
  }
});

prevButton.addEventListener('click', () => {
  if (currentSlide > 0) {
    currentSlide--;
    updateCarousel();
  }
});

