$(document).ready(function () {
    $("#proxyCheck").click(function () {
        $(".proxy").toggle(500);
    });
   
    $('#searchRadio').on('change', function () {
        if ($(this).is(':checked')) {
            $("#term").show();
        }
    });
    $('#productRadio').on('change', function () {
        if ($(this).is(':checked')) {
            $("#term").hide();
        }
    });
    $(".copyToClip").click(function() {
        var $row = $(this).closest("tr");    // Find the row
        var $text = $row.find(".har").text(); // Find the text
        var $temp = $("<input>");
        $("body").append($temp);
        $temp.val($text).select();
        document.execCommand("copy");
        $temp.remove();
    });
    $("#table tbody tr td .jsonContent").JSONView();

});
$(document).ready(function () {
    $(".proxy").hide();
    $("#term").hide();
});

$(document).ready(function () {
    $('#table').DataTable({
        responsive: true
    });
});

/*$('#table tbody tr td button .copyToClip').on('click', function () {
    var data = table.row(this).data();
    alert('You clicked on ' + data[0] + '\'s row');
});*/