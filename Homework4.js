//#1)
for (let i = 1; i < 15; i++) {
  console.log(i);
}

//#2)
for (let i = 20; i > 1; i--) {
  console.log(i);
}

//#3)
let sum = 0;
for (let i = 1; i <= 50; i++) {
  sum += i;
}
console.log("Sum:", sum);

//#4)
function printTable(num) {
  for (let i = 1; i <= 10; i++) {
    console.log(`${num} x ${i} = ${num * i}`);
  }
}
printTable(5);

//#5)
function sumToN(N) {
  let sum = 0;
  for (let i = 1; i <= N; i++) {
    sum += i;
  }
  return sum;
}
let N = 10;
console.log(`Sum from 1 to ${N}:`, sumToN(N));