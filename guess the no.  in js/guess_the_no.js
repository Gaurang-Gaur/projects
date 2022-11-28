// wap to generate a random no. and store it in a variable . the program then take an input from the user to tell them whether the guess correct or not greater or less than the original no.
// score of the game is decide by this method
// 100-(no. of guess )
//program will be terminted if it's guess correctly...
// range of random should be between 1,100.
let x = Math.floor((Math.random() * 100) + 1);
let counter = 0;
let i = 0;
console.log(x);

do {

  i = prompt("enter the no. you guessed");
  if (i < x) {
    console.log("guess bigger no..");
    counter++;
  }
  if (i > x) {
    console.log("guess the smaller no..");
    counter++;


  }
  if (i == x) {
    counter++;
  }

} while (x != i);

if (counter == 1) {
  console.log("\n \n*******Grand Master*******");

}
else if (counter < 10 && counter > 1) {
  console.log("Excellent guess Leader");
}
else if (counter > 10) {
  console.log("kinda average...");

} console.log("\n \nCongralution You guessed it right!");
console.log("\n            In " + counter + " chance");
