window.addEventListener('scroll', () => {
    const scrolled = window.scrollY;
    if(scrolled>=10){
        document.querySelector("nav").style.top = "-1vh";
    }else{
        document.querySelector("nav").style.top = "18px";
    }
    console.log(scrolled);
});


function expand(){
    obj = document.querySelector("#login-option");
    obj2 = document.querySelector('#screen');
    obj3 = document.querySelector('.header');
    obj3.style.backgroundColor = "#000000bd";
    obj2.style.backgroundColor = "#000000bd"
    obj2.style.zindex = "3"
    obj.style.display = "block";
}

function contract(){
    obj = document.querySelector("#login-option");
    obj2 = document.querySelector('#screen');
    obj2.style.backgroundColor = "transparent"
    obj2.style.zindex = "-1"
    obj.style.display = "none";
    obj3 = document.querySelector('.header');
    obj3.style.backgroundColor = "transparent";
}