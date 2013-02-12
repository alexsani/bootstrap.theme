jq(document).ready(function() {
    // if text input field value is not empty show the "X" button
    $("#portal-searchbox .searchField ").keyup(function() {
        $("#portal-searchbox #delete #x").fadeIn();
        if ($.trim($("#portal-searchbox .searchField ").val()) == "") {
            $("#portal-searchbox #delete #x").fadeOut();
        }
    });
    // on click of "X", delete input field value and hide "X"
    $("#portal-searchbox #delete #x").click(function() {
        $("#portal-searchbox .searchField ").val("");
        $(this).hide();
    });
});