/**
 * Created by P on 25.01.2017.
 */

$(document).ready(function(){

    $("#load_list").click(function(){
        var loader = '<i class="fa fa-refresh fa-spin fa-2x fa-fw"></i>'
        loader += '<span class="sr-only">Loading...</span>'
        $("#demo").html(loader);
//        $.get("http://127.0.0.1:5000/get/1/", function(jdata, status)
        var token = $("#user-token").val()
        $.ajax({
         url: "http://127.0.0.1:5000/get/1/",
         type: "GET",
         beforeSend: function(xhr){xhr.setRequestHeader( 'token', token);},
         success: function(jdata)        {
            var data = jdata
            var table = '<table id="items">';
            for (i=0; i < data.length; i++) {
                table +='<tr><td>' + data[i].name + '</td><td> <input type="checkbox"></td><td> <input type="checkbox"></td></tr>';
            }
            table +='</table>'
            $("#demo").html(table)
    },
        statusCode: {
            403 : function() {
             $("#demo").html('<div class="alert alert-danger"><strong>Not authorized!</strong> Wrong or empty token.</div>')
            }

        }
          });
          });


    $("#clear_list").click(function(){
        $("#demo").empty();
    } )


    $(".field").click(function () {
        if ($(this).hasClass("explosion") !== true) {
            $(this).addClass("flaged");
            $(this).html('');
        }

        }

    )


    $(".field").dblclick(function () {
            $(this).text(" ");
            $(this).removeClass("flaged");
            $(this).addClass("explosion")



        }

    )

});
