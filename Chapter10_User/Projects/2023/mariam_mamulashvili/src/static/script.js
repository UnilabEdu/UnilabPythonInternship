
console.log('Script executed');
const productContainers = [...document.querySelectorAll('.product-container')];
const nextBtns = [...document.querySelectorAll('.next-btn')];
const preBtns = [...document.querySelectorAll('.pre-btn')];

productContainers.forEach((item, i) => {
    const cardWidth = item.querySelector('.col-md-3').offsetWidth;
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;
    console.log('Container width:', containerWidth);

    nextBtns[i].addEventListener('click', () => {
        console.log('Next button clicked');
        item.scrollLeft += cardWidth;
    });

    preBtns[i].addEventListener('click', () => {
        console.log('Previous button clicked');
        item.scrollLeft -= cardWidth;
    });
});


document.querySelectorAll('.popup-wrapper img').forEach(image => {
    image.onclick = () => {
        document.querySelector('.popup-image').style.display = 'block';
        document.querySelector('.popup-image img').src = image.getAttribute('src');
    };
});

document.querySelector('.popup-image span').onclick = () => {
    document.querySelector('.popup-image').style.display = 'none';
};