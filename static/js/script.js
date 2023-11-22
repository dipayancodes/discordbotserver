$(document).ready(function() {
    $('#uploadForm').submit(function(e) {
        e.preventDefault();
        $.ajax({
            url: '/upload',
            type: 'post',
            data: new FormData(this),
            contentType: false,
            processData: false,
            success: function(response) {
                alert(response.message);
            }
        });
    });

    $('#executeForm').submit(function(e) {
        e.preventDefault();
        $.ajax({
            url: '/execute',
            type: 'post',
            data: { filename: $('input[name="filename"]').val() },
            success: function(response) {
                if(response.output) {
                    $('#output').text(response.output);
                } else {
                    $('#output').text(response.error || response.message);
                }
            }
        });
    });
});

