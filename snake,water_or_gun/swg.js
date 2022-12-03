let play = true;
let count = 0;
let comcount = 0;
while (play) {
  let game = ['s', 'g', 'w'];
  let guess = game[Math.floor(Math.random() * game.length)];
  console.log(guess);

  console.log("       let begin the game here");

  console.log("*******************************************");
  // console.log("checking");
  let user = prompt("enter your choices 's', 'w ' or 'g'");
  if (user == guess) {
    console.log("tie");


  }
  else if (user == "s" && guess == "w") {
    console.log("congrats ");
    count++;

  }
  else if (user == "w" && guess == "s") {
    console.log("you lose");
    comcount++;

  }
  else if (user == "g" && guess == "s") {
    console.log("congrats ");

    count++;

  }
  else if (user == "s" && guess == "g") {
    console.log("you lose");
    comcount++;

  }
  else if (user == "w" && guess == "g") {
    console.log("congrats ");

    count++;
  }
  else if (user == "g" && guess == "w") {
    console.log("you lose");
    comcount++;

  }
  console.log("total score of user till now " + count);
  console.log("total score of computer till now " + comcount);
  if (count < 10 || comcount < 10) {
    let again = confirm("wanna play again...");

    if (again == true) {
      play = true;
    }
    else
      play = false;
  }


  if (comcount >= 10 || count >= 10) {
    console.log("Game over ");
    console.log("your result");
    break;
  }



}
console.log("*******************************************");
console.log("total score of user till now " + count);
console.log("total score of computer till now " + comcount);
console.log("*******************************************");
if (count > comcount) {
  console.log("congralution you win the game");

}
else
  console.log("better luck next time");





