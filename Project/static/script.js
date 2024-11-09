document.addEventListener("DOMContentLoaded", function() {
    // Example: Handle form submission for adding new classes, users, etc.
    document.querySelector("#add-class-form").addEventListener("submit", function(event) {
        event.preventDefault();
        // Handle the form submission logic here (e.g., sending a POST request to Flask backend)
    });
});