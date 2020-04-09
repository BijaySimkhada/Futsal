window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    if(scrolled>=10){
        document.querySelector("nav").style.top = "-12px";
    }else{
        document.querySelector("nav").style.top = "20px";
    }
    console.log(scrolled);
});
