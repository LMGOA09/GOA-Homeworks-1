//#3)
let count = 1;

while (count <= 10) {
  console.log(count);
  count++;
}

//#4)
let num = 2;

while (num <= 100) {
  console.log(num);
  num += 2;
}

//#5)
let times = parseInt(prompt("Enter a number:"), 10);
let count = 0;

while (count < times) {
  console.log("Hello World");
  count++;
}

//#6)
function getOddNumbers() {
  const oddArray = [];
  let num = 1;

  while (num <= 50) {
    oddArray.push(num);
    num += 2;
  }

  return oddArray;
}

//example:
const result = getOddNumbers();
console.log(result);

//#7)
function checkStatus(status) {
  if (status === 1) { // Online
    console.log("-----------------------------");
    console.log("0101011111111101111100000011001");
    console.log("--------------------------------------------");
    console.log("0101011111111101111100000011001");
  } else {
    console.log("Offline");
  }
}

//example:
checkStatus(1);
checkStatus(0);