let myCounter=myCounter(5);
myCounter.up();
myCounter.down();
myCounter.up();
/*sintaxa de obiect  
        |
        |
        |
        V
*/
function myCounter(start){
    //tot ce e in afara returnului e privat
    return{                 //tot ce e in return e public
        up:function(){
            start++;
            return start;
        },
        down:function(){
            start--;
            return start;
        }
    }
}


function hero(name){
    let energy=100;
    return{
        
        jump:function(){
            energy=-5;
        },
        getEnergy:function(){
            return energy;
        }

    }
}
/*better practice for object
        |
        |
        V
*/
function hero(name){
    let energy=100;
        
    function jump(){
        energy=-5;
    }
    function getEnergy(){
        return energy;
    }
    return{
        jump,
        getEnergy
    }
    
}