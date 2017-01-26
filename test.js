/**
 * Created by P on 25.01.2017.
 */

$(document).ready(function(){

    $("#load_list").click(function(){
        $.get("http://127.0.0.1:5000", function(jdata, status){
        var data = JSON.parse(jdata)
        var text2 = "";
        for (i=0; i < data.length; i++) {
            text2 += data[i].name+ ' <input type="checkbox">' + '<br/>';
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

});
