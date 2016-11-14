/**
 * Created by carlos on 11/6/16.
 */
$(document).ready(function() {
    $(".password").keyup(check_passwords)
});

function check_passwords() {
    if ($("#password").val() !== $("#password2").val()) {
        $("#passwords_match").show();
        $("#signup").attr('disabled','disabled');
    }
    if ($("#password").val() == $("#password2").val()) {
        $("#passwords_match").hide();
        if ($("#username").val() !== '') {
            $("#signup").removeAttr('disabled');
        }
    }
}