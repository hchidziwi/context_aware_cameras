<?php
// Database configuration
$servername = "";
$username = "";        
$password = "";            
$dbname = ""; 

// Connect to the database
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Get the device_id from the query parameter
if (!isset($_GET['device_id'])) {
    die("Device ID is required.");
}

$device_id = $conn->real_escape_string($_GET['device_id']);

// Query the database for the device status
$sql = "SELECT status FROM devices WHERE device_id = '$device_id'";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // Output the status
    $row = $result->fetch_assoc();
    echo $row['status'];
} else {
    // If the device ID is not found
    echo "0"; // Default to 0 if the device is not found
}

// Close the connection
$conn->close();
?>
