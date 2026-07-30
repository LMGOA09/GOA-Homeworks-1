//#3)
console.log("Objective 3");
let inputAge = prompt("Task 3: Enter your age:");
let Age = Number(inputAge);
let AgeList = [];

if (Age >= 18) {
  AgeList.push(true);
} else {
  AgeList.push(false);
}
console.log("Age List:", AgeList);

//#4)
console.log("Objective 4");
let numVal4 = Number(prompt("Task 4: Enter a number (Positive/Negative test):"));
let positive = [];
let negative = [];

if (numVal4 > 0) {
  positive.push(numVal4);
  console.log("Positive Array:", positive);
} else {
  negative.push(numVal4);
  console.log("Negative Array:", negative);
}

//#5)
console.log("Objective 5");
let numVal5 = Number(prompt("Task 5: Enter a number (Even/Odd test):"));
let Even = [];
let Odd = [];

if (numVal5 % 2 === 0) {
  Even.push(numVal5);
  console.log("Even Array:", Even);
} else {
  Odd.push(numVal5);
  console.log("Odd Array:", Odd);
}

//#6)
console.log("Objective 6");
let numbersArray = [10, 20, 30, 40, 50];
console.log("Original array (Task 6):", numbersArray);

numbersArray.shift(); 
console.log("After deleting first element:", numbersArray);


//#7)
console.log("Objective 7");
let colorsArray = ["Red", "Green", "Blue", "Yellow", "Purple"];
console.log("Original array (Task 7):", colorsArray);

colorsArray.pop(); 
console.log("After deleting last element:", colorsArray);

//#8)
console.log("Objective 8");
let Fruit = ["Apple", "Banana", "Orange"];
Fruit.unshift("Mango"); 
console.log("Fruit Array after unshift:", Fruit);

//#9)
console.log("Objective 9");
let num1 = Number(prompt("Calculator: Enter first number:"));
let operator = prompt("Calculator: Enter operator (+, -, *, /):");
let num2 = Number(prompt("Calculator: Enter second number:"));
let result;

if (operator === "+") {
  result = num1 + num2;
} else if (operator === "-") {
  result = num1 - num2;
} else if (operator === "*") {
  result = num1 * num2;
} else if (operator === "/") {
  result = num2 !== 0 ? num1 / num2 : "Error (Cannot divide by zero)";
} else {
  result = "Invalid operator!";
}

console.log(`Calculator Result: ${num1} ${operator} ${num2} = ${result}`);
alert(`Calculator Result: ${num1} ${operator} ${num2} = ${result}`);