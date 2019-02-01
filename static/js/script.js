var searchInput = document.querySelector('.searchwrap input');

var twice = 0;
window.addEventListener('keydown', function(e){
    if(e.shiftKey){
        twice += 1;
        setTimeout(function(){
            twice = 0;
        }, 300);
        if (twice == 2){
            twice = 0;
            searchInput.focus();
        }
    }
});


var anchorList = document.querySelectorAll('.infonav li a');
var secList = document.querySelectorAll('main section');


for (let i=0; i<anchorList.length; i++){
    anchorList[i].addEventListener('click', function(){
        for (let j=0; j<anchorList.length; j++){
            anchorList[j].setAttribute('class', '');
        }
        this.setAttribute('class', 'active');
        secList[i].scrollIntoView();
    });
}