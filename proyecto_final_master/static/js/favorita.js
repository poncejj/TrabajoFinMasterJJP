(function () {
    $('.table').DataTable();

    var sPath = window.location.pathname;
	$('a[href="'+ sPath +'"].nav-link').addClass('active');
  $('.datepicker').datepicker({
            format:'yyyy-mm-dd'
        });
    $( ".slider" ).slider({
	 	range: false,
      	min: 0,
      	max: 1,
      	step: 0.1,
      create: function() {
      	var obj = $(this).children().data('val');
        $(this).children().text( $( this ).slider( "value" ) );
      	$('#'+ obj).val( $( this ).slider( "value" ));
      },
      slide: function( event, ui ) {
        var obj = $(this).children().data('val');
        $(this).children().text( ui.value );
      	$('#' + obj).val( ui.value);
      }
    });
}())

function redirect_url(url){
	document.location.href = url;
}