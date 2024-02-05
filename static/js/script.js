document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('#submit').disabled = true;
    document.querySelector('#name').onkeyup = function(){
        document.querySelector('#submit').disabled = false;
    }
    if(document.querySelector('#name').value === ''){
        document.querySelector('#submit').disabled = true;
    }
})


