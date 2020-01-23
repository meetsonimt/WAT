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
});
$(document).ready(function () {
  $(".proxy").hide();
  $("#term").hide();
});

$(document).ready(function(){
    $('#table').DataTable();
});