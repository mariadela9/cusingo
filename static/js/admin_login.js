
$(document).ready(function() {
    $('input').keyup(validate_admin)
});

function validate_admin() {
    if ($("#username").val() !== 'admin') {
        if ($("#password").val !== 'password') {


}