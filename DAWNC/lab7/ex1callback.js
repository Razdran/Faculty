function logName(name) { console.log(name); }
setTimeout(function(){
    logName('Bob');
},2000)

function startAfter(cb,nr,offset){
    window.setTimeout(function (){setInterval(cb,nr)},offset);
    
}
/*
function stopAfter(cb,nr,max){
    cb('Bob');
    if(max>0)
    setTimeout(function(){
        stopAfter(cb,nr,--max)
    },nr);
}
*/
function stopAfter(cb,nr,max){
    var intervalID=setInterval(function(){
        cb('Bob');
    },nr);
    setTimeout(function(){
        /*...
        ...
        ...*/
    })
}