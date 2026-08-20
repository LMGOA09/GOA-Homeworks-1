//#6)
for (let i = 1; i <= 100; i++) {
  if (i % 5 === 0) {
    console.log(i);
  }
}

//#7)
for (let i = 1; i <= 30; i++) {
  if (i % 4 === 0) {
    console.log(i);
  }
}

//#8)
let product = 1;
for (let i = 1; i <= 10; i++) {
  product *= i;
}
console.log("Product:", product);

//#9)
function printUpToN(N) {
  for (let i = 1; i <= N; i++) {
    console.log(i);
  }
}

let N = 7;
printUpToN(N);

//#10)
function countUpToN(N) {
  let count = 0;
  for (let i = 1; i <= N; i++) {
    count++;
  }
  return count;
}

let N = 25;
console.log(`Total count from 1 to ${N}:`, countUpToN(N));