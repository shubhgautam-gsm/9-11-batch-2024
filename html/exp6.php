<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST["language"])) {
        $selected_language = $_POST["language"];
        switch ($selected_language) {
            case "en":
                echo "You selected English.";
                break;
            case "fr":
                echo "Vous avez sélectionné le français."; // Displayed in French
                break;
            case "de":
                echo "Sie haben Deutsch ausgewählt."; // Displayed in German
                break;
            case "es":
                echo "Seleccionaste español."; // Displayed in Spanish
                break;
            default:
                echo "Invalid language selection.";
        }
    } else {
        echo "Please select a language!";
    }
}
?>
