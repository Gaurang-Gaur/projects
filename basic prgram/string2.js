// methods are just function that belong particular object or data type
let email="gauranggaur007@gmail.com";
console.log(email.indexOf('7')); 
// indexof is method on datatype string and we are passing arugement in it...
// common string methods...
let result=email.lastIndexOf('g');
console.log(result);
result=email.slice(2,10);
console.log(result,email);// this method doesnot modifies the original strings

//method hote to function he hai pe vo store kar te hai object properties
// vo ase function hota hai joke property hote hai like small kar ne ka function large kar ne function.
// jab kise bhi object ke property function bana diya jata hai to usse method kaha te hai...
// aur jab ko function ke property ko denote kar ta ho tu use method bhi kaha sak te hai my boi.
// JavaScript Methods: A JavaScript method is a property of an object that contains a function definition. Methods are functions stored as object properties. Object method can be accessed with the following syntax:

// Syntax:

// object = {
//     methodName: function() {
//         // Content
//     }
// };

// object.methodName()