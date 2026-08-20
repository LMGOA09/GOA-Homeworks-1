//#3)
/*
 * What it is: A shorthand conditional operator in JavaScript written as
   `condition ? expressionIfTrue : expressionIfFalse`.
 * Why we need it: It provides a concise, readable alternative to traditional 
   if/else statements when assigning values or executing short expressions based 
   on a single condition, reducing boilerplate code.
  
 //Examples:
    1. let age = 20;
       let status = (age >= 18) ? "Adult" : "Minor";
    2. let score = 85;
       let grade = (score >= 50) ? "Pass" : "Fail";
    3. let isMember = true;
       let discount = isMember ? 0.20 : 0.05;
    4. let temperature = 30;
       let weather = (temperature > 25) ? "Hot" : "Pleasant";
    5. let userCount = 0;
       let message = userCount === 0 ? "No users found" : `${userCount} users active`;
 */

//#4)
let num1 = parseInt(prompt("Enter the first number:"), 10);
let num2 = parseInt(prompt("Enter the second number:"), 10);

if (num1 > num2) {
    console.log("The first number is greater than the second");
} else if (num2 > num1) {
    console.log("The second number is greater than the first");
} else {
    console.log("The numbers are equal");
}