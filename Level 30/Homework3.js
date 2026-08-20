//#1)
function checkTemperature(temperature) {
  if (temperature > 20) {
    console.log("It's warm");
  } else {
    console.log("It's cold");
  }
}

//examples:
checkTemperature(25);
checkTemperature(15);

//#2)
function checkPassword(password) {
  if (password === "js_0101") {
    console.log("The password is correct");
  } else {
    console.log("The password is incorrect");
  }
}

//examples:
checkPassword("js_0101");
checkPassword("secret");