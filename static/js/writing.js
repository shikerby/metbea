var btn = document.querySelector('.btn-write-post');
var baseRule = document.querySelector('.base-rule');
var editor = document.querySelector('.editor');

btn.addEventListener('click', function(){
    this.style.display = 'none';
    baseRule.style.display = 'none';
    editor.style.display = 'block';
})