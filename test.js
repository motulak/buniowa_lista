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


    $("button.ajax").click(function(){
        $.get("http://localhost:5000", function(data, status){
        $("#lista").html("Data: " + data[0].name + "\nStatus: " + status +'<br>');
        var text2 = "";
        for (i=0; i < lista_buni.length; i++) {
            text2 += data[i].name+ ' <i class="fa fa-circle-o" aria-hidden="true"></i>' + '<br/>';
        }
        $("#demo").html(text2)
    }



    );



        });




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
    { nameof : "szczoteczka do zębów", group : "higiena"}
    ]

});
