function changeTextColor(){
    const heading = document.querySelector('h1');
    heading.style.color = heading.style.color === 'blue' ? 'black' : 'blue';
}

document.addEventListener('DOMContentLoaded', () =>{
    const heading = document.querySelector('h1');
    heading.addEventListener('click', changeTextColor);
});