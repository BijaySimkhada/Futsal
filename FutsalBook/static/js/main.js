window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    if(scrolled>=10){
        document.querySelector("nav").style.top = "-12px";
    }else{
        document.querySelector("nav").style.top = "20px";
    }
    console.log(scrolled);
});


function expand(){
    obj = document.querySelector("#login-option");
    obj.style.display = "block";
}

function contract(){
    obj = document.querySelector("#login-option");
    obj.style.display = "none";
}