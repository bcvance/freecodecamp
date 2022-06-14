if ($("body").data("title") === "main_page"){
    const carouselSlide = document.querySelector(".carousel-slide");
    const carouselImages = document.querySelectorAll(".carousel-slide img");
    const prevBtn = document.querySelector("#prevBtn");
    const nextBtn = document.querySelector("#nextBtn");
    let counter = 1;
    const size = carouselImages[0].clientWidth;
    carouselSlide.style.transform = "translateX(" + (-size * counter) + "px";

    //button listeners

    nextBtn.addEventListener("click", ()=>{
    if (counter >= carouselImages.length - 1){
        return;
    }
    carouselSlide.style.transition = "transform 0.4s ease-in-out";
    counter ++;
    console.log(counter);
    carouselSlide.style.transform = "translateX(" + (-size * counter) + "px";
    });

    prevBtn.addEventListener("click", ()=>{
    if (counter <= 0){
        return;
    }
    carouselSlide.style.transition = "transform 0.4s ease-in-out";
    counter --;
    carouselSlide.style.transform = "translateX(" + (-size * counter) + "px";
    });

    carouselSlide.addEventListener("transitionend", ()=>{
    if (carouselImages[counter].id === "lastClone"){
        carouselSlide.style.transition = "none";
        counter = carouselImages.length - 2;
        carouselSlide.style.transform = "translateX(" + (-size * counter) + "px";
    }
    else if (carouselImages[counter].id === "firstClone"){
        carouselSlide.style.transition = "none";
        counter = carouselImages.length - counter;
        console.log(counter);
        carouselSlide.style.transform = "translateX(" + (-size * counter) + "px";
    }
    });
}
        

if ($("body").data("title") === "contacts_page"){
    let looper;
    let degrees = 0;
    let clicker = true;
    pootPic = document.querySelector("#poot");
    pootPic.addEventListener("click", ()=> {
        clicker = !clicker;
    })
    function rotateAnimation(el, speed) {
        let elem = document.getElementById(el);
        elem.style.transform = "rotate("+degrees+"deg)";
        looper = setTimeout("rotateAnimation(\""+el+"\","+speed+")",speed);
        if (clicker){
            degrees++;
            if (degrees > 359) {
                degrees = 1;
            }
        }
        else if (!clicker) {
            degrees --;
            if (degrees < 0) {
                degrees = 359;
            }
        }
    }
    rotateAnimation("poot", 2);
}