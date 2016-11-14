/**
 * Created by carlos on 11/7/16.
 */
$(document).ready(function() {
    $('#title').keyup(check_not_empty);
    $('#content').keyup(check_not_empty)
});

function check_not_empty() {
    if ($("#title").val() !== '') {
        if ($("#content").val() !== '') {
            $("#post_post").removeAttr('disabled');
        }
    }
}