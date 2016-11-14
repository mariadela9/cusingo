/**
 * Created by carlos on 10/31/16.
 */
$(document).ready(function() {
    $('#comment_submit').click(create_comment);
    $(document).on('click','.comment_delete' , delete_comment);
});

function delete_comment() {
    $.ajax({
        url: $(this).attr('action'),
        type: "POST",
        error: function(err) {
            alert('Error happened');
        },
        success: function(result) {
            // make comment on screen
            var element = document.getElementById(result.element_id);
            $(element).parent().remove()
}})}

function create_comment() {
    $.ajax({
        url: $('#comment_submit').attr('action'),
        type: "POST",
        data: {
            title: $('#title').val(),
            content: $('#content').val()
        },
        error: function(err) {
            alert('Error happened');
        },
        success: function(result) {
            // make comment on screen
            $('#title').val('');
            $('#content').val('');
            // span creations
            var title_span = document.createElement("span");
            var title = document.createTextNode(result.title);
            title_span.appendChild(title);
            var author = document.createTextNode(result.author);
            var author_span = document.createElement("span");
            author_span.appendChild(author);
            var content = document.createTextNode(result.content);
            var content_span = document.createElement("span");
            content_span.appendChild(content);
            // div creations
            var title_div = document.createElement("div");
            var title_node = document.createTextNode("Title: ");
            title_div.appendChild(title_node);
            title_div.appendChild(title_span);
            var content_div = document.createElement("div");
            var content_node = document.createTextNode("Content: ");
            content_div.appendChild(content_node);
            content_div.appendChild(content_span);
            var author_div = document.createElement("div");
            var author_node = document.createTextNode("author: ");
            author_div.appendChild(author_node);
            author_div.appendChild(author_span);
            // delete button
            var delete_button = document.createElement("button");
            var button_node = document.createTextNode("Delete");
            delete_button.appendChild(button_node);
            delete_button.setAttribute("type", "submit");
            delete_button.setAttribute("id", "comment_"+result.comment_id+"_delete");
            delete_button.setAttribute("action", "/comments/"+result.comment_id+"/delete");
            delete_button.setAttribute("class", "comment_delete");
            var lcomment = document.createElement("div");
            // appending divs
            lcomment.setAttribute("class", "list_comments");
            lcomment.setAttribute("name", result.comment_id);
            lcomment.appendChild(title_div);
            lcomment.appendChild(author_div);
            lcomment.appendChild(content_div);
            lcomment.appendChild(delete_button);
            // appending this to html
            var place = document.getElementById("comment_place");
            place.appendChild(lcomment)
        }
    })
}