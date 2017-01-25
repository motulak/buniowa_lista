/**
 * Created by P on 25.01.2017.
 */

$(document).ready(function(){
    $("p").click(function(){
        $(this).hide();
        $("#demo").html("<h2>Dzki dzik</h2>")

    });


    $(".field").click(function () {
        $(this).text("F");

        }

    )


    $(".field").dblclick(function () {
            $(this).text("O");

        }

    )



});
