
// 1
console.log("I'm printing to console!");
// 2
const username = prompt("Type your name.");
console.log("Hello, " + username + "!");
// 3
const a = Number(prompt("Enter first integer:"));
const b = Number(prompt("Enter second integer:"));
const c = Number(prompt("Enter third integer:"));
const sum = a + b + c;
const product = a * b * c;
const average = sum / 3;
console.log("sum:" + sum);
console.log("product:" + product);
console.log("average:" + average);
// 4
function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}
const studentname = prompt("Enter the student's name:");
const number = getRandomInt(4) + 1;
if (number === 1) {
    house = "Gryffindor";
} else if (number === 2) {
    house = "Slytherin";
} else if (number === 3) {
    house = "Hufflepuff";
} else {
    house = "Ravenclaw";
}
console.log(studentname + ", you are "+ house);
//5
const year = prompt("Enter a year:");
if (year % 4 === 0) {
    console.log("this is a leap year");
}
    else if (year % 100 === 0 , year % 400 === 0) {
        console.log("this is a leap year");
}
    else {
        console.log("this is not a leap year");
}
//7
const rolls = Number(prompt("How many rolls?"));
let dicesum = 0;
for (let i = 0; i < rolls; i++) {
    const die = Math.floor(Math.random() * 6) + 1;
    dicesum += die;
}
console.log("dices sum:" + dicesum);
