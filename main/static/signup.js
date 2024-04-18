document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("signupForm").addEventListener("submit", function(event) {
        var usernameInput = document.getElementById("inputUsername").value;
        var passwordInput = document.getElementById("inputPassword").value;
        var confirmPasswordInput = document.getElementById("confirmInputPassword").value;
        var regex = /[!@#$%^&*(),.?":{}|<>]/;

        // Check if username contains special characters
        if (regex.test(usernameInput)) {
            alert("Please avoid using special characters in the username.");
            event.preventDefault(); // Prevent form submission if username contains special characters
        }

        // Check if passwords match
        if (passwordInput !== confirmPasswordInput) {
            alert("Passwords do not match. Please make sure your passwords match.");
            event.preventDefault(); // Prevent form submission if passwords don't match
        }
    });
});
