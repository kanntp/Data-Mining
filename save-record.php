<?php

// เชื่อมต่อกับฐานข้อมูล หรือใช้วิธีอื่นที่เหมาะสมกับการเก็บข้อมูล
$servername = "localhost";
$username = "username";
$password = "password";
$dbname = "myDB";

$conn = new mysqli($servername, $username, $password, $dbname);

// ตรวจสอบการเชื่อมต่อฐานข้อมูล
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// รับค่าจากฟอร์ม
 $hours_per_day = $_POST['field1'];
  $taken_inputs = $_POST['dropdown1'];
  $worker_type = $_POST['dropdown2'];
  $worked_in_teams = $_POST['dropdown3'];
  $coding_skills = $_POST['dropdown4'];
  $self_learning = $_POST['dropdown5'];
  $interested_subjects = $_POST['dropdown6'];
  $communication_skills = $_POST['dropdown7'];

// นำข้อมูลเข้าฐานข้อมูล
$sql = "INSERT INTO records (hours_working, taken_input, worker_type, worked_in_teams, coding_skill_rating, self_learning, interested_subjects, communication_skill_percentage)
VALUES ('$field1', '$dropdown2_1', '$dropdown2_2', '$dropdown2_3', '$dropdown2_4', '$dropdown2_5', '$dropdown2_6', '$dropdown3')";

if ($conn->query($sql) === TRUE) {
  echo "Record saved successfully";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}

// ปิดการเชื่อมต่อฐานข้อมูล
$conn->close();

?>
// dbชื่อ db.save มีตารางชื่อว่า records ซึ่งมี

hours_working (VARCHAR)
taken_input (VARCHAR)
worker_type (VARCHAR)
worked_in_teams (VARCHAR)
coding_skill_rating (VARCHAR)
self_learning (VARCHAR)
interested_subjects (VARCHAR)
communication_skill_percentage (VARCHAR)