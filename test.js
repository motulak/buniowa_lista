/**
 * Created by P on 25.01.2017.
 */

$(document).ready(function(){
    $("button.lista").click(function(){
        $(this).hide();
        var text = "";
        for (i=0; i < lista_buni.length; i++) {
            text += lista_buni[i].nameof+ '<i class="fa fa-circle-o" aria-hidden="true"></i>' + '<br/>';
        }
        $("#demo").html(text)

        });


    $("#load_list").click(function(){
        $.get("http://127.0.0.1:5000", function(jdata, status){
        var data = JSON.parse(jdata)
        $("#lista").html("Data: " + data + "\nStatus: " + status +'<br>');
        var text2 = "";
        for (i=0; i < data.length; i++) {
            text2 += data[i].name+ ' <i class="fa fa-circle-o" aria-hidden="true"></i>' + '<br/>';
        }
        $("#demo").html(text2)
    }
    );      });




    $(".field").click(function () {
        if ($(this).hasClass("explosion") !== true) {
            $(this).addClass("flaged");
            $(this).text(" ");
        }

        }

    )


    $(".field").dblclick(function () {
            $(this).text(" ");
            $(this).removeClass("flaged");
            $(this).addClass("explosion")



        }

    )

var lista_buni = [
    { nameof : "recznik", group : "higiena"},
    ]

});
