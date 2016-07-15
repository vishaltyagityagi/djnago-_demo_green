$(function(){

// using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $('#id_q').on('keyup', function () {
     console.log($('#id_q').val());
var s = $('#id_q').val()
       $.ajax({
           type: 'GET',
           url: 'http://localhost:8000/usersearch/?csrfmiddlewaretoken=SoNwPE3bOXwta4yAWWeZ5Wqeha0XdSwQ&q='+s,
           data: {
               'csrfmiddlewaretoken=SoNwPE3bOXwta4yAWWeZ5Wqeha0XdSwQ&q' : $('#id_q').val(),
               // 'csrfmiddlewaretoken': getCookie('csrftoken')
           },
           success: function(response){
               $('.django-admin-cstm').html(response)


           }
       })
    });

});
