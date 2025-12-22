
// 1
console.log("I'm printing to console!");
// 2
const username = prompt("Type your name.");
document.getElementById("output").innerHTML += ("Hello, " + username + "!<br>");
// 3
const a = Number(prompt("Enter first integer:"));
const b = Number(prompt("Enter second integer:"));
const c = Number(prompt("Enter third integer:"));
const sum = a + b + c;
const product = a * b * c;
const average = sum / 3;
document.getElementById("output").innerHTML +=
    "Sum: " + sum + "<br>" +
    "Product: " + product + "<br>" +
    "Average: " + average + "<br><br>";
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
document.getElementById("output").innerHTML +=
    studentname + ", you are " + house;
//5
const year = prompt("Enter a year:");
let result;
if (year % 400 === 0) {
    result = "this is a leap year"
}
    else if (year % 100 === 0) {
        result = "this is not a leap year"
    }
    else if (year % 4 === 0) {
        result = "this is a leap year"
}
    else {
        result = "this is not a leap year"
}
//7
const rolls = Number(prompt("How many rolls?"));
let dicesum = 0;
for (let i = 0; i < rolls; i++) {
    const die = Math.floor(Math.random() * 6) + 1;
    dicesum += die;
}
console.log("dices sum:" + dicesum);
