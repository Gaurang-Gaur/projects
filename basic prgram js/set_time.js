//setTimeout and Set interval
//arrow function...
// function sum(a,b){
//     return a+b;

// }
sum=(a,b)=>{
    return a+b;
}
logkaro=()=>{
    document.querySelectorAll(".container")[1].innerHTML="<b> we fire the set Timeout</b>"
    console.log("I am log karo function");
    
}
setTimeout(logkaro,1000);
// set interval is used to do repeated task;
