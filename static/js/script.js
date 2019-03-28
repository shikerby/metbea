// 手动封装了 一个 属于我们自己的 ajax, 然后将其 绑定在 传入的全局对象 window 上，这样 在任何页面，只要引入
// 这个脚本， 就可以使用 我这个自己封装的ajax

(function(){
    function myajax(opt){
        opt = opt || {};
        opt.method = opt.method.toUpperCase() || 'POST';
        opt.url = opt.url || '';
        opt.async = opt.async || true;
        opt.csrftoken = opt.csrftoken || '';
        opt.data = opt.data || null;
        opt.success = opt.success || function (){};

        var xmlhttp = new XMLHttpRequest();
        var params = [];

        for(let key in opt.data){
            params.push(key + '=' + opt.data[key]);
        }
        var postData = params.join('&');
        if (opt.method.toUpperCase() === 'POST') {
            xmlhttp.open(opt.method, opt.url, opt.async);
            xmlhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
            xmlhttp.setRequestHeader("X-CSRFToken", opt.csrftoken);
            xmlhttp.send(postData);
        }
        else if (opt.method.toUpperCase() === 'GET') {
            xmlhttp.open(opt.method, opt.url + '?' + postData, opt.async);
            xmlhttp.send(null);
        }
        xmlhttp.onreadystatechange = function () {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                opt.success(xmlhttp.responseText);
            }
        };
    }
    window.getCookie = function(cname){
        var name = cname + "=";
        var ca = document.cookie.split(';');
        for(var i=0; i<ca.length; i++){
            var c = ca[i].trim();
            if (c.indexOf(name)==0) return c.substring(name.length,c.length);
        }
        return "";
    }

    window.myajax = myajax;

})(window, undefined);






var searchInput = document.querySelector('.searchwrap input');

var twice = 0;
document.addEventListener('keyup', function(e){
    if(e.keyCode == 16){
        twice += 1;
        setTimeout(function(){
            twice = 0;
        }, 500);
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