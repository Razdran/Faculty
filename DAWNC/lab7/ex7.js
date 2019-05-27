genericG(add)(3)(10)(15)();
function add(a,b){
    return a+b;
}
function genericG(fn){
    return function innerF(x){
        if(x === undefined){
            //cazul in care apelez genericG(add)();
            return 0;
        }
        return function(y){
            if(y===undefined){
                return x;
                //cazul genericG(add)(5)();
            }
            return innerF(fn(x,y));
            //cazul in care apelez genericG(add)(5)(4)();
        }
    }
}