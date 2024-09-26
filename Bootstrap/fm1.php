<?php
// Database connection settings
$servername = "localhost";
$username = "root"; // Change this to your MySQL username
$password = ""; // Change this to your MySQL password
$dbname = "user";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect form data
    $email = htmlspecialchars($_POST['email']);
    $password = htmlspecialchars($_POST['pass']);
    $remember = isset($_POST['check']) ? 1 : 0; // Store as integer (1 for true, 0 for false)

    // Hash the password before storing it
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Prepare and bind
    $stmt = $conn->prepare("INSERT INTO signup (email, password, remember) VALUES (?, ?, ?)");
    $stmt->bind_param("ssi", $email, $hashed_password, $remember);

    // Execute the statement
    if ($stmt->execute()) {
        echo "<h2>Form Data Received:</h2>";
        echo "<p>Email: " . $email . "</p>";
        echo "<p>Password: (hashed, not displayed)</p>";
        echo "<p>Remember Me: " . ($remember ? 'Yes' : 'No') . "</p>";
        echo "<p>Data successfully saved!</p>";
    } else {
        echo "Error: " . $stmt->error;
    }

    // Close the statement
    $stmt->close();
}

// Close the connection
$conn->close();
?>
