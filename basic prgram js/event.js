//event is js 
// two way to access event are 
//1. directly in html
function clicked(){
    console.log('the button was clicked');

    
// }
// window.onload=function(){
//     console.log("this document was loaded");
    
// }
firstContainer.addEventListener("click",function()    {
    document.querySelectorAll(".container")[1].innerHTML="<b> we have Clicked</b>"
console.log('Click is done!');

//     }
// );// see event are in small case ...
// firstContainer.addEventListener("mouseover",function()    {
//     console.log('MOuse on container!');
    
//         }
//     );
//     firstContainer.addEventListener("mouseout",function()    {
//         console.log('MOuse out of container!');
        
//             }
// //         );
//         firstContainer.addEventListener("mouseup",function()    {
//             console.log('MOuse up on container!');
            
//                 }
//             );firstContainer.addEventListener("mousedown",function()    {
//                 console.log('MOuse down on  container!');
                
//                     }
//                 );
    