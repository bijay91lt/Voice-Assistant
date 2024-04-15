$(document).ready(function() {
    $('#registrationForm').submit(function(event) {
        event.preventDefault(); // Prevent default form submission

        // Get form data
        var username = $('#username').val();
        var password = $('#password').val();

        // Send form data to Flask backend
        $.ajax({
            type: 'POST',
            url: '/register',
            contentType: 'application/json', // Set content type to JSON
            dataType: 'json', // Expect JSON response
            data: JSON.stringify({ 'username': username, 'password': password }),
            success: function(response) {
                // Handle success response
                alert(response.message);
                // Redirect user to login page or perform any other action
            },
            error: function(xhr, status, error) {
                // Handle error response
                alert('Failed to register user. Please try again.');
            }
        });
    });
});
