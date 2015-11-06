<?php
// define variables and set to empty values
$nameErr = $emailErr =$passwordErr = "";
$name = $email = $password = "";

/*if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["name"])) {
    $nameErr = "Name is required";
  } else {
    $name = test_input($_POST["name"]);
  }*/

  $name = test_input($_POST["name"]);
if (!preg_match("/^[a-zA-Z ]*$/",$name)) {
  $nameErr = "Only letters and white space allowed"; 
}

 /* if (empty($_POST["email"])) {
    $emailErr = "Email is required";
  } else {
    $email = test_input($_POST["email"]);
  }*/  

  $email = test_input($_POST["email"]);
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
  $emailErr = "Invalid email format"; 
}


[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]
  
  $password = test_input($_POST["password"]);
if (!preg_match("/^[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]*$/",$password)) {
  $passwordErr = "password can be only letters digits and special characters"; 
}
  /*if (empty($_POST["password"])) {
    $passwordErr = "Password is required";
  } else {
    $website = test_input($_POST["password"]);
  }*/


function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?