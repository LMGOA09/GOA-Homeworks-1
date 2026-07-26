//#6)
//Scope determines where variables are accessible or visible in your code. It acts as a boundary that dictates where 
//a variable can be used or referenced.

//JS has three types of scope: Global Scope, Function Scope, and Block Scope. 
//1. Global Scope means the variable is accessible from anywhere in the code; 
//2. Function Scope means the variable is only accessible within the function it was declared in; 
//3. Block Scope means the variable is only accessible within the block (e.g., inside a loop or an if statement) it was declared in.


//#7)
// 1. Scope:
// - var is function-scoped. It ignores block boundaries like if-statements or loops.
// - let and const are block-scoped. They only exist inside the closest curly braces {}.

// 2. Re-declaration:
// - var allows you to re-declare the same variable name in the same scope.
// - let and const DO NOT allow re-declaration in the same scope (throws a SyntaxError).

// 3. Temporal Dead Zone (TDZ):
// - var is hoisted to the top and initialized with 'undefined' (can be accessed before declaration).
// - let and const are hoisted but NOT initialized. Accessing them before declaration causes a ReferenceError.

// 4. Global Object Attachment:
// - Global var variables attach themselves to the window object (window.myVar).
// - Global let and const variables do NOT attach to the window object.

//Example demonstrating scope differences:
    if (true) {
     var x = 10;  // Accessible outside this block
     let y = 20;  // ONLY accessible inside this block
    }

   console.log(x); // 10
   console.log(y); // Uncaught ReferenceError: y is not defined