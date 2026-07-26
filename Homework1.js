//#1)
/*
 prompt()
 * What it is: A built-in browser method that displays a dialog box with an 
   optional message prompting the user to input some text.
 * Why we need it: It allows for simple, synchronous user input in web environments 
   without needing to build complex HTML input fields and event listeners.
*/
let userInput = prompt("Please enter a value:");

/*
 parseInt()
 * What it is: A built-in JavaScript function that parses a string argument 
   and returns an integer of the specified radix (base).
 * Why we need it: Because inputs from sources like `prompt()` or forms are 
   frequently strings, we cannot perform proper mathematical addition on them 
   (e.g., "5" + "5" becomes "55"). `parseInt()` converts that string into a 
   usable number format (e.g., converting "5" into the number 5).
*/
let convertedNumber = parseInt("42", 10);

//#2)
/*
 Logical AND (&&)
 * What it is: Returns true if and only if all operands are true. If any 
   operand is false, it returns false (short-circuits on the first false).
 * Why we need it: To ensure multiple conditions are met simultaneously 
   before executing code (e.g., checking if a user is logged in AND is an admin).*/
 
   //Examples:
   // 1. let result1 = true && true;   // Evaluates to: true
   // 2. let result2 = true && false;  // Evaluates to: false
   // 3. let age = 20; hasID = true;
   //    let canEnter = (age >= 18 && hasID); // Evaluates to: true
   // 4. let x = 5;
   //    let check = (x > 0 && x < 10);    // Evaluates to: true

 /*Logical OR (||)
 * What it is: Returns true if at least one of the operands is true. It 
 * returns false only if all operands are false (short-circuits on the first true).
 * Why we need it: To execute code when any one of several alternative conditions 
 * is satisfied (e.g., a user can pay with a credit card OR PayPal).
   
 Examples:*/
 // 1. let result1 = true || false;  // Evaluates to: true
 // 2. let result2 = false || false; // Evaluates to: false
 // 3. let isWeekend = true; isHoliday = false;
 //    let canSleepIn = (isWeekend || isHoliday); // Evaluates to: true
 // 4. let userRole = "guest";
 //    let hasAccess = (userRole === "admin" || userRole === "moderator"); // Evaluates to: false

 /*Logical NOT (!)
 * What it is: A unary operator that takes truthy/falsy values and inverts them. 
 * True becomes false, and false becomes true.
 * Why we need it: To check for the negative condition or inverse state 
   (e.g., checking if a user is NOT logged out, or toggling a boolean switch).
 
   Examples:
   1. let result1 = !true;          // Evaluates to: false
   2. let result2 = !false;         // Evaluates to: true
   3. let isLoggedIn = false;
      let showLoginPrompt = !isLoggedIn; // Evaluates to: true
   4. let isEmpty = ![];          // Evaluates to: false (since non-empty array is truthy)
 */