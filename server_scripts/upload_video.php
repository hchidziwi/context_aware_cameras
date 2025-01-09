<?php
// Database connection
$servername = ""; 
$username = "";
$password = "";
$dbname = "";


// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Directory paths
    $indoorDir = "videos/indoor/";
    $outdoorDir = "videos/outdoor/";

    // Ensure directories exist
    if (!is_dir($indoorDir)) {
        mkdir($indoorDir, 0777, true);
    }
    if (!is_dir($outdoorDir)) {
        mkdir($outdoorDir, 0777, true);
    }

    // Get label and device_id from the POST request
    $label = $_POST['label'];
    $deviceId = $_POST['device_id'];

    // Handle image file upload
    if (isset($_FILES['file'])) {
        $fileTmpPath = $_FILES['file']['tmp_name'];
        $fileName = $_FILES['file']['name'];

        // Determine upload folder based on label
        $uploadDir = $label === 'Indoors' ? $indoorDir : $outdoorDir;
        $destPath = $uploadDir . basename($fileName);

        if (move_uploaded_file($fileTmpPath, $destPath)) {
            // Record video details in the database
            //$uploadTime = date('Y-m-d H:i:s');
            $stmt = $conn->prepare("INSERT INTO videos (device_id, label, path) VALUES (?, ?, ?)");
            $stmt->bind_param("sss", $deviceId, $label, $destPath);

            if ($stmt->execute()) {
                echo "Image uploaded and recorded successfully.";
            } else {
                echo "Error recording image details in the database: ";
            }

            $stmt->close();
        } else {
            echo "Error moving the uploaded file." . $_FILES['file'];
        }
    } else {
        echo "Error with the uploaded file: " . $_FILES['file'];
    }
}

$conn->close();
?>
